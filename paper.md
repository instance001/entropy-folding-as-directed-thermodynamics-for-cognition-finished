# Entropy Folding as Directed Thermodynamics for Cognition

## Risky Phrases
- “thermodynamically lawful mechanism” → reads as a physics claim; replace with “thermodynamically compatible under open-system assumptions.”
- “insight is free” → implies no cost; replace with “insight appears low-effort because cost is prepaid during folding.”
- “central mechanism that transforms” → overstates exclusivity; replace with “a proposed mechanism that links vaulting to capacity gain.”

## Abstract
Entropy Folding is a proposed process in which unresolved items (vaulted entropy, `E_v`) are reorganized (folding, `F`) to increase structural capacity (`M`) and make downstream resolutions (insights, `I`) require less effort. This paper restates the cycle in falsifiable, implementation-ready terms and positions it as thermodynamically compatible under open-system assumptions rather than as a physical law. Each variable is operationalized: `E_v` as logged unresolved tasks, `F` as measurable reorganization steps, `ΔM` as capacity proxies (time-to-solve change, error-rate change, plan compression, backtracking reduction, transfer performance), `I` as abrupt performance gains, and `P` as observable outputs. Three null models are specified (Poisson bursts, random-walk skill change, cumulative practice) to bound claims. A minimal empirical predictions section describes how the cycle could fail. The goal is a reproducible research program and a GitHub-friendly reference scaffold, not a claim of guaranteed improvement or thermodynamic novelty. (188 words)

## 1. Motivation and Thesis
Current LLM practice often treats stalled work as discardable; Entropy Folding treats stalls as fuel that, when reorganized, can raise capacity and make later resolutions easier. **Thesis:** If vaulted items are systematically folded and capacity change is tracked with explicit proxies, performance bursts should exceed null models that lack folding.

## 2. Measurable Definitions
- `E_v` (vaulted entropy): count and description of unresolved tasks/problems logged with constraints and failed attempts.
- `F` (folding): observed reorganization actions (clustering, constraint rewrites, ordering changes); countable operations per cycle.
- `M` / `ΔM` (capacity): estimated via proxies listed in §4; record baseline and post-fold values.
- `I` (insight): discrete performance jumps (e.g., sudden drop in time-to-solve or error) temporally following a fold.
- `P` (projects): concrete outputs created post-insight; counted and timestamped; feed the next `E_v`.

## 3. Folding Cycle (concise)
1) Vault items; 2) detect stall; 3) fold (reorganize); 4) update capacity estimate; 5) observe insights; 6) record projects; 7) refresh vault.

## 4. Operationalization (proxies, not ground truth)
- Δ time-to-solve on matched problems before/after fold.
- Δ error rate on matched problems.
- Plan compression: average steps per plan before/after fold.
- Reduction in backtracking steps during problem solving.
- Transfer gain: performance change on an adjacent task class.

## 5. Comparison Null Models
- Poisson burst model (events occur with constant rate, no fold influence).
- Random-walk skill change (capacity drifts without structured folding).
- Simple cumulative practice (monotonic improvement proportional to time on task).

## 6. Empirical Predictions
1) **Burst shift beyond Poisson:** If folding matters, burst timing/magnitude deviates from Poisson expectations; falsified if burst stats match Poisson under folding vs non-folding conditions.  
2) **Proxy improvement vs random-walk:** Capacity proxies should improve more after fold cycles than in matched random-walk simulations; falsified if improvements fall within random-walk confidence intervals.  
3) **Transfer bump over practice-only:** Adjacent-task transfer should exceed simple practice baselines after folding; falsified if transfer gains equal cumulative practice with no fold.

## 7. Limitations & Non-Claims
- Not a claim of new physics; only compatibility with open-system thermodynamics.
- Proxies may misestimate true capacity; they are convenience measures.
- Insights can occur without folding; cycle is not exclusive.
- No claim of prediction or control of individuals or groups.
- No claim that insights are cost-free; costs are logged in folding effort.
- Results depend on task design; weak tasks may mask effects.
- Folding procedures may introduce bias; audits are required.
- Null models may be misspecified; must be reported alongside results.

## License
This preprint and associated code are released under AGPLv3 (see LICENSE).
