from config import *
import funciones_botones as f

class FrResultados(CustomFrame):
    pass

if __name__ == "__main__":
    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("700x500")
            self.grid_rowconfigure(0, weight=1)  # configure grid system
            self.grid_columnconfigure(0, weight=1)

            self.frame_prueba = CustomFrame(self)

            self.my_frame = FrResultados(self)
            self.my_frame.set_siguiente(self.frame_prueba)
            self.my_frame.set_anterior(self.frame_prueba)

            self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    app = App()
    app.mainloop()