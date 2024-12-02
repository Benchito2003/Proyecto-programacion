
# Para guardar las funciones de los botones y no repetir código
# Aclaración: no es necesario poner aqui todas las funciones, solo las que probablemente se vana a repetir en todas las ventanas, como la función de cerrar ventanas
import customtkinter

## Cerrar la ventana(puedes pasarle el atributo self para cerrar la ventana padre)
def cerrar_ventana(ventana_a_cerrar):
    ventana_a_cerrar.destroy()

def abrir_ventana(ventana_padre, ventana_hija): #  código de: https://customtkinter.tomschimansky.com/documentation/windows/toplevelsf
    if ventana_padre.ventana_abierta is None or not ventana_padre.ventana_abierta.winfo_exists(): # Si la ventana no existe
        ventana_padre.ventana_abierta = ventana_hija(ventana_padre) # Crea una nueva ventana 
    else:
        ventana_padre.ventana_abierta.focus()

def mostrar_frame(frame):
    frame.place(relwidth=1, relheight=1)
    frame.tkraise()

## Funciones para borarr/obtener datos de entrys
def obtener_texto(entry):
    texto = entry.get()
    return texto

def borrar_texto(entry):
    entry.delete(0, 'end')

def reemplazar_texto(entry, texto):
    entry.delete(0, 'end')
    entry.insert(0, texto)


""" ## Funciones relacionadas al mouse (en proceso)
def cambiar_estilo(boton):
    # Estilo a cambiar cuando el mouse está encima
    print("Hola mundo")


def restaurar_estilo(boton):
    # Regresar al estilo que tenía antes de que el mouse estuviera ahí de encimoso
    print("Adios mundo")
"""

# Pruebas
if __name__ == "__main__":
    import creacion_usuarios

    class App_ventana_nueva(customtkinter.CTk):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("500x400")

            self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command= lambda: abrir_ventana(self, creacion_usuarios.V_nuevo_usuario))
            self.button_1.pack(side="top", padx=20, pady=20)

            self.ventana_abierta = None

    app = App_ventana_nueva() # Para probar las ventanas nuevas
    app.mainloop()
