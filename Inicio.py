import tkinter as tk
from tkinter import PhotoImage, Toplevel, Button
import keyboard

import Interfaz
import Logica
import database
from PIL import Image, ImageTk

def ajustarVentana(ventana, height, width):
    # Obtener las dimensiones de la pantalla
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()

    # Calcular la posición para centrar la ventana
    position_top = int(screen_height / 2 - height / 2)
    position_left = int(screen_width / 2 - width / 2)

    # Establecer la geometría de la ventana
    ventana.geometry(f"{width}x{height}+{position_left}+{position_top}")
def guardar():
    name = nombre.get("1.0", "end-1c")
    print(nombre.get("1.0", "end-1c"))
    if not name[0]==" " :

        Interfaz.juego(name,"f")


inico = tk.Tk()
inico.resizable(False,False)
inico.title("Ahorcado")
frame = tk.Frame(inico, bg="lightblue")
frame.pack(expand=True, fill="both")
frame.pack_propagate(False)
ajustarVentana(inico,400,600)

nombre = tk.Text(frame,
                   height = 1,
                   width = 20, font=("Vardana", 12))

nombre.place(x=200,y=140)

entrar = tk.Button(frame,text="Entrar",bg="#4449fc",command=guardar,fg="#e1e8a5",font=("Comic Sans MS", 20))
entrar.place(x=240,y=170)
inico.mainloop()