import sqlite3

def guardarResultado(nombre_jugador, resultado):
    connection = sqlite3.connect('resultados.db')  
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            resultado TEXT
        )
    ''')

    cursor.execute('INSERT INTO resultados (nombre, resultado) VALUES (?, ?)', (nombre_jugador, resultado))
    connection.commit()
    connection.close()
