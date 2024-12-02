import customtkinter
from config import * # variables reservadas: c1, c2, c3, c4, c5, c_blanco, c_negro, fuente, t_fuente.
import funciones_botones as f
import funciones_dataframes as f_df
import creacion_usuarios
import pandas as pd

# Marco para el "login"
class FrLogin(customtkinter.CTkFrame):
    def __init__(self, master, frame_siguiente, **kwargs):
        super().__init__(master, fg_color=c1, bg_color=c1, **kwargs)

        # Configuraciones grid del marco
        self.columnconfigure([0,1], weight=1)
        self.rowconfigure([0,1,2,3,4,5], weight=1)

        # Lista de usuarios
        self.lista_usuarios = self.buscar_usuarios()

        #Widgets del marco "login"
        ## Etiqueta usuario
        self.l_usuario = CustomLabel(self, text="Codigo de usuario:") 
        self.l_usuario.grid(column=0, row=1, padx=4, pady=4)

        ## Escoger usuario
        self.cb_usuario = CustomComboBox(master=self, valores=self.lista_usuarios, comando=self.entrar)
        self.cb_usuario.set("selección")
        self.cb_usuario.grid(column=1, row=1, padx=4, pady=4)

        ## Boton crear usuario
        self.b_crear_usuario = CustomButton(self, text="Nuevo usuario", command=lambda: f.abrir_ventana(master, creacion_usuarios.VCrearUsuario))
        self.b_crear_usuario.grid(column=0, row=2, padx=4, pady=4)

        ## Boton para entrar
        self.b_entrar = CustomButton(self, text="Entrar", command=lambda: f.mostrar_frame(frame_siguiente))
        # self.b_entrar = CustomButton(self, text="Actualizar", command=self.actualizar)

        self.b_entrar.grid(column=1, row=2, padx=4, pady=4)

        ## Botón para cerrar
        self.b_cerrar = CustomButton(self, text="Salir de la aplicación", command= lambda: f.cerrar_ventana(master))
        self.b_cerrar.grid(columnspan=2, row=3, padx=4, pady=4)
    
    def buscar_usuarios(self, fichero="usuarios.csv"):
        if f_df.verificar_archivo(fichero):
            df = pd.read_csv(fichero)
            lista_usuarios = df["Codigo"].tolist()
            return lista_usuarios
        else:
            print("No hay dataframe por leer")
            lista_usuarios = ["actualizar"]
            return lista_usuarios
    
    def entrar(self, opcion):
        print(f"tu opción fue: {opcion}")
        if opcion == "actualizar":
            lista_usuarios =  self.buscar_usuarios()
            self.cb_usuario.configure(values=lista_usuarios)
        else:
            pass
    
    def actualizar(self):
        self.cb_usuario.configure(values=self.buscar_usuarios())


# Para probar que todo funcione
if __name__ == "__main__":
    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("400x200")
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

            self.marco_ejemplo = customtkinter.CTkFrame(self)
            self.ventana_abierta = None

            self.my_frame = FrLogin(self, self.marco_ejemplo)
            self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    app = App()
    app.mainloop()