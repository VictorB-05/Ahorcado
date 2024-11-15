import tkinter as tk
from tkinter import Frame

import winsound

def on_release(key):
    try:
        if key.char.isalpha(): #Mira si la tecla es una letra
            print(f"Tecla presionada: {key.char}")
        else:
            winsound.Beep(1400, 500)
            print(f"Tecla presionada: {key.char}")
    except AttributeError:
        # Emitir un beep de cuando la tecla no es una letra
        winsound.Beep(1400, 500)
        print(f"Tecla especial presionada: {key}")


ventana = tk.Tk()
ventana.geometry('1000x600')
frame = Frame(ventana,width=1000,height=600,bg="#ffb0c8",borderwidth=10,relief="ridge")
frame.place(x=0,y=0)

ventana.mainloop()