""" Marco de presentación del programa """
import customtkinter
from config import *
import funciones_botones as f

class Presenteishon(customtkinter.CTkFrame):
    def __init__(self, master, marco_siguiente, **kwargs):
        super().__init__(master, fg_color=c1, bg_color=c1, **kwargs)

        # Configuraciones del marco
        self.columnconfigure([0, 1, 2], weight=1)
        self.rowconfigure([0,1,2,3,4,5], weight=1) 

        # Widgets
        ## Título
        self.l_titulo = CustomLabel(self, text = "Life Rhythm")
        self.l_titulo.configure(font=(fuente, 25, "bold"))
        self.l_titulo.grid(row=0, columnspan=3, padx=20)
        ## Botón para iniciar
        self.b_iniciar = CustomButton(self, text="Iniciar programa", command=lambda: f.mostrar_frame(marco_siguiente))
        self.b_iniciar.grid(row=3, column=1, padx=4, pady=4)

    def iniciar_animacion(self):
        pass

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.marco_ejemplo = customtkinter.CTkFrame(self)

        self.my_frame = Presenteishon(master=self, marco_siguiente=self.marco_ejemplo)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


if __name__ == "__main__":
    app = App()
    app.mainloop()

""" 
Código inspirado de:
https://customtkinter.tomschimansky.com/documentation/widgets/frame
"""