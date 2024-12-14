# Librería de funciones para los dataframes
import pandas as pd
import os

## Archivos
def verificar_archivo(archivo):
    if os.path.exists(archivo):
        return True
    else:
        return False

def guardar_en_archivo(df, archivo, delimitador=','):
    """ Guarda el dataframe en un archivo de texto """
    df.to_csv(archivo, index=False, sep=delimitador)
    print(f"Datos guardados en {archivo}")

def leer_desde_archivo(archivo, delimitador=','):
    """ Lee un archivo y lo convierte en dataframe """
    return pd.read_csv(archivo, sep=delimitador)

## Usuarios
def guardar_datos(datos, columnas, df=None):
    """ Para guardar un usuario nuevo o crear un data frame y guardar los datos si no existe alguno"""
    # Comprobamos si no existe previamente un dataframe
    if df is None:
        df = pd.DataFrame(columns=columnas)
    
    # Crear un dataframe temporal con los datos nuevos
    nuevos_datos = pd.DataFrame(datos, columns=columnas)

    # Concatenar los datos nuevos al dataframe existente
    df = pd.concat([df, nuevos_datos], ignore_index=True)
    return df

def ver_usuarios():
    """ Para ver una lista con todos los usuarios guardados """

def get_datos_usuario(dataframe, codigo, columna="Nombre"):
    """ Trae los datos de un usuario en forma de lista según su código  """
    """ Datos que puede traer: Nombre, Apellido, Edad """
    # Leemos el archivo y lo convertimos en dataframe
    df = dataframe
    # Indicamos que utilice el código como índice
    df.set_index('Codigo', inplace=True)
    dato = df.loc[codigo, columna]
    return dato


## Registros


# Verificación
if __name__ == "__main__":
    # Ejemplo de uso
    columnas = ["Nombre", "Edad", "ciudad"]
    datos = [["Juan", 25, "Madrid"], ["Ana", 30, "Barcelona"]]

    df = guardar_datos(datos, columnas)

    # Ejemplo de añadir datos a un dataframe existente
    nuevos_datos = [["Luis", 22, "Valencia"]]
    df = guardar_datos(nuevos_datos, columnas, df)

    print(df)
    # ---
    # Ejemplo de guardar en un archivo de texto
    guardar_en_archivo(df, 'ejemplo.csv')

    # Ejemplo de leer desde archivo
    df_leido= leer_desde_archivo('ejemplo.csv')
    print("Datos leídos desde archivo:")
    print(df_leido)

    ## Ejemplo de traer un solo dato:
    # nombre = get_datos_usuario(df_leido, "Ana", "ciudad")
    print(f"nombre obtenido: {nombre}")
