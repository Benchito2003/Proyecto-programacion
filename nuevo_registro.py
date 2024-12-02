import customtkinter
import funciones_botones as f
from config import *
import nr_bienvenida, nr_capturar, nr_resultados

# Ventana para la creación de los registros
class VNuevoRegistro(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ## Configuración inicial de la ventanana
        self.geometry("700x500")
        self.minsize(700, 500)
        self.title("Nuevo Registro")
        self.config(bg=c1)
        ## Configuraciones del grid
        self.columnconfigure([0, 1, 2], weight=1)
        self.rowconfigure([0,1,2,3,4,5], weight=1)

        """
        La ventana consta de 3 frames:
            1. Bienvenida al usuario
            2. Inicio de prueba
            3. Resultado
        """
        self.frame3 = nr_resultados.FrResultados(self)
        self.frame2 = nr_capturar.FrCaptura(self, self.frame3)
        self.frame1 = nr_bienvenida.FrBienvenida(self, self.frame2)
        self.frame1.grid(column=0, row=0, sticky="nsew", padx=50, pady=50)


# Clase de  prueba
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
                self.toplevel_window = VNuevoRegistro(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it
    
    
    app = App()
    app.mainloop()

""" Código de: https://customtkinter.tomschimansky.com/documentation/windows/toplevel """