import sys, pandas as pd, pathlib
src, dst = sys.argv[1], sys.argv[2]
df = pd.read_csv(src, parse_dates=['order_time'])
pathlib.Path(dst).parent.mkdir(parents=True, exist_ok=True)
df.to_csv(dst, index=False)
print(f"[ingest] rows={len(df)} -> {dst}")
