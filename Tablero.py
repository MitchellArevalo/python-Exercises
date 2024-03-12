import numpy as np
import random
from colored import fg
import GuardarResultados
import MainMenu

def showBoard(pjBoard, pcBoard, nombre_jugador):
    colorPj = fg('purple_4a')
    colorOponente = fg('light_red')
    greenColor = fg('green')
    
    filas = [ '°', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    columnas = list(range(0, 11))
    tableroCPU_Hide = np.full((11, 11), "O")
    for i in range(11):
        tableroCPU_Hide[i][0] = filas[i]
    for j in range(11):
        if j > 0:
            tableroCPU_Hide[0][j] = str(columnas[j-1])
    
    conteoBarcosCPU = 0
    conteoBarcosPJ = 0
    
    print(colorOponente + '\n Tablero de la PC')
    print(f"\nBarcos hundidos: {conteoBarcosCPU}\n")
    print(tableroCPU_Hide)
    # print('Tablero real')
    # print(pcBoard)
    print('\n=========================================================')
    print(colorPj + f"\nTablero de {nombre_jugador}:\n")
    print(f"\nBarcos hundidos: {conteoBarcosPJ}\n")
    print(pjBoard)
    
    cpuTurn = False
    terminado = 0
    while terminado < 1:
        print(colorOponente + '\n Tablero de la PC')
        print(f"\nBarcos hundidos: {conteoBarcosCPU}\n")
        print(tableroCPU_Hide)
        print('Tablero real')
        print(pcBoard)
        print('\n=========================================================')
        print(colorPj + f"\nTablero de {nombre_jugador}:\n")
        print(f"\nBarcos hundidos: {conteoBarcosPJ}\n")
        print(pjBoard)
        
        if cpuTurn == False: #Turno del jugador
            fila = input("\nIngrese la fila donde desea atacar el barco enemigo: (A, B, C, D, E, F, G, H, I, J,)")
            
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
            
            columna = input("\nIngrese la columna donde desea atacar el barco enemigo: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)")
        
            
            if not columna.isdigit():
                print(greenColor + "\nERROR: Debe ingresar números enteros para la columna")
                continue
            
            columna = int(columna)

            if filanum < 0 or filanum > 10 or columna < 0 or columna > 9:
                print(greenColor + "\nERROR: Coordenadas inválidas")
                continue
            
            if pcBoard[filanum, columna+1] == "X":
                print(greenColor + "\nDisparo Invalidado")
                continue
               
            if pcBoard[filanum, columna+1] == "O":
                cpuTurn = True
                pcBoard[filanum, columna+1] = "X"
                tableroCPU_Hide[filanum, columna+1] = "X"
                print(greenColor + "\nDisparo Fallado")
            
            if pcBoard[filanum, columna+1] == "B":
                cpuTurn = True    
                pcBoard[filanum, columna+1] = "D"
                tableroCPU_Hide[filanum, columna+1] = "D"
                print(greenColor + "\nImpacto")
                conteoBarcosPJ += 1
                
        elif cpuTurn == True:
            fila 
            
            filanum = random.randint(1, 10)
            
            columna = random.randint(1, 10)

            if filanum < 0 or filanum > 9 or columna < 0 or columna > 9:
                continue
            
            if pjBoard[filanum, columna+1] == "X" or pjBoard[filanum, columna+1] == "D":
                continue
            
            if pjBoard[filanum, columna+1] == "O":
                pjBoard[filanum, columna+1] = "X"
                print(greenColor + "\n ¡Disparo Enemigo Fallado!")
                cpuTurn = False
            
            if pjBoard[filanum, columna+1] == "B":
                pjBoard[filanum, columna+1] = "D"
                print(greenColor + "\nImpacto Enemigo")
                conteoBarcosCPU += 1
                cpuTurn = False    
            
        if conteoBarcosCPU == 10:
            print(greenColor + '\nLa CPU ha ganado\n')
            GuardarResultados.guardarResultado(nombre_jugador, 'cpu')
            terminado = 1
        elif conteoBarcosPJ == 10:
            print(greenColor + '\nFelicidades, has ganado la partida\n')
            GuardarResultados.guardarResultado(nombre_jugador, 'jugador')
            terminado = 1

    MainMenu.mainMenu(nombre_jugador)
    