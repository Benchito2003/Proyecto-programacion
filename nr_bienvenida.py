from config import *
import funciones_botones as f

class FrBienvenida(CustomFrame):
    def __init__(self, master, frame_siguiente, **kwargs):
        super().__init__(master, **kwargs)
        
        # Widgets
        ## Etiquetas
        self.l_titulo = CustomLabel(self, text="Instrucciones")
        self.l_titulo.configure(font=(fuente, t_fuente+4, "bold"))
        self.l_titulo.grid(row=0, columnspan=4, padx=20, pady=20)

        self.l_paso1 = CustomLabel(self, text="1. Para realizar el registro es necesario estar sentado.")
        self.l_paso1.configure(font=(fuente, t_fuente+4, "bold"), text_color=c5)
        self.l_paso1.grid(row=1, columnspan=4, padx=4, pady=4, sticky="w")

        self.l_paso1_1 = CustomLabel(self,wraplength=300 , text="1.1. Asegurese de estar en un ambiente callado y sin distracciones 2 minutos antes y durante la prueba.")
        self.l_paso1_1.configure(text_color=c5)
        self.l_paso1_1.grid(row=2, column=0, columnspan=2, padx=4, pady=4, sticky="w")

        self.l_paso1_2 = CustomLabel(self, text="1.2. Durante la prueba no haga ningún movimiento.")
        self.l_paso1_2.configure(text_color=c5)
        self.l_paso1_2.grid(row=3, column=0, columnspan=2, padx=4, pady=4, sticky="w")

        self.l_paso2 = CustomLabel(self, wraplength=400, text="2. Coloque el dedo índice de su mano dominante sobre el sensor durante 20 segundos ininterrumpidos")
        self.l_paso2.configure(font=(fuente, t_fuente+4, "bold"), text_color=c5)
        self.l_paso2.grid(row=4, column=0, columnspan=4, padx=4, pady=4, sticky="w")

        ## Botones
        self.b_empezar = CustomButton(self, text="Empezar", corner_radius=20, width=200, height=50, command = lambda: f.mostrar_frame(frame_siguiente))
        self.b_empezar.grid(row=5, column=1, columnspan=2, sticky="e")

if __name__ == "__main__":
    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("700x500")
            self.grid_rowconfigure(0, weight=1)  # configure grid system
            self.grid_columnconfigure(0, weight=1)

            self.frame_prueba = CustomFrame(self)

            self.my_frame = FrBienvenida(self, self.frame_prueba)
            self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


    app = App()
    app.mainloop()

"""
Código obtenido de: https://customtkinter.tomschimansky.com/documentation/widgets/frame
"""