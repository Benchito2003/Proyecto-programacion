# Importamos al papá de todas nuestras librerías
import customtkinter
import random # Para poder tener unos numeros aleatorios en el usuario
import os

#Importar módulos propios:
import funciones_botones as f
import funciones_dataframes as f_df
from config import * # variables reservadas: c1, c2, c3, c4, c5, c_blanco, c_negro, fuente, t_fuente.

# Clase para agregar los datos el usuario
class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.codigo = None
        self.nombre_fichero = "usuarios.csv"
    
    def gen_codigo(self):
        num_aleatorio = random.randint(1, 100)
        letras_nombre = self.nombre[:2].upper() #las dos primeras letras y siempre en mayusculas
        letras_apellido = self.apellido[:2].upper() # Las dos primeras letras y siempre en mayusculas
        edad = int(self.edad)
        codigo = f"{letras_nombre}{letras_apellido}{edad:02d}{num_aleatorio}" # con :02d damos formato el numero
        # print(codigo)
        # Guardamos el código como una propiedad de la clase
        self.codigo = codigo
        return codigo
    
    def guardar(self):
        # Nos aseguramos que exista un código de usuario antes de guardarlo
        if self.codigo != None:
            columnas = ["Codigo", "Nombre", "Apellido", "Edad" ]
            datos = [[self.codigo, self.nombre, self.apellido, self.edad]]
            if os.path.exists(self.nombre_fichero): # si existe el fichero:
                # guardamos lo del archivo en un dataframe temporal
                df_leido = f_df.leer_desde_archivo(self.nombre_fichero)
                # Actualizamos la dataframe 
                df = f_df.guardar_datos(datos, columnas, df_leido)
            else:
                # Creamos un dataframe completamente nuevo de fábrica
                df = f_df.guardar_datos(datos, columnas)

            # Lo guardamos en el fichero
            f_df.guardar_en_archivo(df, self.nombre_fichero)



# Clase de la ventana nueva
class VCrearUsuario(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configuracion de la ventana
        self.geometry("400x300")
        self.title("Crear usuario nuevo")
        self.config(bg=c1)
        ## Configuraciones del grid
        self.columnconfigure([0, 1, 2], weight=1)
        self.rowconfigure([0,1,2,3,4,5], weight=1) 

        ## En este caso el usuario es un elemento de la ventana
        self.usuario_generado = None
        self.datos_nuevos = None

        # Widgets de la ventana de la creación de usuario
        ## Etiqueta nombre
        self.l_nombre = CustomLabel(self, text="Nombre:")
        self.l_nombre.grid(row=0, column=0, padx=4, pady=4)
        ## Entrada nombre
        self.e_nombre = CustomEntry(self, placeholder_text="'Panchito'")
        self.e_nombre.grid(row=0, column=1, padx=4, pady=4)

        ## Etiqueta apellido
        self.l_apellido = CustomLabel(self, text="Apellido:")
        self.l_apellido.grid(row=1, column=0, padx=4, pady=4)
        ## Entrada apellido
        self.e_apellido = CustomEntry(self, placeholder_text="'Perez'")
        self.e_apellido.grid(row=1, column=1, padx=4, pady=4)

        ## Etiqueta edad
        self.l_edad = CustomLabel(self, text="Edad:")
        self.l_edad.grid(row=2, column=0, padx=4, pady=4)
        ## Entrada edad
        self.e_edad = CustomEntry(self, placeholder_text="Solo enteros")
        self.e_edad.grid(row=2, column=1, padx=4, pady=4)

        ## Botón para generar el usuario
        self.b_gen_usuario = CustomButton(self, text="Generar usuario", command=self.generar_usuario)
        self.b_gen_usuario.grid(row=3, columnspan=2, padx=4, pady=4)

        ## Etiqueta Usuario
        self.l_usuario = CustomLabel(self, text="Tu usuario es:")
        ## Etiqueta del usuario generado
        self.l_usuario_generado = CustomLabel(self, text="Usuario generado automaticamente")

        ## Botón para continuar
        self.b_continuar = CustomButton(self, text="cerrar", command=lambda: f.cerrar_ventana(self))
        self.b_continuar.grid(row=5, column=1, padx=10, pady=10)
    
    # Funciones propias de la ventana:
    def borrar_campos(self):
        f.borrar_texto(self.e_nombre)
        f.borrar_texto(self.e_apellido)
        f.borrar_texto(self.e_edad)
    
    def obtener_campos(self):
        """ Obtenemos los campos y los guardamos como una propiedad de la clase """
        nombre = f.obtener_texto(self.e_nombre)
        apellido = f.obtener_texto(self.e_apellido)
        edad = f.obtener_texto(self.e_edad)

        # Creamos un objeto de usuario y lo guardamos dentro de las propiedades de la clase
        self.usuario_generado = Usuario(nombre, apellido, edad) 

    def generar_usuario(self): 
        """ Proceso para crear un usuario: """
        # paso 1: obtenemos los datos y verificamos que no hayan errores
        try:
            self.obtener_campos()
            # paso 2: Generamos un nuevo usuario con una función de la clase
            codigo = self.usuario_generado.gen_codigo()
            # paso 3: ocultamos el botón de generar usuario
            self.b_gen_usuario.grid_forget()
            # Paso 4: Modificamos la etiqueta para que enseñe el usuario generado
            self.l_usuario_generado.configure(text=f"Su codigo de usuario es: {codigo}")
            # paso 5: enseñamos la etiqueta con el usuario generado
            self.l_usuario.grid(row=4, column=0, padx=4, pady=4)
            self.l_usuario_generado.grid(row=4, column=1, padx=4, pady=4)
            # paso 6: borramos evidencia la evidencia del crimen >;) 
            self.borrar_campos()
            # Paso 7: guardamos los datos en la dataframe
            self.usuario_generado.guardar()
            
        except:
            # Mensaje de error si ingresan datos inválidos
            self.b_gen_usuario.grid_forget()
            self.l_usuario_generado.configure(text=f"Los datos ingresados no son válidos, cierre e intente de nuevo.")
            self.l_usuario.grid(row=4, column=0, padx=4, pady=4)
            self.l_usuario_generado.grid(row=4, column=1, padx=4, pady=4)
            self.borrar_campos()



if __name__ == "__main__":
    # Ejemplo de introducir la ventana nueva dentro de la ventana, esto no es necesario modificar solo es para poder llamar a la ventana para poder desarrollar mas fácil
    class App(customtkinter.CTk):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("500x400")
    
            self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command=self.open_toplevel)
            self.button_1.pack(side="top", padx=20, pady=20)
    
            self.boton_cerrar = CustomButton(self, text="cerrar ventana", command=lambda: f.cerrar_ventana(self))
            self.boton_cerrar.pack(side="bottom", padx=20, pady=20)
    
            self.toplevel_window = None
    
        def open_toplevel(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = VCrearUsuario(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it
        app = App()
        app.mainloop()

""" 
Código inspirado de:
https://customtkinter.tomschimansky.com/documentation/windows/toplevels
"""