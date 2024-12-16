from config import *
import funciones_botones as f

class FrBienvenida(CustomFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Widgets
        ## Etiquetas
        ### Título:
        self.l_titulo =  CustomLabel(self, text="¿Qué es el índice de recuperación cardiaca?")
        self.l_titulo.configure(font=(fuente, t_fuente+4, "bold"))
        self.l_titulo.grid(row=0, column=1)
        ### Explicación
        self.l_text = CustomLabel(self, wraplength=400, text="El índice de recuperación cardaica o HRR (Hearth Rate Recovery), es una herramienta que nos permite medir la capacidad que tiene el corazón de recuperarse tras un esfuerzo físico. Útil para conocer la salud del corazón.")
        self.l_text.grid(row=1, column=1)

        ## Botones
        ### Siguiente
        self.b_siguiente = CustomButton(self, text="Siguiente", command= lambda:f.mostrar_frame(self.siguiente))
        self.b_siguiente.grid(row=2, column=1)
        ### salida
        self.b_salida = CustomButton(self, text="Salir", command=lambda: f.cerrar_ventana(master))
        self.b_salida.grid(row=4, column=1)

if __name__ == "__main__":
    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("700x500")
            self.grid_rowconfigure(0, weight=1) 
            self.grid_columnconfigure(0, weight=1)

            self.frame_prueba = CustomFrame(self)

            self.my_frame = FrBienvenida(self)
            self.my_frame.set_siguiente(self.frame_prueba)

            self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


    app = App()
    app.mainloop()