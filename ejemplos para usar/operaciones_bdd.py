# operaciones con bases de datos
import sqlite3

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect("sample.db")
cursor = conn.cursor()

# Create new table
create_table_query = "query"

cursor.execute(create_table_query)
# Insert sample data
sample_data = [("Jhon Doe", 30), ("Jane Doe", 25), ("Jim Beam", 30)]
for person in sample_data:
    cursor.execute("Insert INTO people(name, age) VALUES (?,?)", person)

conn.commit()