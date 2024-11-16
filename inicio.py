'''
Creadores:
La flor
El inge
El samy
El García²
El Aleks
Alfonso Gamboa Rubén
'''

import tkinter as Tk
from customtkinter import CTk, CTkFrame, CTkEntry, CTkButton, CTkLabel


#Importar módulos propios:
import colores as col
import gestion_usuarios
import toma_datos

# Colores escogidos
paleta = col.paleta1
c1 = paleta[0] # Para el fondo
c2 = paleta[1] # Iconos 1
c3 = paleta[2] # Iconos 2
c4 = paleta[3] # para los marcos
c5 = paleta[4] # Para las letras
c_negro = "#000000" #Colores constantes
c_blanco = "FFFFFF" #Colores constantes

fuente = "sans rerif"

""" # comandos antes de convertir a clase nuestro programa
v_principal = CTk() # En este caso va a ser un objeto de custom tkinter (para colores y diseños chidos)
v_principal.geometry("960x540") # Geometría a libre albedrío
v_principal.minsize(320, 540) #tamaño mínimo para que no pasen cosas extrañas ;)
v_principal.config(bg = c1)

## configuración de filas y columnas para toda la ventana principal, permitiendonos centrar el contenido sin importar el tamaño de la ventana
v_principal.columnconfigure(0, weight=1)
v_principal.rowconfigure(0, weight=1) """

# Ventana principal
class V_principal(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Popiedades de la ventana
        self.geometry("400x200")  # Geometría a libre albedrío
        # self.minsize(320, 540) # tamaño mínimo para que no pasen cosas extrañas ;)
        self.config(bg = c1) # Un color de fondo

        ## configuración de filas y columnas para toda la ventana principal, permitiendonos centrar el contenido sin importar el tamaño de la ventana
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.toplevel_window = None # Variable que nos ayudadrá a saber si ya hay abierta una ventana nueva


        # marcos
        ## marco 1: ingreso de usuario
        self.marco1 = CTkFrame(self, fg_color=c1, bg_color=c1) #le ponemos el mismo color que el de fondo de pantalla
        self.marco1.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)
        ### configuración de columnas y ventanas del marco
        self.marco1.columnconfigure([0, 1], weight=1)
        self.marco1.rowconfigure([0,1,2,3,4,5], weight=1) 

        ## marco 2: marco de la ventana principal
        self.marco2 = CTkFrame(self, fg_color=c1, bg_color=c1) #le ponemos el mismo color que el de fondo de pantalla
        # self.marco2.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)
        ### configuración de columnas y ventanas del marco
        self.marco2.columnconfigure([0, 1], weight=1)
        self.marco2.rowconfigure([0,1,2,3,4,5], weight=1) 

        
        
        # Widgets marco 1
        ## Etiqueta usuario
        self.l_usuario = CTkLabel(self.marco1, font=(fuente, 14), bg_color=c1, fg_color=c1, text_color=c4, text="Usuario: ")
        self.l_usuario.grid(column=0, row=1, padx=4, pady=4)

        ## Entrada de usuario
        self.e_usuario = CTkEntry(self.marco1,font=(fuente, 14), bg_color=c1, fg_color= c1, text_color=c4, placeholder_text="Ingresar usuario", border_color=c4)
        self.e_usuario.grid(column=1, row=1, padx=4, pady=4) # Se va a colocar en la primera fila

        ## Boton crear usuario
        self.b_crear_usuario = CTkButton(self.marco1, bg_color=c1, fg_color=c4, text_color=c1, text="Nuevo usuario", border_color=c4, command=self.open_toplevel)
        self.b_crear_usuario.grid(column=0, row=2, padx=4, pady=4)

        ## Boton para entrar
        self.b_entrar = CTkButton(self.marco1, bg_color=c1, fg_color=c4, text_color=c1, text="Entrar", border_color=c4)
        self.b_entrar.grid(column=1, row=2, padx=4, pady=4)

        ## Botón para cerrar
        self.b_cerrar = CTkButton(self.marco1, bg_color=c1, fg_color=c4, text_color=c1, text="Cerrar aplicación", border_color=c4)
        self.b_cerrar.grid(columnspan=2, row=3, padx=4, pady=4)

    # Funciones
    ## Botones para cambiar de marcos
    def mostrar_marco1():
        self.marco2.forget()
        self.marco1.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)
    
    def mostrar_marco2():
        self.marco1.forget()
        self.marco2.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)
    
    def open_toplevel(self): # código de: https://customtkinter.tomschimansky.com/documentation/windows/toplevelsf
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = gestion_usuarios.ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it



# Main

if __name__ == "__main__":
    inicio = V_principal()
    inicio.mainloop()

