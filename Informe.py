import sqlite3
import MainMenu

def generarInforme():
    connection = sqlite3.connect('resultados.db')
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='resultados'")
    table_exists = cursor.fetchone()

    if not table_exists:
        print("No se encontró la tabla 'resultados'. Juegue una partida para empezar a guardar los datos.")
        connection.close()
        MainMenu.mainMenu('PJ')
        return

    cursor.execute('SELECT nombre, resultado FROM resultados')
    resultados = cursor.fetchall()
    connection.close()

    import matplotlib.pyplot as plt

    resultados_cpu = [resultado[1] for resultado in resultados if resultado[1] == 'cpu']
    resultados_jugador = [resultado[1] for resultado in resultados if resultado[1] != 'cpu']

    labels = ['CPU', 'Jugador']
    sizes = [len(resultados_cpu), len(resultados_jugador)]
    colors = ['lightcoral', 'lightskyblue']
    explode = (0.1, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Resultados de partidas')
    plt.show()
