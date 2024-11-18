import sqlite3

conn = sqlite3.connect('Registro.db')

# Crear un cursor
cursor = conn.cursor()

cursor.execute("IF NOT EXIST CREATE table jugador"
               "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "nombre TEXT)")

cursor.execute("IF NOT EXIST CREATE table palabra"
               "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "palabra TEXT,"
               "tipo TEXT)")

cursor.execute("IF NOT EXIST CREATE table partida"
               "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "ganada BOOLEAN,"
               "idJugador INTEGER,"
               "idPalabra INTEGER,"
               "FOREIGN KEY(idJugador) REFERENCES jugador(id),"
               "FOREIGN KEY(idPalabra) REFERENCES palabra(id))")