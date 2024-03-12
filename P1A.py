import sqlite3
import openpyxl
import os
import random
from tkinter import Tk, filedialog

def crear_base_de_datos():
    try:
        conn = sqlite3.connect('base_de_datos_estudiantes.db')
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas_existen = cursor.fetchall()

        if tablas_existen:
            conn.close()
            print("La base de datos ya existe")
            return
        else:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS estudiantes (
                    id_estudiante INTEGER PRIMARY KEY,
                    nombre TEXT,
                    carrera_id INTEGER,
                    municipio_id INTEGER,
                    FOREIGN KEY (carrera_id) REFERENCES carreras(id_carrera),
                    FOREIGN KEY (municipio_id) REFERENCES municipios(id_municipio)
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS materias (
                    id_materia INTEGER PRIMARY KEY,
                    nombre TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS notas (
                    id_nota INTEGER PRIMARY KEY,
                    estudiante_id INTEGER,
                    materia_id INTEGER,
                    curso TEXT,
                    nota INTEGER,
                    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id_estudiante),
                    FOREIGN KEY (materia_id) REFERENCES materias(id_materia)
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS carreras (
                    id_carrera INTEGER PRIMARY KEY,
                    nombre TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS municipios (
                    id_municipio INTEGER PRIMARY KEY,
                    nombre TEXT,
                    departamento_id INTEGER,
                    FOREIGN KEY (departamento_id) REFERENCES departamentos(id_departamento)
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS departamentos (
                    id_departamento INTEGER PRIMARY KEY,
                    nombre TEXT
                )
            ''')

            insertar_municipios_departamentos(cursor)

            insertar_estudiantes_notas_materias_carreras(cursor)

            conn.commit()
            conn.close()

            print("La base de datos se ha creado con éxito")
            return
    except Exception as e:
        return f"Error al crear la base de datos: {e}"
     
def insertar_municipios_departamentos(cursor):
    try:
        archivo_excel = 'municipiosDepartamento.xlsx'
        wb = openpyxl.load_workbook(archivo_excel)
        sheet = wb.active

        for row in sheet.iter_rows(min_row=2, values_only=True):
            municipio, departamento = row

            cursor.execute('SELECT id_municipio FROM municipios WHERE nombre = ?', (municipio,))
            resultado_municipio = cursor.fetchone()

            if not resultado_municipio:
                
                cursor.execute('INSERT INTO municipios (nombre) VALUES (?)', (municipio,))
                cursor.execute('SELECT id_municipio FROM municipios WHERE nombre = ?', (municipio,))
                resultado_municipio = cursor.fetchone()

            cursor.execute('SELECT id_departamento FROM departamentos WHERE nombre = ?', (departamento,))
            resultado_departamento = cursor.fetchone()

            if not resultado_departamento:
                cursor.execute('INSERT INTO departamentos (nombre) VALUES (?)', (departamento,))
                cursor.execute('SELECT id_departamento FROM departamentos WHERE nombre = ?', (departamento,))
                resultado_departamento = cursor.fetchone()

            cursor.execute('UPDATE municipios SET departamento_id = ? WHERE id_municipio = ?', (resultado_departamento[0], resultado_municipio[0]))

    except Exception as e:
        print(f"Error al agregar datos de municipios iniciales desde Excel: {e}")
    finally:
        wb.close()

def insertar_estudiantes_notas_materias_carreras(cursor):
    for materia_nombre in ["Matemáticas", "Biología", "Historia", "Programación", "Química"]:
        cursor.execute('''
            INSERT INTO materias (nombre)
            VALUES (?)
        ''', (materia_nombre,))

    for carrera_nombre in ["Ingeniería", "Medicina", "Derecho"]:
        cursor.execute('''
            INSERT INTO carreras (nombre)
            VALUES (?)
        ''', (carrera_nombre,))
        
    cursor.execute('SELECT id_municipio FROM municipios')
    resultado_Municipios = cursor.fetchall()

    length_Municipios= len(resultado_Municipios)
    
    cursor.execute('SELECT id_carrera FROM carreras')
    resultado_carreras = cursor.fetchall()

    length_Carreras= len(resultado_carreras)
    
    cursor.execute('SELECT id_materia FROM materias')
    resultado_materias = cursor.fetchall()

    length_Materias= len(resultado_materias)
    
    secuencia = 0
    
    for _ in range(10):
        secuencia += 1
        nombre_estudiante = f"Estudiante_{secuencia}"
        carrera_id = random.randint(1, length_Carreras) 
        municipio_id = random.randint(1, length_Municipios)  

        cursor.execute('''
            INSERT INTO estudiantes (nombre, carrera_id, municipio_id)
            VALUES (?, ?, ?)
        ''', (nombre_estudiante, carrera_id, municipio_id))

        for _ in range(20):
            estudiante_id = cursor.lastrowid
            materia_id = random.randint(1, length_Materias)  
            curso = f"Curso_{secuencia}"
            nota = random.randint(0, 5)  

            cursor.execute('''
                INSERT INTO notas (estudiante_id, materia_id, curso, nota)
                VALUES (?, ?, ?, ?)
            ''', (estudiante_id, materia_id, curso, nota))
  