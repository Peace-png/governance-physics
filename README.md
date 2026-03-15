# Governance Physics Simulation

Simulating governance structures (Kubernetes clusters, organizations) as spiking neural networks to study phase transitions, cascade failures, and critical dynamics.

## What is this?

Imagine a Kubernetes cluster like a company with hierarchy levels. When failures happen, they can cascade like dominoes. This project models that using brain-like neural networks to predict when systems become unstable.

## Files

| File | Description |
|------|-------------|
| `governance_physics_k8s.py` | K8s-focused simulation |
| `governance_physics_snn.py` | Multi-domain simulation (K8s, Fed, Corp) |
| `docs/GOVERNANCE_PHYSICS_RESEARCH_REPORT.md` | Full research with sources |

## Results

| Test | Result |
|------|--------|
| Avalanche dynamics (power-law) | ✅ Near-critical (α ≈ 1.88) |
| Phase transition | ❌ Weak/absent |
| λ ∝ √N scaling | ❌ Rejected |

## Running

```bash
conda activate conscious_snn
python governance_physics_k8s.py
```

## Sources & Citations

See `docs/GOVERNANCE_PHYSICS_RESEARCH_REPORT.md` for full bibliography including:
- Christiano, Eichenbaum & Evans (1999) - Monetary policy transmission
- Romer & Romer (2004) - Fed shock identification
- Gertler & Karadi (2015) - High-frequency policy identification
- Various arXiv papers on cascade failures in networks

## Contributors

- **Peace** - Research direction, empirical validation probe, "don't hold back" methodology
- **Claude (Atlas)** - Simulation implementation, research synthesis, literature review
