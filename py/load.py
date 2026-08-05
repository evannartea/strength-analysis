import time
import pandas as pd
from config import engine

start = time.time()
df = pd.read_csv("data/raw/openpowerlifting-2026-08-01-55149139.csv")
df.to_sql(
    name="openpowerlifting_20260801",
    con=engine,
    schema="raw",
    if_exists="replace",
    index=False,
    chunksize=10000,
    method="multi"
)

print(f"Loaded successfully!\nTime elapsed:{time.time() - start:1f}s")