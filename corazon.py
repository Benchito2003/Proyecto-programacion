# Etiqueta para gif del corazon
import customtkinter
from PIL import Image

"""  
Código tomado de: https://stackoverflow.com/questions/77943528/how-to-display-gif-or-mp4s
"""

class CorazonGif(customtkinter.CTkLabel):
    def __init__(self, master, ubicacion_imagen, **kwargs):
        self.imagen_gif = Image.open(ubicacion_imagen)
        #Tamaño de la  imagen
        kwargs.setdefault("width", self.imagen_gif.width)
        kwargs.setdefault("height", self.imagen_gif.height)
