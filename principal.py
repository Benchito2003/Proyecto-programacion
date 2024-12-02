""" 
Frame principal: Este es el frame donde se crean nuevos registros, se ven los registros previos y
donde se puede hacer la prueba de esfuerzo
Documentación: https://customtkinter.tomschimansky.com/documentation/widgets/frames
"""
# Importamos librerías
## Librerías de python
import customtkinter
## Módulos propios
### Configuración general:
from config import * # variables reservadas: c1, c2, c3, c4, c5, c_blanco, c_negro, fuente, t_fuente.
### Funciones generales de los botones
import funciones_botones as f
### ventanas que van a surgir de esta clase
import ver_registros
import nuevo_registro

# Marco del programa principal
class FrPrincipal(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=c1, bg_color=c1, **kwargs)

        # Configuraciones grid del marco
        self.columnconfigure([0, 1, 2], weight=1)
        self.rowconfigure([0,1,2,3,4,5], weight=1)

        # Widgets del Frame principal
        ## Etiqueta menu principal
        self.titulo = CustomLabel(self, text="Menu Principal")
        self.titulo.grid(row=0, columnspan=3, padx=20)
        ## Botón de nuevo registro
        self.b_nuevo = CustomButton(self, text="Nuevo registro", command = lambda: f.abrir_ventana(master, nuevo_registro.VNuevoRegistro))
        self.b_nuevo.grid(row=1, column=0, padx=4, pady=4)
        ## Botón para prueba de esfuerzo
        self.b_esfuerzo = CustomButton(self, text="Prueba de esfuerzo")
        self.b_esfuerzo.grid(row=1, column=1, padx=4, pady=4)
        ## Botón para ver registros
        self.b_ver = CustomButton(self, text="Ver registros", command= lambda:f.abrir_ventana(master, ver_registros.VverRegistros))
        self.b_ver.grid(row=1, column=2, padx=4,pady=4)
        ## Botón para salir
        self.b_salida = CustomButton(self, text="Salir de la aplicación", command=lambda: f.cerrar_ventana(master))
        self.b_salida.grid(row=4, column=2, padx=4, pady=4)


# Aqui podemos probar que el marco funcione correctamente y sin errores:
if __name__ == "__main__":
    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("400x200")
            self.grid_rowconfigure(0, weight=1)  # configure grid system
            self.grid_columnconfigure(0, weight=1)

            self.ventana_abierta = None

            self.my_frame = FrPrincipal(master=self)
            self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    app = App()
    app.mainloop()