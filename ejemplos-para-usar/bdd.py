# Base convertir un data frame a una base de datos
# Vamos a hacer nuestro propio data frame

import pandas as pd

# my_data = pd.read_csv("my_input_file.csv") # es recomendable guardar en csv para que sea más fácil leer
columns = ['a', 'b'] #Nombramos nuestras tablas
my_data = pd.DataFrame([[1, 2], [3, 4]], columns=columns)

## conect to database
import sqlite3

conn = sqlite3.connect("pythonsqulite.db")

##psh the dataframe to sql
my_data.to_sql("my_data", conn, if_exists="replace")

##create the table

conn.execute(
    """
    Create table my_table as
    select * from my_data
    """
)