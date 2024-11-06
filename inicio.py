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
from customtkinter import CTk, CTkFrame, CTkEntry
import colores as col

# Colores escogidos
paleta = col.paleta2
c1 = paleta[0] # Para el fondo
c2 = paleta[1] # Iconos 1
c3 = paleta[2] # Iconos 2
c4 = paleta[3] # para los marcos
c5 = paleta[4] # Para las letras
c_negro = "#000000" #Colores constantes
c_blanco = "FFFFFF" #Colores constantes

# Ventana principal
v_principal = CTk() # En este caso va a ser un objeto de custom tkinter (para colores y diseños chidos)
v_principal.geometry("960x540") # Geometría a libre albedrío
v_principal.minsize(320, 540) #tamaño mínimo para que no pasen cosas extrañas ;)
v_principal.config(bg = c1)

## configuración de filas y columnas para toda la ventana principal, permitiendonos centrar el contenido sin importar el tamaño de la ventana
v_principal.columnconfigure(0, weight=1)
v_principal.rowconfigure(0, weight=1)

# marcos
## marco 1
marco1 = CTkFrame(v_principal, fg_color=c1, bg_color=c1) #le ponemos el mismo color que el de fondo de pantalla
marco1.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)
### configuración de columnas y ventanas del marco
marco1.columnconfigure([0, 1], weight=1)
marco1.rowconfigure([0,1,2,3,4,5], weight=1) 


#Entrada de nombre
e_nombre = CTkEntry(marco1,font=("sans rerif", 14), bg_color=c1, fg_color= c1, text_color=c4, placeholder_text="Nombre", border_color=c4)
e_nombre.grid(columnspan=2, row=1, padx=4, pady=4) # Se va a colocar en la primera fila


v_principal.mainloop()
