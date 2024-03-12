import random
import sqlite3
import MainMenu

def generarBaseDeDatosConDatos(nombre_jugador):
    connection = sqlite3.connect('resultados.db')
    cursor = connection.cursor()

    # Crear la tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            resultado TEXT
        )
    ''')

    cursor.execute('SELECT COUNT(*) FROM resultados')
    registros_actuales = cursor.fetchone()[0]

    if registros_actuales < 10:
        while registros_actuales < 10:
            resultado = 'cpu' if random.randint(0, 1) == 0 else 'jugador'
            cursor.execute('INSERT INTO resultados (nombre, resultado) VALUES (?, ?)', (nombre_jugador, resultado))
            registros_actuales += 1
    else:
        print('Lo sentimos, ya generó los primeros 10 registros aleatorios, por favor juegue para seguir guardando información')
    connection.commit()
    connection.close()

    MainMenu.mainMenu(nombre_jugador)
