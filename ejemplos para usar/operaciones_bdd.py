# operaciones con bases de datos
# NOTA: Estas manipulaciones son con una base de datos que hizo la amestra, por lo que estos comandos no nos funcionarán con nuestra propia base de datos, pero la maestra con gusto nos puede brindar los querys específicos que necesitamos
import sqlite3

# Connect to SQLite database (or create if it doesn't exist)
conn = sqlite3.connect("sample.db")
cursor = conn.cursor()

# Create new table
create_table_query = "CREATE TABLE IF NOT EXISTS people(id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL);"

cursor.execute(create_table_query)
# Insert sample data
sample_data = [("Jhon Doe", 30), ("Jane Doe", 25), ("Jim Beam", 30)]
for person in sample_data:
    cursor.execute("Insert INTO people(name, age) VALUES (?,?)", person)

conn.commit()

# retribe unique records by removing duplicates from a dataset. 
# you can ise the DISTINCT

select_distinct_query = "SELECT DISTINCT age FROM people"
for row in cursor.execute(select_distinct_query):
    print(row)

count_distinct_query = "SELECT COUNT(DISTINCT age) FROM people"
cursor.execute(count_distinct_query)
result = cursor.fetchone()
print("Number of distinct ages: ", result[0])

group_by_query = "SELECT age, COUNT(DISTINCT name) FROM people GROUP BY age"
for row in cursor.execute(group_by_query):
    print(f"Age: {row[0]}, Distinct Names: {row[1]}")