from config import *
import funciones_botones as f

class FrResultados(CustomFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Widgets
        ## Etiquetas
        self.l_titulo = CustomLabel(self, text="Resultados")
        self.l_titulo.configure(font=(fuente, t_fuente+4, "bold"))
        self.l_titulo.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        ### Resultado esperado

        # self.l_resultado_esperado = CustomLabel(self, text="Frecuencia cardiaca máxima acorde a su edad: {220 - edad}")

        ### Resultado obtenido

        self.l_latidos = CustomLabel(self, text="125 lpm")
        self.l_latidos.configure(font=(fuente, 25), fg_color=c_blanco, text_color=c_negro, corner_radius=20)
        self.l_latidos.grid(row=1, column=1, sticky="nsew")

        self.l_nota = CustomLabel(self, wraplength=200, text="NOTA: En caso de haber despegado el dedo del sensor, tendra que repetir la prueba.")
        self.l_nota.configure(text_color=c5)
        self.l_nota.grid(row=2, column=0)

        ## Botones
        self.b_guardar = CustomButton(self, text="Guardar", command= lambda: f.cerrar_ventana(master))
        self.b_guardar.grid(row=2, column=1)

        self.b_borrar = CustomButton(self, text="Borrar", command= lambda: f.cerrar_ventana(master))
        self.b_borrar.grid(row=3, column=1)

        self.b_salir = CustomButton(self, text="salir", command= lambda: f.cerrar_ventana(master))
        self.b_salir.grid(row=3, column=2)



if __name__ == "__main__":
    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("700x500")
            self.grid_rowconfigure(0, weight=1)  # configure grid system
            self.grid_columnconfigure(0, weight=1)

            self.my_frame = FrResultados(master=self)
            self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


    app = App()
    app.mainloop()

"""
Código obtenido de: https://customtkinter.tomschimansky.com/documentation/widgets/frame
"""