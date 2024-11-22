# Importamos al papá de todas nuestras librerías
import customtkinter

#Importar módulos propios:
import funciones_botones as f
from config import *

# Clase de la ventana nueva
class V_nuevo_usuario(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Configuracion de la ventana
        self.geometry("400x300")
        self.title("Crear usuario nuevo")
        self.config(bg=c1)
        # Configuraciones del grid
        self.columnconfigure([0, 1, 2], weight=1)
        self.rowconfigure([0,1,2,3,4,5], weight=1) 

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
        self.e_edad = CustomEntry(self, placeholder_text="Ingresar edad")
        self.e_edad.grid(row=2, column=1, padx=4, pady=4)

        ## Botón para generar el usuario
        self.b_gen_usuario = CustomButton(self, text="Generar usuario")
        self.b_gen_usuario.grid(row=3, columnspan=2, padx=4, pady=4)

        ## Etiqueta Usuario
        self.l_usuario = CustomLabel(self, text="Tu usuario es:")
        self.l_usuario.grid(row=4, column=0, padx=4, pady=4)
        ## Etiqueta del usuario generado
        self.l_usuario_generado = CustomLabel(self, text="Usuario generado automaticamente")
        self.l_usuario_generado.grid(row=4, column=1, padx=4, pady=4)

        ## Botoón para continuar
        self.b_continuar = CustomButton(self, text="Continuar", command=lambda: f.cerrar_ventana(self))
        self.b_continuar.grid(row=5, column=1, padx=10, pady=10)

# Ejemplo de introducir la ventana nueva dentro de la ventana, esto no es necesario modificar solo es para poder llamar a la ventana para poder desarrollar mas fácil
class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")

        self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command=self.open_toplevel)
        self.button_1.pack(side="top", padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = V_nuevo_usuario(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

if __name__ == "__main__":
    app = App()
    app.mainloop()

""" 
Código inspirado de:
https://customtkinter.tomschimansky.com/documentation/windows/toplevels
"""
