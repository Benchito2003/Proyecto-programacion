from tkinter import *
from PIL import Image, ImageTK
#Create an instance od tkinter frame
win=Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
#define a function to clone the window
def close_win():
    win.destroy()
#Load the image


file = "recursos/tocar.png"
image = Image.open(file)
#Resize the Image
image = image.resize((50,50), Image.Resampling.LANCZOS)
#Convert the image to PhotoImage
img = ImageTK.PhotoImage(image)
#Create a Label
Label(win, text="Click de below button to close the window", font=("Aerial 15 bold")).pack(pady=20)
#Create a label with the image
button = Button(win, text="Click Me", font=("Helvica 15 bold"), image=img, compound=LEFT, command=close_win)
button.pack()