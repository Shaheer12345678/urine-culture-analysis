# Diagnostic Stewardship Data Analysis (Urine Culture Ordering)

Reproducible pipeline (Make + Python) to explore ordering patterns and simple reduction strategies.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make run
```

This will run `scripts/ingest.py`, `scripts/clean.py`, and `scripts/analyze.py` and write outputs to `outputs/`.


