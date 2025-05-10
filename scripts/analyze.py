import sys, pandas as pd, matplotlib.pyplot as plt, numpy as np, pathlib
src, report, plot = sys.argv[1], sys.argv[2], sys.argv[3]
df = pd.read_csv(src, parse_dates=['order_time'])
total = len(df)
