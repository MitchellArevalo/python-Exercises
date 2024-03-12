import numpy as np
import random
from colored import fg
import MainMenu

def asignarNombreJugador():
    nombre_jugador = input("\nIngrese su nombre: ")
    MainMenu.mainMenu(nombre_jugador)
    
def asignarBarcos(nombre_jugador):
    colorUsuario = fg('blue')
    redColor = fg('light_red')
    filas = [ '°', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    columnas = list(range(0, 11))
    tablero_jugador = np.full((11, 11), "O")
    for i in range(11):
        tablero_jugador[i][0] = filas[i]
    for j in range(11):
        if j > 0:
            tablero_jugador[0][j] = str(columnas[j-1])

    barcos_restantes = 10
   
    print(redColor +f"\nTablero de {nombre_jugador}:\n")
    print( redColor +f'Barcos restantes {barcos_restantes}')
    print(colorUsuario + '----------------------PJ----------------------')
    print(tablero_jugador)
    
    barcos_colocados = 0
    while barcos_colocados < 10:
        fila = input("\nIngrese la fila donde desea ubicar su barco: (A, B, C, D, E, F, G, H, I, J,)")
        filanum = -1

        if fila.upper() == 'A':
            filanum = 1
        elif fila.upper() == 'B':
            filanum = 2
        elif fila.upper() == 'C':
            filanum = 3
        elif fila.upper() == 'D':
            filanum = 4
        elif fila.upper() == 'E':
            filanum = 5
        elif fila.upper() == 'F':
            filanum = 6
        elif fila.upper() == 'G':
            filanum = 7
        elif fila.upper() == 'H':
            filanum = 8
        elif fila.upper() == 'I':
            filanum = 9
        elif fila.upper() == 'J':
            filanum = 10
        else:
            print(f'ERROR: La letra {fila} no está permitida,intentalo nuevamente')
            continue
        
        columna = input("\nIngrese la columna donde desea ubicar su barco: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)")
        
            
        if not columna.isdigit():
            print("\nERROR: Debe ingresar números enteros para la columna")
            continue
        
        columna = int(columna)

        if filanum < 0 or filanum > 10 or columna < 0 or columna > 9:
            print("\nERROR: Coordenadas inválidas")
            continue
        
        if tablero_jugador[filanum, columna+1] != "O":
            print("\nERROR: Ubicación ocupada, seleccione otra")
            continue
       
        
        tablero_jugador[filanum, columna+1] = "B"
        
        barcos_colocados += 1
        barcos_restantes += -1
       
        print(redColor +f"\nTablero de {nombre_jugador}:\n")
        print( redColor +f'Barcos restantes {barcos_restantes}')
        print(colorUsuario + '----------------------PJ----------------------')
        print(tablero_jugador)
        
    return tablero_jugador

def generarBarcosCPU():
    
    colorOponente = fg('purple_4a')
    filasOponente = [ '°', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    columnasOponente = list(range(0, 11))
    tablero_oponente = np.full((11, 11), "O")
    for i in range(11):
        tablero_oponente[i][0] = filasOponente[i]
    for j in range(11):
        if j > 0:
            tablero_oponente[0][j] = str(columnasOponente[j-1])
    
    barcos_colocados = 0
    while barcos_colocados < 10:
        
        fila = random.randint(1, 10)
        
        columna = random.randint(1, 10)

        if fila < 0 or fila > 10 or columna < 0 or columna > 10:
            continue
        
        if tablero_oponente[fila, columna] != "O":
            continue
        
        tablero_oponente[fila, columna] = "B"
        
        barcos_colocados += 1
        
    return tablero_oponente
