import tkinter as tk
from tkinter import PhotoImage, Toplevel, Button
import keyboard
import Logica
import database
from PIL import Image, ImageTk

from database import palabras

abecedario = [chr(i) for i in range(97, 123)]  # abecedario
teclas_presionadas = set()  # Almacenar teclas presionadas para evitar letras duplicadas

def ajustarVentana(ventana, height, width):
    # Obtener las dimensiones de la pantalla
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()

    # Calcular la posición para centrar la ventana
    position_top = int(screen_height / 2 - height / 2)
    position_left = int(screen_width / 2 - width / 2)

    # Establecer la geometría de la ventana
    ventana.geometry(f"{width}x{height}+{position_left}+{position_top}")

ventana = tk.Tk()
ventana.resizable(False,False)
ventana.title("Ahorcado")
frame = tk.Frame(ventana, bg="lightblue")
frame.pack(expand=True, fill="both")
frame.pack_propagate(False)
ajustarVentana(ventana,800,1400)

letraR = tk.StringVar()
palabra = database.palabras("F")
logica = Logica

def juego(jugador,palabra):
    global teclas_presionadas, logica
    database.iniciar()
    palabra = database.palabras(palabra)
    logica = Logica.Logica(jugador, palabra[1])#se pasa solo la palabra la logica

    # Variables

    letraR.set("LETRA: _")

    resultado = tk.StringVar()
    resultado.set(logica.resultado)

    # Etiqueta 1
    label1 = tk.Label(frame, textvariable=letraR, font=("Arial", 30), bg="lightblue")
    label1.place(x=400, y=650, height=100, width=200)

    # Etiqueta 2
    rel = tk.Label(frame, textvariable=resultado, font=("Arial", 30), bg="lightblue")
    rel.place(x=650, y=650, height=100, width=400)

    img_path = "resorcues/ahorcado7.png"
    image = Image.open(img_path)
    img_tk = ImageTk.PhotoImage(image)

    lAhorcado = tk.Label(frame, image=img_tk)
    lAhorcado.place(x=400, y=20)

    nombre = tk.StringVar()
    nombre.set(logica.jugador)
    lNombre = tk.Label(frame, textvariable=nombre, font=("Arial", 30), bg="lightblue")
    lNombre.place(x=10, y=100)

    def reinit():
        global teclas_presionadas, palabra, logica
        palabra = database.palabras("F")
        logica = Logica.Logica(jugador,palabra[1])
        letraR.set("LETRA: _")
        resultado.set(logica.resultado)
        ahorcado()
        teclas_presionadas = set()

    def manejar_presion(event):
        global teclas_presionadas, palabra, logica
        print(event.name,logica.fin())
        # Verificar si la tecla es una letra y quedan vidas
        if event.name.isalpha()  and logica.vidas > 0 and not logica.fin():
            letra  = event.name.lower()
            if letra in abecedario and letra not in teclas_presionadas: #coprobamos si esta en el abecadario y no esta en las selcionadas
                teclas_presionadas.add(letra)
                letraR.set("LETRA:"+letra)
                if logica.jugar(letra):
                    resultado.set(logica.resultado)
                    if logica.fin():
                        ventana.after(0, win)
                        database.partida(logica.jugador,palabra[0],True)
                else :
                    ahorcado()
                    if logica.fin():
                        ventana.after(0, lose)
                        database.partida(logica.jugador,palabra[0],False)


    def ahorcado():
        global img_tk
        image = Image.open(f"resorcues/ahorcado{logica.vidas+1}.png")
        img_tk = ImageTk.PhotoImage(image)
        lAhorcado.config(image=img_tk)

    def win():
        menu = Toplevel()
        menu.title("GANA")
        img = PhotoImage(file="resorcues/win.gif")
        label = tk.Label(menu, image=img)
        label.pack()
        tk.Label(menu, text="HAS GANADO").pack()
        menu.resizable(False, False)
        ajustarVentana(menu,300,250)
        menu.mainloop()

    def lose():
        menu = Toplevel()
        menu.title("VAYA MATAO")
        img = PhotoImage(file="resorcues/lose.gif")
        label = tk.Label(menu, image=img)
        label.pack()
        tk.Label(menu, text="VAYA MATAO").pack()
        menu.resizable(False, False)
        ajustarVentana(menu, 300, 250)
        menu.mainloop()

    breset = Button(frame, text="RESET", bg="RED", command=reinit, font=("Arial", 30), fg="white")
    breset.place(x=1120, y=100)
    keyboard.on_press(manejar_presion)

    ventana.mainloop()

juego("Paco","f")