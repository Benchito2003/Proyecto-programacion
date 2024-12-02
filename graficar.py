import matplotlib.pyplot as plt

def graficar_datos(x, y, titulo="Gráfico de Datos", x_etiqueta="Eje X", y_etiqueta="Eje Y"):
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', marker='o')
    plt.title(titulo)
    plt.xlabel(x_etiqueta)
    plt.ylabel(y_etiqueta)
    plt.grid(True)
    plt.show()