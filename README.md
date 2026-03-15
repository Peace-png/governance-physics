<p align="center">
  <img src="header_image.png" alt="Governance Physics" width="100%">
</p>

# Governance Physics: Phase Transitions and Cascade Dynamics in Kubernetes Clusters

> A spiking neural network simulation investigating whether organizational structures follow universal scaling laws similar to phase transitions in statistical physics.

## Abstract

We model Kubernetes cluster governance as a hierarchical spiking neural network to test three predictions from "Governance Physics" theory:

1. **Phase transitions exist** — Systems transition from synchronized (stable) to desynchronized (unstable) as control attenuation (λ) increases
2. **Critical avalanche dynamics** — Failure cascades follow power-law distributions with exponent α ≈ 1.5
3. **Universal scaling** — Control rate λ scales with √(system size)

**Results:** We find evidence for critical avalanche dynamics (α = 1.88, near theoretical 1.5) but no clear phase transition and the √N scaling law is rejected.

---

## Methodology

### Model Architecture

We represent a Kubernetes cluster as a 5-layer hierarchy:

```
Layer 0: API Server / Controller Manager (Executive)
Layer 1: Scheduler / etcd (Coordination)
Layer 2: Kubelets (Node Agents)
Layer 3: Pods (Workload Units)
Layer 4: Containers (Labor)
```

Each layer is modeled as a population of Leaky Integrate-and-Fire (LIF) neurons with:

- **Downward synapses**: Control signals with exponential weight decay `w = 0.5 * exp(-λ * depth)`
- **Upward synapses**: Failure feedback with decay `w = 0.3 * exp(-μ * depth_from_bottom)`

### Parameters (K8s Domain)

| Parameter | Value | Empirical Range | Source |
|-----------|-------|-----------------|--------|
| λ (control rate) | 0.8/s | 0.1-1.0/s | Controller loop frequencies |
| τ (timescale) | 20ms | 10-100ms | etcd consensus latency |
| μ (dissipation) | 1.5 | — | Tuned parameter |
| G (efficiency) | 0.4 | 0.2-0.8 | Span-of-control estimates |

### Measurements

1. **Order Parameter (Φ)** — Kuramoto-style synchronization measure across time windows
2. **Avalanche Distribution** — Cascade sizes during high-activity periods
3. **Power-law Exponent (α)** — Maximum likelihood estimation for avalanche sizes

---

## Results

### 1. Phase Transition

| Metric | Value |
|--------|-------|
| Critical λ | ~1.36 |
| Max \|dΦ/dλ\| | 0.034 |
| Verdict | **WEAK/ABSENT** |

The order parameter Φ remained roughly constant (0.26-0.35) across the λ sweep. No sharp transition was detected.

### 2. Avalanche Dynamics

| Metric | Value | Critical Value |
|--------|-------|----------------|
| Power-law exponent α | 1.88 | ~1.5 |
| Avalanches detected | 224 | — |
| Verdict | **NEAR-CRITICAL** | ✅ |

The cascade size distribution follows a power-law with exponent close to the critical value, suggesting the model captures realistic failure propagation dynamics.

### 3. Scaling Law (λ ∝ √N)

| Metric | Value |
|--------|-------|
| R² for √N fit | 0.025 |
| Verdict | **REJECTED** |

The predicted scaling relationship between control rate and system size does not emerge from the model.

---

## Validation Hooks

This simulation makes testable predictions. Real empirical data would falsify the model if:

| Prediction | Falsified If |
|------------|--------------|
| Cascade power-law | Real K8s cascades don't follow power-law distribution |
| Exponent α ≈ 1.5-2.0 | Real cascade exponent is significantly different |
| Timescale 10-100ms | Real failure propagation is orders of magnitude different |
| No phase transition | Real clusters DO show sharp stability transitions |

**Data sources needed for validation:**
- Public K8s failure cascade logs
- Cascade size distributions from production clusters
- Propagation time measurements through microservice dependency graphs

---

## Files

| File | Description |
|------|-------------|
| [`governance_physics_k8s.py`](governance_physics_k8s.py) | K8s-focused simulation code |
| [`governance_physics_snn.py`](governance_physics_snn.py) | Multi-domain simulation (K8s, Fed, Corp) |
| [`docs/GOVERNANCE_PHYSICS_RESEARCH_REPORT.md`](docs/GOVERNANCE_PHYSICS_RESEARCH_REPORT.md) | Full research report with literature review |
| [`governance_physics_k8s_results.png`](governance_physics_k8s_results.png) | K8s visualization output |
| [`governance_physics_snn_results.png`](governance_physics_snn_results.png) | Multi-domain visualization |

---

## Running the Simulation

```bash
# Activate environment with Brian2
conda activate conscious_snn

# Run K8s simulation
python governance_physics_k8s.py

# Run multi-domain simulation
python governance_physics_snn.py
```

**Requirements:**
- Python 3.11+
- Brian2 2.8.0+
- NumPy, Matplotlib

---

## Sources & Citations

### Theoretical Foundations
- Prigogine, I. (1977). Nobel Lecture: Time, Structure and Fluctuations
- Nicolis, G. & Prigogine, I. (1977). Self-Organization in Non-Equilibrium Systems

### Monetary Policy Transmission (Federal Reserve Domain)
- Christiano, L.J., Eichenbaum, M. & Evans, C.L. (1999). "Monetary Policy Shocks: What Have We Learned and to What End?" Handbook of Macroeconomics
- Romer, C.D. & Romer, D.H. (2004). "A New Measure of Monetary Shocks." AER
- Gertler, M. & Karadi, P. (2015). "Monetary Policy Surprises, Credit Costs, and Economic Activity." AER

### Cascade Failures in Networks
- arXiv:2204.08407 — "Non-Markovian random walks characterize network robustness"
- arXiv:2112.11308 — "Cascading failures in isotropic and anisotropic spatial networks"
- arXiv:2010.01373 — "Abrupt transition due to non-local cascade propagation"

### Kubernetes Empirical Data
- Google Cluster Data (Borg traces): github.com/google/cluster-data
- etcd performance benchmarks: etcd.io/docs/v3.5/benchmarks/
- K8s scalability docs: kubernetes.io/docs/setup/best-practices/cluster-large/

---

## Limitations

1. **No empirical validation** — Parameters are estimated, not fitted from real data
2. **Simplified topology** — Real K8s networks have more complex dependency structures
3. **Single domain tested** — Only K8s has plausible timescales for this model
4. **No temporal evolution** — Model doesn't capture learning/adaptation

---

## Author

**Peace** — Research direction, empirical validation, methodology, analysis

---

## License

MIT

---

## Citation

```bibtex
@misc{governance_physics_2026,
  title={Governance Physics: Phase Transitions and Cascade Dynamics in Kubernetes Clusters},
  author={Peace},
  year={2026},
  url={https://github.com/Peace-png/governance-physics}
}
```
