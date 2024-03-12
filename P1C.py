import sqlite3
import openpyxl
import os
import random
from tkinter import Tk, filedialog

def exportar_a_excel(cursor):
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = cursor.fetchall()

        nombre_archivo = 'base_de_datos_exportada.xlsx'
        numero_consecutivo = 1

        while os.path.exists(nombre_archivo):
            nombre_archivo = f'base_de_datos_exportada_{numero_consecutivo}.xlsx'
            numero_consecutivo += 1

        wb = openpyxl.Workbook()

        for tabla in tablas:
            hoja = wb.create_sheet(title=tabla[0])

            cursor.execute(f'SELECT * FROM {tabla[0]}')
            datos = cursor.fetchall()

            hoja.append([desc[0] for desc in cursor.description])

            for fila in datos:
                hoja.append(fila)

        wb.remove(wb['Sheet'])

        wb.save(nombre_archivo)
        print(f"Datos exportados correctamente a {nombre_archivo}.")
    except Exception as e:
        print(f"Error al exportar datos a Excel: {e}")
