# Módulo para guardar configuraciones globales:
# Si queremos cambiar el color de la aplicación se hace desde aquí y no desde cada ventana
import colores
import customtkinter
from tkinter import font

# Colores escogidos
paleta = colores.paleta5
c1 = paleta[0] # Para el fondo
c2 = paleta[1] # Iconos 1
c3 = paleta[2] # Iconos 2
c4 = paleta[3] # para los marcos
c5 = paleta[4] # Para las letras (contraste del fondo)
c_negro = "#000000" #Colores constantes
c_blanco = "#FFFFFF" #Colores constantes

# Fuente para todas las ventanas a menos que quieras una una fuente específica
fuente = "Times New Roman"
t_fuente = 14 # tamaño de la fuente
# fuente_negritas = "Arial Black"

# Alternativa a fuente
""" fuente_normal = font.Font(family="sans rerif", size=14)
fuente_negra = font.Font(family="sans rerif", size=14, weight="bold") """

# Estilo general de etiquetas
class CustomLabel(customtkinter.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, font=(fuente, t_fuente), bg_color=c1, fg_color=c1, text_color=c4, **kwargs)

# Estilo general de botones
# CTkButton(self.marco1, font=(fuente, t_fuente), bg_color=c1, fg_color=c4, text_color=c1, text="Nuevo usuario", border_color=c4) # Para botones parecidos

class CustomButton(customtkinter.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, font=(fuente, t_fuente), bg_color=c1, fg_color=c4, text_color=c1, border_color=c4, **kwargs)

# Estilo general de las entradas
# self.e_usuario = CTkEntry(self.marco1,font=(fuente, t_fuente), bg_color=c1, fg_color= c1, text_color=c4, placeholder_text="Ingresar usuario", border_color=c4)

class CustomEntry(customtkinter.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, font=(fuente, t_fuente), bg_color=c1, fg_color=c1, text_color=c4, border_color=c4, **kwargs)


# Estilo general de los combobox

class CustomComboBox(customtkinter.CTkComboBox):
    def __init__(self, master, valores, comando, **kwargs):
        super().__init__(master, values=valores, command=comando, font=(fuente, t_fuente), dropdown_font=(fuente, t_fuente), bg_color=c1, hover=True, justify="center", fg_color=c4)


# Configuración de Frames
class CustomFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=c1, bg_color=c1,**kwargs)

        ## Configuraciones del grid
        self.columnconfigure([0, 1, 2], weight=1)
        self.rowconfigure([0,1,2,3,4,5], weight=1)