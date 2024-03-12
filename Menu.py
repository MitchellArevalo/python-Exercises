import sqlite3
import P1A
import P1B
import P1C
import P1D
import P1E

def menu():

    while True:
        print("\nMenú:")
        print("a. Crear base de datos")
        print("b. Cargar datos desde Excel")
        print("c. Exportar datos a Excel")
        print("d. Ingresar registros")
        print("e. Generar informes")
        print("q. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == 'a':
            P1A.crear_base_de_datos()
        elif opcion == 'b':
            conn = sqlite3.connect('base_de_datos_estudiantes.db')
            cursor = conn.cursor()
            P1B.agregar_datos_desde_excel_municipios_departamentos(cursor)
            conn.commit()
            conn.close()
        elif opcion == 'c':
            conn = sqlite3.connect('base_de_datos_estudiantes.db')
            cursor = conn.cursor()
            P1C.exportar_a_excel(cursor)
            conn.commit()
            conn.close()
        elif opcion == 'd':
            conn = sqlite3.connect('base_de_datos_estudiantes.db')
            cursor = conn.cursor()
            P1D.ingresar_registro_interactivo(cursor)
            conn.commit()
            conn.close()
        elif opcion == 'e':
            conn = sqlite3.connect('base_de_datos_estudiantes.db')
            cursor = conn.cursor()
            P1E.generar_informes(cursor)
            conn.commit()
            conn.close()
        elif opcion == 'q':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
 
menu()