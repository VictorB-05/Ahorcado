class Logica:

    def __init__(self, jugador, palabra):
        self.jugador = jugador
        self.vidas = 6
        self.palabra = [char.lower() for char in palabra]
        self.resultado = ["_" for _ in palabra]

    def jugar(self, letra):
        acierto = False
        for i, char in enumerate(self.palabra):
            if letra == char:
                self.resultado[i] = letra
                acierto = True
        if not acierto:
            self.vidas -= 1
        return acierto

    def fin(self):
        if self.resultado == self.palabra:
            return True
        elif self.vidas == 0:
            return True
        return False

# import keyboard
# import database
#
# database.iniciar()
# # Almacenar teclas presionadas para solo ser presionadas una vez
# teclas_presionadas = set()
# vidas = 5
# to_array = None  # Convertir a minúsculas para evitar problemas con mayúsculas
# resultado = None
#
# def init():
#     palabra = database.palabras("F")
#     to_array = [char.lower() for char in palabra] # Convertir a minúsculas para evitar problemas con mayúsculas
#     resultado = ["_" for _ in palabra]
#     vidas = 5
#
# init()
#
# # teclas presionadas
# def manejar_presion(event):
#     if event.name.isalpha() and (event.name.lower() not in teclas_presionadas) and vidas > 0:
#         teclas_presionadas.add(event.name.lower())
#         actualizar_resultado(event.name.lower())
#
# # Función para actualizar el resultado en base a teclas presionadas
# def actualizar_resultado(letra):
#     global vidas
#     acierto = False
#     for i , char in enumerate(to_array):
#         if letra == char:
#             resultado[i] = letra
#             acierto = True
#     if not acierto:
#         vidas -= 1
#     # for i, char in enumerate(to_array):
#     #     if char in teclas_presionadas:
#     #         resultado[i] = palabra[i]
#     # print(" ".join(resultado))
#
# # Asignar el manejador al evento de soltar tecla
# keyboard.on_release(manejar_presion)
#
#
# # Mantener el programa en ejecución
# # keyboard.wait("esc")