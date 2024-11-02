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
import customtkinter as CTk
import colores as col

#Colores escogidos
paleta = col.paleta2
c1 = paleta[0] # Color mas oscuro
c2 = paleta[1] # 
c3 = paleta[2] # 
c4 = paleta[3] # 
c5 = paleta[4] # Color más claro

# Ventana principal
v_principal = CTk() # En este caso va a ser un objeto de custom tkinter (para colores y diseños chidos)
v_principal.geometry("500x600+350+20") # Geometría a libre albedrío
v_principal.minsize(480, 50)
v_principal.config(bg = c)




v_principal.mainloop()
