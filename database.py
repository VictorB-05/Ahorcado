import sqlite3
import random


def iniciar():
    conn = sqlite3.connect('Registro.db')

    cursor = conn.cursor()

    cursor.execute("CREATE table IF NOT EXISTS jugador"
                   "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "nombre TEXT)")

    cursor.execute("CREATE table IF NOT EXISTS palabra"
                   "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "palabra TEXT,"
                   "tipo TEXT)")

    cursor.execute("CREATE table IF NOT EXISTS partida"
                   "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "ganada BOOLEAN,"
                   "idJugador INTEGER,"
                   "idPalabra INTEGER,"
                   "FOREIGN KEY(idJugador) REFERENCES jugador(id),"
                   "FOREIGN KEY(idPalabra) REFERENCES palabra(id))")

    conn.commit()

    cursor.execute("SELECT * FROM palabra")
    rel = cursor.fetchall()

    if len(rel) < 1:
        cursor.execute("")
        frutas = [("Manzana", "Fruta"), ("Platano", "Fruta"), ("Naranja", "Fruta"),
                  ("Fresa", "Fruta"), ("Kiwi", "Fruta"), ("Uva", "Fruta"),
                  ("Pera", "Fruta"), ("Mango", "Fruta"), ("Melon", "Fruta"),
                  ("Sandia", "Fruta")]

        conceptos = [("Algoritmo", "Informática"), ("Compilador", "Informática"),
                     ("Base de Datos", "Informática"), ("Clase", "Informática"),
                     ("Objeto", "Informática"), ("Framework", "Informática"),
                     ("Interprete", "Informática"), ("Script", "Informática"),
                     ("Bit", "Informática"), ("Nodo", "Informática")]

        # Inserción de datos en la tabla
        cursor.executemany("INSERT INTO palabra (palabra, tipo) VALUES (?, ?)", frutas)
        cursor.executemany("INSERT INTO palabra (palabra, tipo) VALUES (?, ?)", conceptos)

        conn.commit()
def palabras(tipo):
    conn = sqlite3.connect('Registro.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id,palabra FROM palabra WHERE tipo LIKE ?", (tipo + '%',))
    rel = cursor.fetchall()
    posicion = random.randint(0,len(rel))-1 #valor random de la palabra
    var = rel[posicion] # se coje el valor random de la base de datos
    return var

def partida(jugador,palabra,ganar):
    conn = sqlite3.connect('Registro.db')

    cursor = conn.cursor()
    cursor.execute("SELECT id FROM jugador WHERE nombre = ?", (jugador,))
    id = cursor.fetchone()
    print(id)
    cursor.execute("INSERT INTO partida (ganada,idJugador,idPalabra) VALUES (?,?,?)",(ganar,id[0],palabra))
    conn.commit()

def jugador (jugador):
    conn = sqlite3.connect('Registro.db')

    cursor = conn.cursor()
    cursor.execute("SELECT id FROM jugador WHERE nombre = ?", (jugador,))
    id = cursor.fetchone()
