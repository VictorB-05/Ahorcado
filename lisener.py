import keyboard

# Almacenar teclas presionadas para evitar duplicados mientras se mantiene la tecla
teclas_presionadas = set()

def manejar_presion(event):
    # Verificar si la tecla es una letra y no está en teclas_presionadas
    if event.name.isalpha() and event.name not in teclas_presionadas:
        teclas_presionadas.add(event.name)  # Agregar al conjunto
        print(f"Tecla presionada: {event.name}")

def manejar_liberacion(event):
    # Remover la tecla del conjunto al liberarla
    if event.name in teclas_presionadas:
        teclas_presionadas.remove(event.name)
        print(f"Tecla liberada: {event.name}")

# Registrar eventos de presionar y liberar teclas
keyboard.on_press(manejar_presion)
keyboard.on_release(manejar_liberacion)

# Mantener el programa activo
print("Presiona teclas (esc para salir).")
keyboard.wait("esc")  # Salir al presionar 'esc'