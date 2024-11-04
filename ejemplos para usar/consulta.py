import sqlite3

conn = sqlite3.connect("sample.db")
cursor = conn.cursor()

select_distinct_query = "SELECT DISTINCT age FROM people"
for row in cursor.execute(select_distinct_query):
    print(row)