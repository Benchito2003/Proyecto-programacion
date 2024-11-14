#utilizar pygame no como juego, sino como una forma de agregar sonido a la aplicación
from tkinter import *
import pygame
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of window
win.geometry("700x500")

# Add a background image
bg = ImageTk.PhotoImage(file="recursos/cruz.png")

label = Label(win, image=bg)
label.place(x=0, y=0)

# Initialize mixer modulle in pygame
pygame.mixer.init()

# Define a function to play the music
def play_sound():
    pygame.mixer.music.load("/home/chino/Desktop/Proyecto-programacion/recursos/pou.wav") # nota, está muy limitado con mp3
    pygame.mixer.music.play()

# Add a button widget
b1 = Button(win, text="Play Music", command=play_sound)
b1.pack(pady=60)

win.mainloop()