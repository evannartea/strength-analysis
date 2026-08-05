import pandas as pd
from config import engine

def export_to_csv(table_name, engine):
    df = pd.read_sql(f"SELECT * FROM staging.{table_name}", engine)

    file_path = f"data/clean/{table_name}.csv"
    df.to_csv(file_path, index=False)

    return file_path

export_to_csv("openpowerlifting_20260801", engine)

print("Exported successfully!")