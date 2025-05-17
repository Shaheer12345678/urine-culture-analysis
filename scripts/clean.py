import sys, pandas as pd
src, dst = sys.argv[1], sys.argv[2]
df = pd.read_csv(src, parse_dates=['order_time'])
