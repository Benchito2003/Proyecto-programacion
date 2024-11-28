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
import marco0
import creacion_usuarios
import login
import funciones_botones as f
import principal
from config import * # variables reservadas: c1, c2, c3, c4, c5, c_blanco, c_negro, fuente, t_fuente.


# Ventana principal
# Esta es la vetnana que se ejecutará
class Vinicio(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Popiedades de la ventana
        self.geometry("500x200")  # Geometría (Aun puede ser cambiada)
        self.minsize(500, 200) # tamaño mínimo para que no pasen cosas extrañas ;)
        self.config(bg = c1) # Un color de fondo
        self.title("Life Rhythm")

        ## configuración de filas y columnas para toda la ventana principal, permitiendonos centrar el contenido sin importar el tamaño de la ventana
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Ventanas
        self.ventana_abierta = None # Variable que nos ayudadrá a saber si ya hay abierta una ventana nueva

        # marcos
        ## marco 2: marco de la ventana principal
        self.marco2 = principal.FrPrincipal(master=self) 
        ## marco 1: ingreso de usuario
        self.marco1 = login.FrLogin(self, self.marco2)
        ## Marco 0: Presentación del programa
        self.marco0 = marco0.Presenteishon(master=self, marco_siguiente=self.marco1)
        self.marco0.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)


# Main

if __name__ == "__main__":
    inicio = Vinicio()
    inicio.mainloop()

