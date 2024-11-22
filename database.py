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
        frutas = [("Manzana", "fruta"), ("Platano", "fruta"), ("Naranja", "fruta"),
                  ("Fresa", "fruta"), ("Kiwi", "fruta"), ("Uva", "fruta"),
                  ("Pera", "fruta"), ("Mango", "fruta"), ("Melon", "fruta"),
                  ("Sandia", "fruta")]

        conceptos = [("Algoritmo", "informatica"), ("Compilador", "informatica"),
                     ("Base de Datos", "informatica"), ("Clase", "informatica"),
                     ("Objeto", "informatica"), ("Framework", "informatica"),
                     ("Interprete", "informatica"), ("Script", "informatica"),
                     ("Bit", "informatica"), ("Nodo", "informatica")]

        nombres = [("Victor", "nombre"), ("Dani", "nombre"),
                     ("Rodri", "nombre"), ("Jose Manuel", "nombre"),
                     ("Andrea", "nombre"), ("Patri", "nombre"),
                     ("Carla", "nombre"), ("Ivan", "nombre"),
                     ("Alberto", "nombre"), ("Lucas", "nombre"),
                     ("Jose Ignacio", "nombre"), ("Pablo", "nombre"),
                     ("Antonio", "nombre"), ("Raul", "nombre"),
                     ("Rafa", "nombre"), ("Martin", "nombre"),
                     ("Miguel", "nombre"), ("Nico", "nombre"),
                     ("Guille", "nombre"), ("Roberto", "nombre"),
                     ("Alexandro", "nombre"), ("Manuel", "nombre"),
                     ("Sergio", "nombre"), ("Alberto", "nombre"), ("Javier", "nombre")]

        # Inserción de datos en la tabla
        cursor.executemany("INSERT INTO palabra (palabra, tipo) VALUES (?, ?)", frutas)
        cursor.executemany("INSERT INTO palabra (palabra, tipo) VALUES (?, ?)", conceptos)
        cursor.executemany("INSERT INTO palabra (palabra, tipo) VALUES (?, ?)", nombres)
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
    cursor.execute("INSERT INTO partida (ganada,idJugador,idPalabra) VALUES (?,?,?)",(ganar,id[0],palabra))
    conn.commit()

def jugador(jugador):
    conn = sqlite3.connect('Registro.db')

    cursor = conn.cursor()
    cursor.execute("SELECT id FROM jugador WHERE nombre = ?", (jugador,))
    id = cursor.fetchone()
    return id

def insertar(jugador):
    conn = sqlite3.connect('Registro.db')

    cursor = conn.cursor()
    cursor.execute("INSERT INTO jugador (nombre) VALUES (?)", (jugador,))
    conn.commit()

def datos(id):
    conn = sqlite3.connect('Registro.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM partida WHERE idJugador = ?", id)
    rel = cursor.fetchall()
    return rel