# Creación de una ventana de inicio de sesión con custom tkinter
# Talvez no necesitemos una ventana de inicio de sesión, 
# pero podemos usarla para inspirarnos


from customtkinter import CTk, CTkFrame
from tkinter import PhotoImage

# Variables útiles
c_negro =  "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67"



# Ventana principal
root = CTk()
root.geometry("500x600+350+20") #Dimensión de la ventana + 350 posiciones hacia la derecha + 20 posiciones hacia abajo
root.minsize(480, 500) #Tamaño mínimo al que podrá modificar el usuario
root.config(bg = c_negro) #Cambio de color del background

logo = PhotoImage(file = "recursos/Starbucks-Logo-600x338.png")

root.call("wm", "iconphoto", root._w, logo)
root.mainloop()