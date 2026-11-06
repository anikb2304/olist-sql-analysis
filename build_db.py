import sqlite3
from pathlib import Path
import pandas as pd

data_dir = Path("data")
conn = sqlite3.connect("olist.db")

for csv in sorted(data_dir.glob("*.csv")):
    table = csv.stem.replace("_dataset", "").replace("olist_", "")
    df = pd.read_csv(csv)
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"{table}: {len(df)} rows")

conn.close()