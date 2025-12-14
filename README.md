# Entropy Folding as Directed Thermodynamics for Cognition
License: AGPLv3 (see LICENSE)

[![CI](https://github.com/instance001/entropy-folding-as-directed-thermodynamics-for-cognition-finished/actions/workflows/ci.yml/badge.svg)](https://github.com/instance001/entropy-folding-as-directed-thermodynamics-for-cognition-finished/actions/workflows/ci.yml)
License: AGPLv3 (see LICENSE)

## What this repo is
- Paper draft (`paper.md`) on fold-aware capacity estimation under open-system thermodynamic compatibility.
- Minimal code stubs (`src/efe.py`, `src/metrics.py`) to structure vault→fold→capacity→insight cycles.
- Test placeholders (`tests/`) to ensure the loop runs and stalls/bursts are detectable.
- Slots for data (`data/`) and notebooks (`notebooks/`) for A/B or null-model comparisons.
- Guidance on ΔM proxies (time-to-solve, error rate, plan compression, backtracking reduction, transfer).
- Null models to compare against (Poisson bursts, random-walk skill change, cumulative practice).
- Proxy selection checklist: task-matched pairs, fixed pre/post windows, note floor/ceiling effects, report proxy choice alongside results.
- BibTeX entry for PhilPapers/GitHub.
- Link to shared disclaimer: see `../DISCLAIMER.md`.

## What this repo is not
- Not a claim of new physics or closed-system thermodynamics.
- Not a guarantee of performance gain.
- Not a predictor or controller of behavior.
- Not a sentience claim.
- Not a production implementation; code is skeletal.

## Quickstart
```bash
python -m venv .venv
./.venv/Scripts/activate
pip install -U pytest
pytest
```

## Citation
```
@article{paterson_entropy_folding_2025,
  title   = {Entropy Folding as Directed Thermodynamics for Cognition},
  author  = {Paterson, Anthony},
  year    = {2025},
  note    = {Preprint, Symbound entropy series},
  url     = {https://github.com/entropy-folding-as-directed-thermodynamics-for-cognition-finished}
}
```
