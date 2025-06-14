import sys, pandas as pd
src, dst = sys.argv[1], sys.argv[2]
df = pd.read_csv(src, parse_dates=['order_time'])
# Remove "screen" indications as likely inappropriate
df['is_screen'] = df['indication'].str.contains("screen", case=False, na=False)
df_clean = df[~df['is_screen']].copy()
df_clean.to_csv(dst, index=False)
print(f"[clean] rows_in={len(df)} rows_out={len(df_clean)} -> {dst}")

