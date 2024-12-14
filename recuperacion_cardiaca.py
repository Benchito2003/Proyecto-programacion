# Módulos generales
import customtkinter
import funciones_botones as f
from config import *

# Módulos específicos

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
        self.columnconfigure([0, 1, 2], weight=1)
        self.rowconfigure([0,1,2,3,4,5], weight=1)

        """ 
        La ventana consta de 5 frames: 
            1. Indiciaciones.
            2. Primera captura (en reposo).
            3. Segunda captura (despues de hacer ejericio).
            4. Tercera captura (despues del descanso).
            5. Presentación de resultados.
        """

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