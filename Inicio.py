import sys
import tkinter as tk
import database

palabra = None

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
    global inico
    name = nombre.get("1.0", "end-1c").capitalize()
    if not len(name)==0:
        if not name[0]==" " :
            jugador = database.jugador(name)
            if jugador == None:
                database.insertar(name)
            if palabra != None:
                import Interfaz
                inico.withdraw()
                Interfaz.juego(name,palabra)

def datos():
    global inico, resultado
    name = nombre.get("1.0", "end-1c").capitalize()
    if not len(name) == 0:
        if not name[0] == " ":
            jugador = database.jugador(name)
            if jugador == None:
                resultado.config(state=tk.NORMAL)
                resultado.delete("1.0","end")
                resultado.insert(tk.INSERT,"Resultado:\n El usuario no existe en la DB")
                resultado.config(state=tk.DISABLED)
            else:
                datos = database.datos(jugador)
                lista = partidas(datos)
                resultado.config(state=tk.NORMAL)
                resultado.delete("1.0","end")
                resultado.insert(tk.INSERT, f"Resultado:\n GANAR {lista[0]}\n PERDER {lista[1]}")
                resultado.config(state=tk.DISABLED)

def partidas(datos):
    ganadas = 0
    perdidas = 0
    for list in datos:
        if list[1] == 1:
            ganadas+=1
        else:
            perdidas+=1
    debol = [ganadas,perdidas]
    return debol

def tematica(tem):
    global palabra
    fruta.config(bg="#4449fc")
    informaticos.config(bg="#4449fc")
    nombres.config(bg="#4449fc")
    palabra=tem
    if tem == "fruta":
        fruta.config(bg="red")
    elif tem == "informatica":
        informaticos.config(bg="red")
    elif tem == "nombre":
        nombres.config(bg="red")
database.iniciar()
inico = tk.Tk()
inico.resizable(False,False)
inico.title("Ahorcado")
frame = tk.Frame(inico, bg="lightblue")
frame.pack(expand=True, fill="both")
frame.pack_propagate(False)
ajustarVentana(inico,400,600)

label1 = tk.Label(frame, text="EL AHORCADO", font=("Arial", 20), bg="lightblue")
label1.place(x=190,y=10)

fruta = tk.Button(frame,text="fruta",bg="#4449fc",fg="#e1e8a5",font=("Comic Sans MS", 12),command=lambda: tematica("fruta"))
informaticos = tk.Button(frame,text="conpcetos informaticos",bg="#4449fc",fg="#e1e8a5",font=("Comic Sans MS", 12),command=lambda: tematica("informatica"))
nombres = tk.Button(frame,text="nombres",bg="#4449fc",fg="#e1e8a5",font=("Comic Sans MS", 12),command=lambda: tematica("nombre"))
fruta.place(x=90,y=70)
informaticos.place(x=200,y=70)
nombres.place(x=450,y=70)

label1 = tk.Label(frame, text="Introduce tu nombre:", font=("Arial", 15), bg="lightblue")
label1.place(x=200,y=110)
nombre = tk.Text(frame,
                   height = 1,
                   width = 20, font=("Vardana", 12))

nombre.place(x=200,y=140)

entrar = tk.Button(frame,text="Entrar",bg="#4449fc",command=guardar,fg="#e1e8a5",font=("Comic Sans MS", 20))
entrar.place(x=240,y=170)


resultado = tk.Text(frame,
                   height = 3,
                   width = 30, font=("Vardana", 12))
resultado.insert(tk.END,"Resultado:")
resultado.place(x=160,y=320)
resultado.config(state=tk.DISABLED)
entrar = tk.Button(frame,text="Buscar",bg="#4449fc",command=datos,fg="#e1e8a5",font=("Comic Sans MS", 12))
entrar.place(x=260,y=270)

inico.mainloop()