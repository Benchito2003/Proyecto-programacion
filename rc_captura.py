""" Captura de frecuencias para calcular HRR """
from config import *
import funciones_botones as fb
import funciones_dataframes as fdf
import leer_pico

class FrCapturaFrecuencias(CustomFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.tiempo_espera = 60
        self.tiempo_primer_registro = 59
        self.tiempo_segundo_registro = 1

        # Widgets
        ## etiquetas
        ### Nota para recordar al usuario que haga primero las sentadillas
        self.l_recuerdo = CustomLabel(self, wraplength=200, text="No olvides hacer primero tus 20 sentadillas para llevar a tu coraźon a su frecuencia cardiaca máxima")
        self.l_recuerdo.grid(row=1, column=1)

        ### Primer registro
        self.l_primer_registro = CustomLabel(self, text="Primer registro")
        self.l_primer_registro.configure(font=(fuente, t_fuente+4, "bold"))
        self.l_primer_registro.grid(row=0, column=0, padx=20, pady=20)

        self.l_primer_frecuencia = CustomLabel(self, text = "")
        self.l_primer_frecuencia.configure(font=(fuente, 25), fg_color=c_blanco, text_color=c_negro, corner_radius=20)
        self.l_primer_frecuencia.grid(row=1, column=0, sticky="nsew")

        self.l_nota1 = CustomLabel(self, wraplength=200, text="Tu frecunecia cardiaca máxima fue: 100, la frecuencia máxima ideal para tu edad es: 10")

        ### Segundo registro
        self.l_segundo_registro = CustomLabel(self, text="Segundo registro")
        self.l_segundo_registro.configure(font=(fuente, t_fuente+4, "bold"))
        self.l_segundo_registro.grid(row=0, column=2, padx=20, pady=20)

        self.l_segunda_frecuencia = CustomLabel(self, text= "")
        self.l_segunda_frecuencia.configure(font=(fuente, 25), fg_color=c_blanco, text_color=c_negro, corner_radius=20)
        self.l_segunda_frecuencia.grid(row=1, column=2, sticky="nsew")

        ### Tiempo de espera
        self.l_texto_espera = CustomLabel(self, wraplength=200, text="Por favor deje el dedo en el sensor estos segundos:")

        self.l_tiempo_espera = CustomLabel(self, text=f"{self.tiempo_espera}")
        self.l_tiempo_espera.configure(font=(fuente, 25), fg_color=c_blanco, text_color=c_negro, corner_radius=20)

        ## botones
        self.b_comenzar = CustomButton(self, text="Comenzar", command=self.comenzar)
        self.b_comenzar.grid(row=3, column=1)

        self.b_siguiente = CustomButton(self, text="Continuar", command= lambda: fb.mostrar_frame(self.siguiente))

        self.b_salir = CustomButton(self, text="salir", command=lambda: fb.cerrar_ventana(master))
        self.b_salir.grid(row=4, column=0)
    
    # Funciones propias de la clase
    def comenzar(self):
        """ Funciones de comenzar """
        
        # 1. Ocultamos el botón de comenzar y la nota de recuerdo
        self.b_comenzar.grid_forget()
        self.l_recuerdo.grid_forget()
        # 2. Mostramos la cuenta regresiva
        self.l_texto_espera.grid(row=3, column=1)
        self.l_tiempo_espera.grid(row=4, column=1, sticky="nsew")
        # 3. Comenzamos la cuenta regresiva
        self.cuenta_regresiva(self.tiempo_espera)
    
    def cuenta_regresiva(self, tiempo):
        """  Prometo que esta es la ultima función de cuenta regresiva """
        if tiempo > 0:
            self.l_tiempo_espera.configure(text=f"{tiempo}")
            if tiempo == self.tiempo_primer_registro:
                self.l_nota1.grid(row=2, column=0)
                latido1 = leer_pico.obtener_frecuencia(10)
                self.l_nota1.configure(text=f"Tu frecuencia cardiaca máxima fue de {latido1} lpm, cuando la recomendable para tu edad es: {200 - 20}")
                self.l_primer_frecuencia.configure(text=f"{latido1} lpm")
            if tiempo == self.tiempo_segundo_registro:
                latido2 = leer_pico.obtener_frecuencia(10)
                self.l_segunda_frecuencia.configure(text=f"{latido2} lpm")
            self.after(1000, self.cuenta_regresiva, tiempo -1)
        else:
            self.l_tiempo_espera.configure(text="ya puedes retirar el dedo", font=(fuente, t_fuente))
            self.b_siguiente.grid(row=4, column=2)


if __name__ == "__main__":
    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("700x500")
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

            self.frame_prueba = CustomFrame(self)

            self.my_frame = FrCapturaFrecuencias(self)
            self.my_frame.set_siguiente(self.frame_prueba)

            self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


    app = App()
    app.mainloop()