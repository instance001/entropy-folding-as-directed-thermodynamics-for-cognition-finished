# Contributing
License: AGPLv3 (see LICENSE).

## Setup
1. `python -m venv .venv`
2. `.\.venv\Scripts\activate`
3. `pip install -U pip -r requirements.txt`

## Tests
- `pytest` (pyproject sets `pythonpath=src`; no extra flags needed).

## Guardrails
- Do not introduce anthropomorphism or claims of sentience/feelings.
- Do not add deterministic forecasting, prediction of individuals, or control claims.
- Keep language open-system and proxy-based; report null models and uncertainty.
- Maintain AGPLv3 headers/comments where present.
