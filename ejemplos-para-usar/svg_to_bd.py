# Leer un svg y transformarlo a base de datos

import sqlite3
import pandas as pd

df = pd.read_csv("Iris.csv")
#print(df)
conn = sqlite3.connect("iris_example.db")

# Convert DataFrame to SQL
df.to_sql("iris_table_name", conn, if_exists="replace", index=False)