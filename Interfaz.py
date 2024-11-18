import tkinter as tk
from tkinter import Frame, Label
import keyboard
import Logica

# Almacenar teclas presionadas para evitar letras duplicadas
teclas_presionadas = set()

def manejar_presion(event):
    # Verificar si la tecla es una letra y no está en teclas_presionadas
    if event.name.isalpha() and event.name not in teclas_presionadas:
        teclas_presionadas.add(event.name)
        resultado.set(event.name)

    #Esto hace que solo puedas tocar la letra una vez

ventana = tk.Tk()
ventana.geometry('1000x600')
frame = Frame(ventana,width=1000,height=600,bg="#ffb0c8",borderwidth=10,relief="ridge")
frame.place(x=0,y=0)
resultado = tk.StringVar()
resultado.set("inicio")
label1 = Label(frame,textvariable=resultado, font=("Arial",30), bg="#ffb0c8")
label1.place(height=200,width=400)

keyboard.on_press(manejar_presion)

ventana.mainloop()