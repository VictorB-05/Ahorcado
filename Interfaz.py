import sys
import tkinter as tk
from tkinter import PhotoImage, Toplevel, Button
import keyboard
import Logica
import database
from PIL import Image, ImageTk

abecedario = [chr(i) for i in range(97, 123)]
abecedario = abecedario + ['ñ'] # abecedario
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

ventana = tk.Toplevel()
ventana.resizable(False,False)
ventana.title("Ahorcado")
frame = tk.Frame(ventana, bg="lightblue")
frame.pack(expand=True, fill="both")
frame.pack_propagate(False)
ajustarVentana(ventana,800,1400)

letraR = tk.StringVar()
palabra = ""
logica = Logica.Logica

img_path = "resorcues/ahorcado7.png"
image = Image.open(img_path)
img_tk = ImageTk.PhotoImage(master= ventana,image=image)
resultado = tk.StringVar()
tematica = ""
letras = tk.StringVar()


def juego(jugador,tematicaAux):
    global teclas_presionadas, logica, img_tk, resultado, tematica,letras,palabra
    tematica = tematicaAux
    palabra = database.palabras(tematica)
    logica = Logica.Logica(jugador, palabra[1])

    letraR.set("LETRA: _")

    resultado.set(logica.pResultado())

    label1 = tk.Label(frame, textvariable=letraR, font=("Arial", 30), bg="lightblue")
    label1.place(x=390, y=650, height=100, width=200)

    rel = tk.Label(frame, textvariable=resultado, font=("Arial", 30), bg="lightblue")
    rel.place(x=600, y=650, height=100, width=420)

    lAhorcado = tk.Label(frame, image=img_tk)
    lAhorcado.image = img_tk
    lAhorcado.place(x=400, y=20)
    nombre = tk.StringVar()
    nombre.set(logica.jugador)
    lNombre = tk.Label(frame, textvariable=nombre, font=("Arial", 25), bg="lightblue")
    lNombre.place(x=10, y=100)

    letras.set("LETRAS:")
    letrasL = tk.Label(frame, textvariable=letras, font=("Arial", 25), bg="lightblue")
    letrasL.place(x=10, y=150)

    tema = tk.Label(frame, text=tematica, font=("Arial", 25), bg="lightblue")
    tema.place(x=10, y=200)

    def reinit():
        global teclas_presionadas, palabra, logica, tematica, letras
        palabra = database.palabras(tematica)
        logica = Logica.Logica(jugador,palabra[1])
        letraR.set("LETRA: _")
        letras.set("LETRAS:")
        resultado.set(logica.pResultado())
        ahorcado()
        teclas_presionadas = set()

    def manejar_presion(event):
        global teclas_presionadas, palabra, logica, letras
        # Verificar si la tecla es una letra y quedan vidas
        if event.name.isalpha()  and logica.vidas > 0 and not logica.fin():
            letra  = event.name.lower()
            if letra in abecedario and letra not in teclas_presionadas: #coprobamos si esta en el abecadario y no esta en las selcionadas
                teclas_presionadas.add(letra)
                letraR.set("LETRA:"+letra)
                if logica.jugar(letra):
                    resultado.set(logica.pResultado())
                    if logica.fin():
                        win()
                        database.partida(logica.jugador,palabra[0],True)
                else :
                    ahorcado()
                    letras.set(f"{letras.get()} {letra}")
                    if logica.fin():
                        lose()
                        database.partida(logica.jugador,palabra[0],False)

    def ahorcado():
        global img_tk
        image = Image.open(f"resorcues/ahorcado{logica.vidas+1}.png")
        img_tk = ImageTk.PhotoImage(master=ventana,image=image)
        lAhorcado.config(image=img_tk)

    def win():
        menu = Toplevel()
        menu.title("GANA")
        menu.config(bg="lightblue")
        img = PhotoImage(file="resorcues/win.gif")
        label = tk.Label(menu, image=img,bg="lightblue")
        label.pack()
        tk.Label(menu, text="HAS GANADO",font=("Arial", 20), bg="lightblue").pack()
        menu.resizable(False, False)
        ajustarVentana(menu,300,250)
        label.img = img

    def lose():
        global palabra
        menu = Toplevel()
        menu.title("PEDER")
        menu.config(bg="lightblue")
        img = PhotoImage(file="resorcues/lose.gif")
        label = tk.Label(menu, image=img, bg="lightblue")
        label.pack()
        tk.Label(menu, text=f"VAYA MATAO\n Palabra {palabra[1]}", font=("Arial", 20), bg="lightblue").pack()
        menu.resizable(False, False)
        ajustarVentana(menu,300,250)
        label.img = img

    def salir():
        global ventana, keyboard
        if ventana:
            ventana.destroy()
            ventana = None
        keyboard.unhook_all()
        sys.exit(0)


    breset = Button(frame, text="RESET", bg="RED", command=reinit, font=("Arial", 30), fg="white")
    breset.place(x=1120, y=300,width=200)
    bsalir = Button(frame, text="SALIR", bg="RED", command=salir, font=("Arial", 30), fg="white")
    bsalir.place(x=1120, y=100,width=200)
    keyboard.on_press(manejar_presion)
    ventana.mainloop()




# juego("Paco","f")