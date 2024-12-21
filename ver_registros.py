import customtkinter
from config import *
import funciones_botones as f

class VverRegistros(customtkinter.CTkToplevel): # Ventana para ver registros
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1040x600")
        self.minsize(1040, 600)
        self.columnconfigure([0, 1, 2], weight=1)
        # self.rowconfigure([0,1,2,3,4,5], weight=1) 
        self.config(bg=c1)

        # Variables de control
        self.nombre_usuario = None
        self.codigo = None
        self.numero_registros = 10

        # Widgets
        ## Etiquetas
        self.l_titulo = CustomLabel(self, text=f"Registros de usuario")
        self.l_titulo.grid(row=0, column=0, padx=20, pady=20)

        self.generar_etiquetas(self.numero_registros)

        ## Botones
        self.b_salir = CustomButton(self, text="salir", command= lambda: f.cerrar_ventana(self))
        self.b_salir.grid(row=0, column=2)

        self.b_graficar = CustomButton(self, text="Graficar registros")
        self.b_graficar.grid(row=0, column=1)

    # Funciones propias de la ventana
    def generar_etiquetas(self, cantidad):
        " Generar etiquetas a corde con el npumero de registros que exitan"
        for i in range(cantidad):
            self.l_registro = CustomLabel(self, text=f"registro {i+1}")
            self.l_registro.grid(row=(i+1), column=0, padx=4, pady=4)

            self.b_borrar = CustomButton(self, text="Borrar registro")
            self.b_borrar.grid(row=(i+1), column=2, padx=4, pady=4)
    
    def ocultar_etiqueta(etiqueta):
        etiqueta.grid_forget()
    
    def actualizar_datos(self, codigo, usuario):
        self.codigo = codigo
        self.nombre_usuario = usuario
        self.l_titulo.configure(text=f"Registros de {usuario}")


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
                self.toplevel_window = VverRegistros(self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it
    app = App()
    app.mainloop()