'''
Creadores:
La flor
El inge
El samy
El García²
El Aleks
Alfonso Gamboa Rubén

La ventana de inicio aunque suene irónico, es la ventana main, que es la que se va a ejecutar, por lo ésta organiza y llama al resto

'''

import tkinter as Tk
from customtkinter import CTk, CTkFrame, CTkEntry, CTkButton, CTkLabel


#Importar módulos propios:
import creacion_usuarios
import funciones_botones as f
import principal
from config import * # variables reservadas: c1, c2, c3, c4, c5, c_blanco, c_negro, fuente, t_fuente.


# Ventana principal
class V_inicio(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Popiedades de la ventana
        self.geometry("500x200")  # Geometría (Aun puede ser cambiada)
        # self.minsize(320, 540) # tamaño mínimo para que no pasen cosas extrañas ;)
        self.config(bg = c1) # Un color de fondo
        self.title("Life Rhythm")

        ## configuración de filas y columnas para toda la ventana principal, permitiendonos centrar el contenido sin importar el tamaño de la ventana
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.ventana_abierta = None # Variable que nos ayudadrá a saber si ya hay abierta una ventana nueva


        # marcos
        ## marco 1: ingreso de usuario
        self.marco1 = CTkFrame(self, fg_color=c1, bg_color=c1) #le ponemos el mismo color que el de fondo de pantalla
        self.marco1.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)
        ### configuración de columnas y ventanas del marco
        self.marco1.columnconfigure([0, 1], weight=1)
        self.marco1.rowconfigure([0,1,2,3,4,5], weight=1) 
        ## marco 2: marco de la ventana principal
        self.marco2 = principal.V_principal(master=self) 
        

        

        # Widgets marco 1
        ## Etiqueta usuario
        self.l_usuario = CustomLabel(self.marco1, text="Usuario:")
        self.l_usuario.grid(column=0, row=1, padx=4, pady=4)

        ## Entrada de usuario
        self.e_usuario = CustomEntry(self.marco1, placeholder_text="Ingresar usuario")
        self.e_usuario.grid(column=1, row=1, padx=4, pady=4) # Se va a colocar en la primera fila

        ## Boton crear usuario
        self.b_crear_usuario = CustomButton(self.marco1, text="Nuevo usuario", command=lambda: f.abrir_ventana(self, creacion_usuarios.V_nuevo_usuario))
        self.b_crear_usuario.grid(column=0, row=2, padx=4, pady=4)

        ## Boton para entrar
        self.b_entrar = CustomButton(self.marco1, text="Entrar", command=lambda: self.mostrar_frame(frame=self.marco2))
        self.b_entrar.grid(column=1, row=2, padx=4, pady=4)

        ## Botón para cerrar
        self.b_cerrar = CustomButton(self.marco1, text="Salir de la aplicación", command= lambda: f.cerrar_ventana(self))
        self.b_cerrar.grid(columnspan=2, row=3, padx=4, pady=4) 

    # Funciones propias de "inicio.py"
    def mostrar_frame(frame):
        frame.place(relwidth=1, relheight=1)
        frame.tkraise()

# Main

if __name__ == "__main__":
    inicio = V_inicio()
    inicio.mainloop()

