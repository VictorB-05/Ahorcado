from pynput import keyboard
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

# Escucha eventos de teclado
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()