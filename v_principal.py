""" 
Ps, yo creo que mejor le hacemos su propia ventana a la aplicación principal
Código creado por: Rubén ebrio a las 4am ;)
Documentación: https://customtkinter.tomschimansky.com/documentation/widgets/frames
"""


# Marco de la aplicación principal
class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)



# Aqui podemos probar que el marco funcione correctamente y sin errores:
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()