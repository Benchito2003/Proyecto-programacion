# Importamos al papá de todas nuestras librerías
import customtkinter

#Importar módulos propios:
import colores as col

# Colores escogidos
paleta = col.paleta1
c1 = paleta[0] # Para el fondo
c2 = paleta[1] # Iconos 1
c3 = paleta[2] # Iconos 2
c4 = paleta[3] # para los marcos
c5 = paleta[4] # Para las letras (contraste del fondo)
c_negro = "#000000" #Colores constantes
c_blanco = "FFFFFF" #Colores constantes



# Clase de la ventana nueva
class V_nuevo_usuario(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="Ventana de cración de usuarios")
        self.label.pack(padx=20, pady=20)

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
