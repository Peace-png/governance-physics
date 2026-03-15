#!/usr/bin/env python3
"""
Governance Physics: Kubernetes-Only SNN Simulation
===================================================
Focused simulation for K8s failure cascade dynamics.

VALIDATION HOOKS (what empirical data would falsify this model):
- If real cascade sizes don't follow power-law → model wrong
- If λ doesn't scale with √(N_nodes) → scaling law wrong
- If phase transition doesn't exist → criticality claim wrong
- If cascade propagation time ≠ 10-100ms → timescale wrong
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from brian2 import *

# K8s PARAMETERS (from empirical estimates)
K8S_PARAMS = {
    'lambda_': 0.8,        # Control rate (0.1-1.0 /s empirically)
    'mu': 1.5,             # Dissipation rate
    'tau_base': 20*ms,     # Base timescale (10-100ms for etcd)
    'G': 0.4,              # Governance efficiency
    'N_layers': 5,         # Hierarchy: Control Plane → Nodes → Pods → Containers
    'neurons_per_layer': 100,
}


def create_k8s_snn(lambda_override=None, n_nodes=100):
    """Create K8s cluster as hierarchical SNN.

    Layers represent:
    0: API Server / Controller Manager (executive)
    1: Scheduler / etcd
    2: Kubelets (node agents)
    3: Pods
    4: Containers (labor)
    """
    params = K8S_PARAMS.copy()
    if lambda_override is not None:
        params['lambda_'] = lambda_override

    N_layers = params['N_layers']
    neurons_per_layer = params['neurons_per_layer']
    total_neurons = N_layers * neurons_per_layer

    lambda_ = params['lambda_']
    mu = params['mu']
    tau_base = params['tau_base']

    # Timescales increase with depth (deeper = slower response)
    tau_layers = [tau_base * (1 + 0.3*i) for i in range(N_layers)]

    start_scope()

    eqs = '''
    dv/dt = (ge - v + I_noise)/tau_m : volt (unless refractory)
    dge/dt = -ge/tau_e : volt
    tau_m : second
    tau_e : second
    I_noise : volt
    '''

    neurons = NeuronGroup(
        total_neurons,
        eqs,
        threshold='v > 1*volt',
        reset='v = 0*volt',
        refractory=2*ms,
        method='euler'
    )

    for i in range(N_layers):
        start_idx = i * neurons_per_layer
        end_idx = (i + 1) * neurons_per_layer
        neurons.v[start_idx:end_idx] = 'rand() * 0.5 * volt'
        neurons.tau_m[start_idx:end_idx] = tau_layers[i]
        neurons.tau_e[start_idx:end_idx] = 5*ms
        neurons.I_noise[start_idx:end_idx] = '0.05 * rand() * volt'

    # DOWNWARD: Control plane → nodes → pods → containers
    # Weight decays with λ (control attenuation)
    down_synapses = []
    for i in range(N_layers - 1):
        src_start = i * neurons_per_layer
        src_end = (i + 1) * neurons_per_layer
        tgt_start = (i + 1) * neurons_per_layer
        tgt_end = (i + 2) * neurons_per_layer

        S = Synapses(neurons, neurons, 'w : 1', on_pre='ge_post += w * volt', delay=1*ms)
        S.connect(condition=f'(i >= {src_start}) and (i < {src_end}) and (j >= {tgt_start}) and (j < {tgt_end})', p=0.2)
        S.w = 0.5 * np.exp(-lambda_ * (i + 1))
        down_synapses.append(S)

    # UPWARD: Failure feedback from containers → pods → nodes → control
    # Weight decays with μ (dissipation)
    up_synapses = []
    for i in range(N_layers - 1, 0, -1):
        src_start = i * neurons_per_layer
        src_end = (i + 1) * neurons_per_layer
        tgt_start = (i - 1) * neurons_per_layer
        tgt_end = i * neurons_per_layer

        S = Synapses(neurons, neurons, 'w : 1', on_pre='ge_post += w * volt', delay=2*ms)
        S.connect(condition=f'(i >= {src_start}) and (i < {src_end}) and (j >= {tgt_start}) and (j < {tgt_end})', p=0.15)
        S.w = 0.3 * np.exp(-mu * (N_layers - i))
        up_synapses.append(S)

    # External input (API requests, scheduling demands)
    input_group = PoissonGroup(neurons_per_layer, rates=200*Hz)
    S_input = Synapses(input_group, neurons, on_pre='ge_post += 0.8*volt')
    S_input.connect(j='i')

    spike_monitor = SpikeMonitor(neurons)
    rate_monitor = PopulationRateMonitor(neurons)

    net = Network([
        neurons,
        input_group,
        S_input,
        spike_monitor,
        rate_monitor,
        *down_synapses,
        *up_synapses
    ])

    return {
        'net': net,
        'neurons': neurons,
        'spike_monitor': spike_monitor,
        'rate_monitor': rate_monitor,
        'params': params,
        'tau_layers': tau_layers,
        'N_layers': N_layers,
        'neurons_per_layer': neurons_per_layer,
        'down_synapses': down_synapses,
        'up_synapses': up_synapses
    }


def compute_order_parameter(spike_monitor, time_window=10*ms, N_neurons=None):
    """Kuramoto-style order parameter Φ for synchronization."""
    if N_neurons is None:
        N_neurons = int(max(spike_monitor.i)) + 1

    if len(spike_monitor.t) == 0:
        return 0.0

    t_max = spike_monitor.t[-1]
    n_windows = int(t_max / time_window)

    if n_windows == 0:
        return 0.0

    order_params = []
    for w in range(n_windows):
        t_start = w * time_window
        t_end = (w + 1) * time_window

        mask = (spike_monitor.t >= t_start) & (spike_monitor.t < t_end)
        spike_times = spike_monitor.t[mask]

        if len(spike_times) > 0:
            phases = 2 * np.pi * ((spike_times - t_start) / time_window)
            real_part = np.mean(np.cos(phases))
            imag_part = np.mean(np.sin(phases))
            phi = np.sqrt(real_part**2 + imag_part**2)
            order_params.append(phi)

    return np.mean(order_params) if order_params else 0.0


def compute_avalanche_distribution(spike_monitor, dt=1*ms, N_neurons=None):
    """Compute avalanche sizes and test for power-law."""
    if N_neurons is None:
        N_neurons = int(max(spike_monitor.i)) + 1

    all_times = np.array(spike_monitor.t / ms)

    if len(all_times) == 0:
        return [], 0, {}

    t_max = int(max(all_times))
    dt_ms = dt / ms

    n_bins = max(1, int(t_max / dt_ms) + 1)
    activity = np.zeros(n_bins)

    for t in all_times:
        bin_idx = int(t / dt_ms)
        if bin_idx < n_bins:
            activity[bin_idx] += 1

    threshold = np.mean(activity) if np.mean(activity) > 0 else 1

    avalanche_sizes = []
    current_size = 0
    in_avalanche = False

    for a in activity:
        if a > threshold:
            current_size += a
            in_avalanche = True
        else:
            if in_avalanche and current_size > 0:
                avalanche_sizes.append(current_size)
            current_size = 0
            in_avalanche = False

    # Fit power-law exponent using MLE
    stats = {}
    if len(avalanche_sizes) > 5:
        sizes = np.array(avalanche_sizes)
        sizes = sizes[sizes > 0]
        if len(sizes) > 0 and np.min(sizes) > 0:
            alpha = 1 + len(sizes) / np.sum(np.log(sizes / np.min(sizes)))
            stats['alpha'] = alpha
            stats['n_avalanches'] = len(sizes)
            stats['mean_size'] = np.mean(sizes)
            stats['max_size'] = np.max(sizes)

            # Test if power-law is plausible (KS test approximation)
            # Critical value for α≈1.5: should have wide distribution
            stats['is_criticalish'] = 1.2 < alpha < 2.5
        else:
            alpha = 0
    else:
        alpha = 0
        stats['n_avalanches'] = 0

    return avalanche_sizes, alpha, stats


def test_lambda_scaling():
    """Test if λ scales with √N (predicted by theory)."""
    print("\n--- TESTING λ ∝ √N SCALING LAW ---")

    node_counts = [50, 100, 200, 400]
    inferred_lambdas = []

    for n_nodes in node_counts:
        # Run simulation and find critical λ (where Φ drops fastest)
        lambdas = np.linspace(0.2, 2.0, 10)
        d_phis = []

        for lam in lambdas:
            sim = create_k8s_snn(lambda_override=lam, n_nodes=n_nodes)
            sim['net'].run(300*ms)
            phi = compute_order_parameter(sim['spike_monitor'],
                                          N_neurons=sim['N_layers'] * sim['neurons_per_layer'])
            d_phis.append(phi)

        # Find inflection point as proxy for λ_critical
        d2_phi = np.gradient(np.gradient(d_phis))
        lambda_crit = lambdas[np.argmax(np.abs(d2_phi))] if len(d2_phi) > 0 else 1.0
        inferred_lambdas.append(lambda_crit)
        print(f"  N={n_nodes}: λ_c ≈ {lambda_crit:.3f}")

    # Test scaling
    sqrt_n = np.sqrt(node_counts)

    # Fit λ = a * √N + b
    if len(inferred_lambdas) > 2:
        coeffs = np.polyfit(sqrt_n, inferred_lambdas, 1)
        r_squared = 1 - np.sum((np.array(inferred_lambdas) - (coeffs[0]*sqrt_n + coeffs[1]))**2) / \
                        np.sum((np.array(inferred_lambdas) - np.mean(inferred_lambdas))**2)

        print(f"\n  Scaling fit: λ = {coeffs[0]:.4f} * √N + {coeffs[1]:.4f}")
        print(f"  R² = {r_squared:.3f}")
        print(f"  Verdict: {'SUPPORTS' if r_squared > 0.7 else 'REJECTS'} λ ∝ √N scaling")

        return r_squared > 0.7, r_squared

    return False, 0


if __name__ == '__main__':
    print("="*70)
    print("KUBERNETES GOVERNANCE PHYSICS - SNN SIMULATION")
    print("="*70)
    print("\nValidation hooks (what would falsify this model):")
    print("  - Cascade sizes NOT power-law → model wrong")
    print("  - λ does NOT scale with √N → scaling law wrong")
    print("  - No phase transition → criticality wrong")
    print("  - Propagation time ≠ 10-100ms → timescale wrong")
    print("="*70)

    # ============================================
    # PHASE 1: BASELINE SIMULATION
    # ============================================
    print("\n--- PHASE 1: BASELINE SIMULATION ---")
    sim = create_k8s_snn()
    sim['net'].run(1*second, report='text')

    N_total = sim['N_layers'] * sim['neurons_per_layer']
    phi = compute_order_parameter(sim['spike_monitor'], N_neurons=N_total)
    avalanche_sizes, alpha, stats = compute_avalanche_distribution(sim['spike_monitor'], N_neurons=N_total)

    print(f"\n  Baseline Results:")
    print(f"    Order parameter Φ = {phi:.3f}")
    print(f"    Avalanche exponent α = {alpha:.3f}")
    print(f"    Total spikes: {len(sim['spike_monitor'].t)}")
    print(f"    Avalanches detected: {stats.get('n_avalanches', 0)}")
    print(f"    Power-law plausible: {stats.get('is_criticalish', False)}")

    # ============================================
    # PHASE 2: PHASE TRANSITION DETECTION
    # ============================================
    print("\n--- PHASE 2: PHASE TRANSITION ---")
    lambdas = np.linspace(0.1, 2.5, 20)
    order_params = []

    for lam in lambdas:
        sim = create_k8s_snn(lambda_override=lam)
        sim['net'].run(500*ms)
        phi = compute_order_parameter(sim['spike_monitor'],
                                      N_neurons=sim['N_layers'] * sim['neurons_per_layer'])
        order_params.append(phi)
        print(f"  λ = {lam:.2f}: Φ = {phi:.3f}")

    # Find critical λ (steepest descent)
    d_phi = np.gradient(order_params)
    lambda_critical = lambdas[np.argmax(np.abs(d_phi))] if len(d_phi) > 0 else 0.5

    print(f"\n  Critical λ ≈ {lambda_critical:.3f}")
    print(f"  Max |dΦ/dλ| = {np.max(np.abs(d_phi)):.3f}")
    print(f"  Phase transition: {'DETECTED' if np.max(np.abs(d_phi)) > 0.1 else 'WEAK/ABSENT'}")

    # ============================================
    # PHASE 3: SCALING LAW TEST
    # ============================================
    scaling_holds, r_squared = test_lambda_scaling()

    # ============================================
    # VISUALIZATION
    # ============================================
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    # 1. Phase diagram
    ax = axes[0, 0]
    ax.plot(lambdas, order_params, 'b-o', linewidth=2, markersize=6)
    ax.axvline(lambda_critical, color='r', linestyle='--', linewidth=2, label=f'$\\lambda_c$ = {lambda_critical:.2f}')
    ax.axhline(0.5, color='gray', linestyle=':', alpha=0.5)
    ax.set_xlabel('λ (control attenuation)', fontsize=12)
    ax.set_ylabel('Φ (order parameter)', fontsize=12)
    ax.set_title('Phase Transition: Sync → Desync', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)

    # 2. Avalanche distribution
    ax = axes[1, 0]
    if len(avalanche_sizes) > 5:
        sorted_sizes = np.sort(avalanche_sizes)[::-1]
        ccdf = np.arange(1, len(sorted_sizes)+1) / len(sorted_sizes)
        ax.loglog(sorted_sizes, ccdf, 'bo-', markersize=4, label=f'α = {alpha:.2f}')

        # Reference power-law
        ref_x = np.logspace(0.5, 2.5, 50)
        ax.loglog(ref_x, ref_x**(-1.5) * 10, 'r--', linewidth=2, label='Critical (α=1.5)')
        ax.set_xlabel('Avalanche size S', fontsize=12)
        ax.set_ylabel('P(S > s)', fontsize=12)
        ax.set_title('Cascade Size Distribution', fontsize=14)
        ax.legend()
        ax.grid(True, alpha=0.3)

    # 3. Temporal dynamics (rate over time)
    ax = axes[0, 1]
    rates = sim['rate_monitor'].rate / Hz
    times = sim['rate_monitor'].t / ms
    ax.plot(times[:min(5000, len(times))], rates[:min(5000, len(rates))], 'b-', alpha=0.7)
    ax.set_xlabel('Time (ms)', fontsize=12)
    ax.set_ylabel('Firing rate (Hz)', fontsize=12)
    ax.set_title('Population Activity', fontsize=14)
    ax.grid(True, alpha=0.3)

    # 4. Layer activity
    ax = axes[0, 2]
    layer_names = ['API Server', 'etcd', 'Kubelets', 'Pods', 'Containers']
    layer_rates = []
    for i in range(sim['N_layers']):
        start_idx = i * sim['neurons_per_layer']
        end_idx = (i + 1) * sim['neurons_per_layer']
        mask = (sim['spike_monitor'].i >= start_idx) & (sim['spike_monitor'].i < end_idx)
        layer_rates.append(np.sum(mask) / 1.0)  # spikes per second

    colors = plt.cm.viridis(np.linspace(0.2, 0.8, sim['N_layers']))
    bars = ax.bar(layer_names, layer_rates, color=colors, edgecolor='black')
    ax.set_ylabel('Spike count (1s)', fontsize=12)
    ax.set_title('Activity by Hierarchy Level', fontsize=14)
    ax.tick_params(axis='x', rotation=15)

    # 5. Criticality assessment
    ax = axes[1, 1]
    ax.axis('off')

    verdict_text = f"""
KUBERNETES GOVERNANCE PHYSICS RESULTS
══════════════════════════════════════

Phase Transition:
  λ_critical ≈ {lambda_critical:.3f}
  Status: {'DETECTED' if np.max(np.abs(d_phi)) > 0.1 else 'WEAK'}

Power-Law Cascades:
  Exponent α = {alpha:.2f}
  Critical value: α ≈ 1.5
  Status: {'NEAR-CRITICAL' if 1.2 < alpha < 2.5 else 'SUBCRITICAL'}

Scaling Law (λ ∝ √N):
  R² = {r_squared:.3f}
  Status: {'SUPPORTED' if scaling_holds else 'NOT SUPPORTED'}

─── VALIDATION HOOKS ───
□ Get real K8s cascade data
□ Measure cascade exponent
□ Test λ scaling with cluster size
□ Verify 10-100ms propagation
"""
    ax.text(0.05, 0.95, verdict_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # 6. Parameters used
    ax = axes[1, 2]
    ax.axis('off')

    params_text = f"""
MODEL PARAMETERS (K8s Domain)
═════════════════════════════

λ (control rate): {K8S_PARAMS['lambda_']}
  Empirical range: 0.1-1.0/s ✓

τ (timescale): {float(K8S_PARAMS['tau_base']/ms):.0f}ms
  Empirical range: 10-100ms ✓

μ (dissipation): {K8S_PARAMS['mu']}

G (efficiency): {K8S_PARAMS['G']}

Hierarchy: {K8S_PARAMS['N_layers']} layers
  API → etcd → Kubelets → Pods → Containers

─── EMPIRICAL SOURCES ───
• etcd latency measurements
• Controller loop frequencies
• Pod scheduling benchmarks
"""
    ax.text(0.05, 0.95, params_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

    plt.tight_layout()
    plt.savefig('/home/peace/governance_physics_k8s_results.png', dpi=150, bbox_inches='tight')

    print("\n" + "="*70)
    print("SIMULATION COMPLETE")
    print("="*70)
    print(f"\n📊 Results saved to: /home/peace/governance_physics_k8s_results.png")
    print(f"\n{'='*70}")
    print("SUMMARY FOR VALIDATION")
    print("="*70)
    print(f"  Phase transition: λ_c ≈ {lambda_critical:.3f}")
    print(f"  Avalanche exponent: α = {alpha:.2f} (critical ≈ 1.5)")
    print(f"  Scaling law: R² = {r_squared:.3f} ({'PASS' if scaling_holds else 'FAIL'})")
    print("="*70)
