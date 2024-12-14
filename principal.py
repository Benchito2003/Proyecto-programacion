""" 
Frame principal: Este es el frame donde se crean nuevos registros, se ven los registros previos y
donde se puede hacer la prueba de esfuerzo
Documentación: https://customtkinter.tomschimansky.com/documentation/widgets/frames
"""
# Importamos librerías
## Librerías de python
import customtkinter
## Módulos propios
### Configuración general:
from config import * # variables reservadas: c1, c2, c3, c4, c5, c_blanco, c_negro, fuente, t_fuente.
### Funciones generales de los botones
import funciones_botones as f
### Funciones para las fataframes
import funciones_dataframes as f_df
### ventanas que van a surgir de esta clase
import ver_registros
import nuevo_registro

# Marco del programa principal
class FrPrincipal(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=c1, bg_color=c1, **kwargs)

        # Configuraciones grid del marco
        self.columnconfigure([0, 1, 2], weight=1)
        self.rowconfigure([0,1,2,3,4,5], weight=1)

        self.codigo = None
        self.nombre_usuario = None

        # Widgets del Frame principal
        ## Etiqueta menu principal
        self.titulo = CustomLabel(self, text=f"¿Qué deseas hacer, {self.nombre_usuario}?")
        self.titulo.grid(row=0, columnspan=3, padx=20)
        ## Botón de nuevo registro
        self.b_nuevo = CustomButton(self, text="Registrar frecuencia cardiaca", command = lambda: f.abrir_ventana(master, nuevo_registro.VNuevoRegistro))
        self.b_nuevo.grid(row=1, column=0, padx=4, pady=4)
        ## Botón para prueba de esfuerzo
        self.b_prueba = CustomButton(self, text="Medir HRR")
        self.b_prueba.grid(row=1, column=1, padx=4, pady=4)
        ## Botón para ver registros
        self.b_ver = CustomButton(self, text="Ver registros", command= self.ventana_registros)
        self.b_ver.grid(row=1, column=2, padx=4,pady=4)
        ## Botón para salir
        self.b_salida = CustomButton(self, text="Salir de la aplicación", command=lambda: f.cerrar_ventana(master))
        self.b_salida.grid(row=4, column=2, padx=4, pady=4)

    # Funciones propias del marco
    def get_usuario(self, archivo, codigo):
        """ Función para traer el nombre de usuario según el código recibido """
        if f_df.verificar_archivo(archivo):
            dataframe = f_df.leer_desde_archivo(archivo)
            nombre = f_df.get_datos_usuario(dataframe, codigo, "Nombre")
            return nombre
        else:
            print("Archivo no encontrado")

    def actualizar_codigo(self, codigo):
        """ permite observar si ha cambiado el codigo de usuarios """
        archivo = "usuarios.csv"
        self.codigo = codigo
        self.nombre_usuario = self.get_usuario(archivo,codigo)
        self.titulo.configure(text=f"¿Qué deseas hacer {self.nombre_usuario}?")

    def ventana_registros(self):
        """ Función especial para abrir los registros """
        f.abrir_ventana(self.master, ver_registros.VverRegistros)
        # Actualizamos el codigo de la ventana de los registros
        self.master.ventana_abierta.actualizar_datos(self.codigo, self.nombre_usuario)




# Aqui podemos probar que el marco funcione correctamente y sin errores:
if __name__ == "__main__":
    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("400x200")
            self.grid_rowconfigure(0, weight=1)  # configure grid system
            self.grid_columnconfigure(0, weight=1)

            self.ventana_abierta = None

            self.my_frame = FrPrincipal(master=self)
            self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    app = App()
    app.mainloop()