import sys, pandas as pd, matplotlib.pyplot as plt, numpy as np, pathlib
src, report, plot = sys.argv[1], sys.argv[2], sys.argv[3]
df = pd.read_csv(src, parse_dates=['order_time'])
total = len(df)
pos_rate = (df['uc_result'] == 'pos').mean() if total else 0.0
by_loc = df.groupby('location').size().to_dict()

