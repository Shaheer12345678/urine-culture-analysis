import sys, pandas as pd, matplotlib.pyplot as plt, numpy as np, pathlib
src, report, plot = sys.argv[1], sys.argv[2], sys.argv[3]
df = pd.read_csv(src, parse_dates=['order_time'])
total = len(df)
pos_rate = (df['uc_result'] == 'pos').mean() if total else 0.0
by_loc = df.groupby('location').size().to_dict()

pathlib.Path(report).parent.mkdir(parents=True, exist_ok=True)
with open(report, "w") as f:
    f.write(f"Total orders analyzed: {total}\n")
    f.write(f"Positive rate: {pos_rate:.2%}\n")
    f.write("Orders by location:\n")
    for k,v in by_loc.items():
        f.write(f"  - {k}: {v}\n")
print(f"[analyze] Wrote report -> {report}")

plt.figure()
df['order_time'].dt.date.value_counts().sort_index().plot(kind='bar')
plt.title("Orders per day")
plt.tight_layout()
plt.savefig(plot)
