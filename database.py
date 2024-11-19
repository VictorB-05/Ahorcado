import sqlite3

conn = sqlite3.connect('Registro.db')

# Crear un cursor
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

rel = cursor.execute("SELECT * FROM palabra")

if rel is None:
    cursor.execute("")
    frutas = [("Manzana", "Fruta"), ("Plátano", "Fruta"), ("Naranja", "Fruta"),
              ("Fresa", "Fruta"), ("Kiwi", "Fruta"), ("Uva", "Fruta"),
              ("Pera", "Fruta"), ("Mango", "Fruta"), ("Melón", "Fruta"),
              ("Sandía", "Fruta")]

    conceptos = [("Algoritmo", "Informática"), ("Compilador", "Informática"),
                 ("Base de Datos", "Informática"), ("Clase", "Informática"),
                 ("Objeto", "Informática"), ("Framework", "Informática"),
                 ("Intérprete", "Informática"), ("Script", "Informática"),
                 ("Bit", "Informática"), ("Nodo", "Informática")]

    # Inserción de datos en la tabla
    cursor.executemany("INSERT INTO palabra (palabra, tipo) VALUES (?, ?)", frutas)
    cursor.executemany("INSERT INTO palabra (palabra, tipo) VALUES (?, ?)", conceptos)

    conn.commit()