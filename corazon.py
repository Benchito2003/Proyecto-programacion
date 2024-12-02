# Etiqueta para gif del corazon
import customtkinter
from PIL import Image, ImageSequence

# Creamos una clase que hereda las propiedades de una etiqueta de custom tkinter
class Gif_corazon(customtkinter.CTkLabel):
    def __init__(self, master, gif_path, *args, **kwargs):
        super().__init__(master, *args, text="", font=("sans rerif", 40), **kwargs)
        self.frames = []
        self.load_gif(gif_path)
        self.current_frame = 0
        self.animation_running = False
        #Solucion para el tamaño
        # self.width = width
        # self.height = height

        
    def load_gif(self, gif_path):
        gif = Image.open(gif_path)
        for frame in ImageSequence.Iterator(gif):
            frame_image = customtkinter.CTkImage(frame.convert("RGBA"))
            self.frames.append(frame_image) 

    """ def load_gif(self, gif_path):
        gif = Image.open(gif_path)
        for frame in ImageSequence.Iterator(gif):
        # Redimensiona cada frame al tamaño deseado:
            resized_frame = frame.resize((self.width, self.height), Image.ANTIALIAS)
            frame_image = customtkinter.CTkImage(resized_frame)
            self.frames.append(frame_image) """
    
    def start_animation(self, delay=100):
        self.animation_running = True
        self._animate(delay)

    def stop_animation(self):
        self.animation_running = False
    
    def _animate(self, delay):
        """ Controla la animación del gif """
        # Detener la animación si no está activa
        if not self.animation_running:
            return
        
        # Establece la imagen actual del frame
        self.configure(image=self.frames[self.current_frame])

        # Calcula el siguiente frame:
        self.current_frame += 1
        if self.current_frame >= len(self.frames):
            self.current_frame = 0 # Reinicia a la primera frame si llega al final
        
        # Programa la llamada a esta función después del retraso indicado
        self.after(delay, self._animate, delay)


# Ventana de prueba 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.gif_label = Gif_corazon(self, "sources/corazon2.gif")
        self.gif_label.grid(row=0, column=0, pady=20)
        self.gif_label.start_animation(delay=100) # Velocidad de animación en milisegundos

# Verificador de que todo funcione
if __name__ == "__main__":
    app =  App()
    app.mainloop()