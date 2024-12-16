from config import *
import funciones_botones as f

class FrInstrucciones(CustomFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.columnconfigure([0, 1, 2, 3, 4], weight=1)

        # Widgets

        ## Etiquetas
        ### Título
        self.l_titulo = CustomLabel(self, text="Instrucciones")
        self.l_titulo.configure(font=(fuente, t_fuente+4, "bold"))
        self.l_titulo.grid(row=0, column=2)
        ### Pasos
        self.l_paso1 = CustomLabel(self, text="Paso 1. Realice 20 sentadillas")
        self.l_paso1.grid(row=1, column=2)
        self.l_paso2 = CustomLabel(self, wraplength=400, text="Paso 2. Coloque el dedo sobre el sensor y presion el botón 'Empezar'")
        self.l_paso2.grid(row=2, column=2)
        self.l_recomendacion = CustomLabel(self, wraplength=400, text="Recomendación: No muevas el dedo del sensor ni realices movimientos bruscos")
        self.l_recomendacion.grid(row=3, column=2)

        ## Botones
        ### Cambiar páginas
        self.b_anterior = CustomButton(self, text="Anterior", command= lambda: f.mostrar_frame(self.anterior))
        self.b_anterior.grid(row=5, column=1)

        self.b_siguiente = CustomButton(self, text="Continuar", command= lambda: f.mostrar_frame(self.siguiente))
        self.b_siguiente.grid(row=5, column=3)


if __name__ == "__main__":
    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("700x500")
            self.grid_rowconfigure(0, weight=1)  # configure grid system
            self.grid_columnconfigure(0, weight=1)

            self.frame_prueba = CustomFrame(self)

            self.my_frame = FrInstrucciones(self)
            self.my_frame.set_siguiente(self.frame_prueba)
            self.my_frame.set_anterior(self.frame_prueba)

            self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    app = App()
    app.mainloop()