import sqlite3
import openpyxl
import os
import random
from tkinter import Tk, filedialog

def obtener_lista_carreras(cursor):
    cursor.execute('SELECT id_carrera, nombre FROM carreras')
    carreras = cursor.fetchall()
    return carreras

def generar_informes(cursor):
    try:
        carreras = obtener_lista_carreras(cursor)

        print("Seleccione una carrera:")
        for id_carrera, nombre_carrera in carreras:
            print(f"{id_carrera}. {nombre_carrera}")

        seleccion_carrera = int(input("Ingrese el número de la carrera: "))

        nombre_carrera = next((nombre for id_carrera, nombre in carreras if id_carrera == seleccion_carrera), None)

        cursor.execute('''
            SELECT nombre, AVG(nota) as promedio_general
            FROM estudiantes
            JOIN notas ON estudiantes.id_estudiante = notas.estudiante_id
            GROUP BY estudiantes.id_estudiante
            ORDER BY promedio_general DESC
            LIMIT 5
        ''')
        mejores_estudiantes_general = cursor.fetchall()
        print("Los 5 mejores estudiantes en general:")
        for estudiante in mejores_estudiantes_general:
            print(f"{estudiante[0]} - Promedio: {estudiante[1]:.1f}")
            
        if nombre_carrera is not None:
            cursor.execute('''
                SELECT estudiantes.nombre AS estudiante, carreras.nombre AS carrera, notas.nota
                FROM notas
                JOIN estudiantes ON notas.estudiante_id = estudiantes.id_estudiante
                JOIN carreras ON estudiantes.carrera_id = carreras.id_carrera
                WHERE carreras.id_carrera = ?
                ORDER BY notas.nota DESC
            ''', (seleccion_carrera,))
            notas_carrera = cursor.fetchall()

            print("\nInforme de notas por carrera:")
            print("Estudiante\t\tCarrera\t\tNota")
            for estudiante, _, nota in notas_carrera:
                print(f"{estudiante}\t\t{nombre_carrera}\t\t{nota:.1f}")

        else:
            print("Carrera no válida. Por favor, ingrese un número de carrera válido.")

        cursor.execute('''
            SELECT AVG(nota) as promedio_general
            FROM notas
        ''')
        promedio_general = cursor.fetchone()[0]
        print(f"Promedio general: {promedio_general:.3f}")
        
        cursor.execute('''
            SELECT carreras.nombre as carrera, AVG(notas.nota) as promedio_carrera
            FROM estudiantes
            JOIN notas ON estudiantes.id_estudiante = notas.estudiante_id
            JOIN carreras ON estudiantes.carrera_id = carreras.id_carrera
            GROUP BY carreras.id_carrera
        ''')
        promedio_por_carrera = cursor.fetchall()
        print("Promedio por carrera:")
        
        for promedio_carrera in promedio_por_carrera:
            print(f"{promedio_carrera[0]} - Promedio: {promedio_carrera[1]:.3f}")
            
    except Exception as e:
        print(f"Error al generar informes: {e}")
