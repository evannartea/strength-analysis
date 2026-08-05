import os
import pandas as pd
import time
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)

start = time.time()
df = pd.read_csv("data/openpowerlifting-2026-08-01-55149139.csv")
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