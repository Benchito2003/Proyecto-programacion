from config import *
import funciones_botones as f

class FrCaptura(CustomFrame):
    def __init__(self, master, frame_siguiente, **kwargs):
        super().__init__(master, **kwargs)

        #Variables de control
        self.tiempo=20
        
        # Widgets
        self.l_titulo = CustomLabel(self, text="Captura de frecuencia cardiaca")
        self.l_titulo.grid(row=0, column=0, columnspan=3)

        self.l_tiempo = CustomLabel(self, text=f"{self.tiempo}")
        self.l_tiempo.configure(font=(fuente, 25), fg_color=c_blanco, text_color=c_negro, corner_radius=20)
        self.l_tiempo.grid(row=1, column=1, sticky="nsew")

        # Botones
        self.b_iniciar = CustomButton(self, text="Iniciar", command= lambda: self.cuenta_regresiva(self.tiempo))
        self.b_iniciar.grid(row=2, column=1)

        self.b_siguiente = CustomButton(self, text="siguiente", command= lambda: f.mostrar_frame(frame_siguiente))

        self.b_reiniciar = CustomButton(self, text="reinicar prueba", command=self.reinicio)

        self.b_salir = CustomButton(self, text="Salir", command= lambda: f.cerrar_ventana(master))
        self.b_salir.grid(row=5, column=1, columnspan=2, sticky="e")

        # Funciones
    def cuenta_regresiva(self, tiempo):
        """ Función para una cuenta regresiva :o """
        self.b_iniciar.grid_forget()
        if tiempo > 0:
            self.l_tiempo.configure(text=f"{tiempo}")
            self.after(1000, self.cuenta_regresiva, tiempo-1) 
            # La función se llama así misma cada 1000 ms y recibe de argumento el tiempo anterior menos 1
        else:
            self.l_tiempo.configure(text="Prueba terminada")
            self.b_siguiente.grid(row=3, column=1)
            self.b_reiniciar.grid(row=4, column=1)
    
    def reinicio(self):
        self.l_tiempo.configure(text=f"{self.tiempo}")
        self.b_iniciar.grid(row=2, column=1)
        self.b_siguiente.grid_forget()
        self.b_reiniciar.grid_forget()


if __name__ == "__main__":
    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("700x500")
            self.grid_rowconfigure(0, weight=1)  # configure grid system
            self.grid_columnconfigure(0, weight=1)

            self.frame_prueba = CustomFrame(self)

            self.my_frame = FrCaptura(self, self.frame_prueba)
            self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


    app = App()
    app.mainloop()

"""
Código obtenido de: https://customtkinter.tomschimansky.com/documentation/widgets/frame
"""