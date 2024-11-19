""" 
Ps, yo creo que mejor le hacemos su propia ventana a la aplicación principal
Código creado por: Rubén ebrio a las 4am ;)
Documentación: https://customtkinter.tomschimansky.com/documentation/widgets/frames
"""
import customtkinter
from config import * # variables reservadas: c1, c2, c3, c4, c5, c_blanco, c_negro, fuente, t_fuente.
import funciones_botones as f

# Marco del programa principal
class V_principal(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=c1, bg_color=c1, **kwargs)

        # Configuraciones del marco
        self.columnconfigure([0, 1, 2], weight=1)
        self.rowconfigure([0,1,2,3,4,5], weight=1) 

        # Widgets del Frame principal
        ## Etiqueta menu principal
        self.titulo = CustomLabel(self, text="Menu Principal")
        self.titulo.grid(row=0, columnspan=3, padx=20)
        ## Botón de nuevo registro
        self.b_nuevo = CustomButton(self, text="Nuevo registro")
        self.b_nuevo.grid(row=1, column=0, padx=4, pady=4)
        ## Botón para
        ## Botón para ver registros
        self.b_ver = CustomButton(self, text="Ver registros")
        self.b_ver.grid(row=1, column=2, padx=4,pady=4)
        ## Botón para salir
        self.b_salida = CustomButton(self, text="Salir de la aplicación", command=lambda: f.cerrar_ventana(self))
        self.b_salida.grid(row=2, column=2, padx=20, pady=20)


# Aqui podemos probar que el marco funcione correctamente y sin errores:
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = V_principal(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()