# Creación de una ventana de inicio de sesión con custom tkinter
# Talvez no necesitemos una ventana de inicio de sesión, 
# pero podemos usarla para inspirarnos


from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkCheckBox, CTkImage
from tkinter import PhotoImage 
from PIL import Image #En nuestro caso utilizaremos otra librería para las imagenes

# Variables útiles
c_negro =  "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67d"



# Ventana principal
root = CTk()
root.geometry("500x600+350+20") #Dimensión de la ventana + 350 posiciones hacia la derecha + 20 posiciones hacia abajo
root.minsize(480, 500) #Tamaño mínimo al que podrá modificar el usuario
root.config(bg = c_negro) #Cambio de color del background


# Imágenes
logo = PhotoImage(file = "recursos/Starbucks-Logo-600x338.png")
# subida = PhotoImage(file="recursos/cloud-upload-alt (2).png")
fondo = CTkImage(light_image=Image.open("recursos/Starbucks-Logo-600x338.png"), dark_image=Image.open("recursos/Starbucks-Logo-600x338.png"), size=(425, 250))
subida = CTkImage(light_image=Image.open("recursos/cloud-upload-alt (2).png"), dark_image=Image.open("recursos/cloud-upload-alt (2).png"), size=(30, 30))



frame = CTkFrame(root, fg_color=c_negro, bg_color=c_negro)
frame.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)

frame.columnconfigure([0, 1], weight=1)
frame.rowconfigure([0,1,2,3,4,5], weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

CTkLabel(frame, image=fondo, text="",fg_color="transparent", bg_color="transparent").grid(columnspan=2, row=0)

correo = CTkEntry(frame, font=("sans rerif", 12), bg_color=c_negro, text_color=c_verde, placeholder_text="Correo electronico", border_color=c_verde, fg_color=c_negro, width = 220, height= 40)
correo.grid(columnspan=2, row=1, padx=4, pady=4)

password = CTkEntry(frame, font=("sans rerif", 12), bg_color=c_negro, text_color=c_verde, placeholder_text="Contraseña", border_color=c_verde, fg_color=c_negro, width = 220, height= 40)
password.grid(columnspan=2, row=2, padx=4, pady=4)

checamesta = CTkCheckBox(frame, text="Recuerdame", hover_color=c_morado, border_color=c_verde, fg_color=c_verde, text_color=c_verde)
checamesta.grid(columnspan=2, row=3, padx=4, pady=4)

bt_iniciar = CTkButton(frame, font=("sans serif", 12), text_color=c_verde, border_color=c_verde, fg_color=c_negro, hover_color=c_morado, corner_radius=12, border_width=2, text="INICIAR SESION", height=40)
bt_iniciar.grid(columnspan=2, row = 4, pady=4, padx=4)

bt_subir = CTkButton(frame, font=("sans serif", 12), text_color=c_verde, border_color=c_verde, fg_color=c_negro, hover_color=c_morado, corner_radius=12, border_width=2, image=subida, text= "Subir imagen", height=40)
bt_subir.grid(columnspan=2, row = 5, pady=4, padx=4)



root.call("wm", "iconphoto", root._w, logo)
root.mainloop()