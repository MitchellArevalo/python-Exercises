import Asignaciones
import  Tablero
import Informe
import GenerarDatosAleatorios
import EliminarRegistros

def mainMenu(nombre_jugador):
    print("\nHola " + nombre_jugador + "!")
    print("\n----- Batalla Naval ------")
    print("\n----- Menú Principal -----")
    print("\n1. Introducir nombre del jugador.")
    print("2. Iniciar juego.")
    print("3. Generar reporte.")
    print("4. Generar datos aleatorios.")
    print("5. Eliminar todos los datos.")
    print("6. Cerrar programa.")

    opcion = input("\nEscriba el numero de una opcción: ")
    
    if opcion == '1':
        Asignaciones.asignarNombreJugador()

    elif opcion == '2':
        pcBoard = Asignaciones.generarBarcosCPU()
        pjBoard = Asignaciones.asignarBarcos(nombre_jugador)
        Tablero.showBoard(pjBoard, pcBoard, nombre_jugador)
        
    elif opcion == '3':
        Informe.generarInforme()
        
    elif opcion == '4':
        GenerarDatosAleatorios.generarBaseDeDatosConDatos(nombre_jugador)

    elif opcion == '5':
        EliminarRegistros.eliminar_archivo_resultados()
        mainMenu(nombre_jugador)
        
    elif opcion == '6':
        print("\nFin del Programa")

    else:
        print("\nERROR: Selección Inválida")
        mainMenu(nombre_jugador)
