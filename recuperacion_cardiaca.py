# Módulos generales
import customtkinter
import funciones_botones as f
from config import *

# Módulos específicos
import rc_bienvenida, rc_captura, rc_instrucciones, rc_resultados

# Ventana nueva para el registrar el índice de recuperación cardiaca
class VHRR(customtkinter.CTkToplevel): # Ventana de Hearth Rate Recovery
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        ## Configuración inicial de la ventana
        self.geometry("700x500")
        self.minsize(700, 500)
        self.title("Nuevo Registro")
        self.config(bg=c1)
        ## Configuraciones del grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        """ 
        La ventana consta de 4 frames: 
            1. Explicación.
            2. Indicación del ejercicio.
            3. Captura de frecuencias.
            4. Resultado de las prueba.
        """

        # Widgets
        ## Frames:
        ### Marco de explicación
        self.marco1 = rc_bienvenida.FrBienvenida(self)
        self.marco1.grid(row=0, column=0, sticky="nsew")
        ### Marco de las instrucciones
        self.marco2 = rc_instrucciones.FrInstrucciones(self)
        self.marco2.set_anterior(self.marco1)
        self.marco1.set_siguiente(self.marco2) # El marco 2 es el que le sigue al marco 1 y asi sucesivamente
        ### Marco de captura de frecuencias
        self.marco3 = rc_captura.FrCapturaFrecuencias(self)
        self.marco2.set_siguiente(self.marco3)
        ### Marco de resultados
        self.marco4 = rc_resultados.FrResultados(self)

if __name__ == "__main__":
    class App(customtkinter.CTk):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("500x400")

            self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command=self.open_toplevel)
            self.button_1.pack(side="top", padx=20, pady=20)
    
            self.toplevel_window = None

        def open_toplevel(self):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = VHRR(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it
    
    app = App()
    app.mainloop()