import keyboard

# Almacenar teclas presionadas para solo ser presionadas una vez
teclas_presionadas = set()

palabra = "manzana"
to_array = [char.lower() for char in palabra]  # Convertir a minúsculas para evitar problemas con mayúsculas
resultado = ["_" for _ in palabra]

# teclas presionadas
def manejar_presion(event):
    if event.name.isalpha() and event.name.lower() not in teclas_presionadas:
        teclas_presionadas.add(event.name.lower())
        actualizar_resultado()

# Función para actualizar el resultado en base a teclas presionadas
def actualizar_resultado():
    global resultado
    for i, char in enumerate(to_array):
        if char in teclas_presionadas:
            resultado[i] = palabra[i]
    print(" ".join(resultado))

# Asignar el manejador al evento de soltar tecla
keyboard.on_release(manejar_presion)

print(" ".join(resultado))

# Mantener el programa en ejecución
keyboard.wait("esc")