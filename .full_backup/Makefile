run: ingest clean analyze

ingest:
\tpython scripts/ingest.py data/orders.csv outputs/ingested.csv

clean:
\tpython scripts/clean.py outputs/ingested.csv outputs/clean.csv
