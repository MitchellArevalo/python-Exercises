import sqlite3
import openpyxl
import os
import random
from tkinter import Tk, filedialog

def obtener_ruta_excel():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    archivo_excel = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=[("Excel files", "*.xlsx;*.xls")])
    root.destroy()
    return archivo_excel

def agregar_datos_desde_excel_municipios_departamentos(cursor):
    try:
        archivo_excel = obtener_ruta_excel()
        if not archivo_excel:
            print("Selección de archivo cancelada.")
            return

        wb = openpyxl.load_workbook(archivo_excel)
        sheet = wb.active
        cantidad_Municipios = 0
        cantidad_departamentos = 0

        for row in sheet.iter_rows(min_row=2, values_only=True):
            municipio, departamento = row

            cursor.execute('SELECT id_municipio FROM municipios WHERE nombre = ?', (municipio,))
            resultado_municipio = cursor.fetchone()

            if not resultado_municipio:
                cursor.execute('SELECT id_departamento FROM departamentos WHERE nombre = ?', (departamento,))
                resultado_departamento = cursor.fetchone()

                if not resultado_departamento:
                    cursor.execute('INSERT INTO departamentos (nombre) VALUES (?)', (departamento,))
                    cursor.execute('SELECT id_departamento FROM departamentos WHERE nombre = ?', (departamento,))
                    resultado_departamento = cursor.fetchone()
                    cantidad_departamentos += 1

                cursor.execute('INSERT INTO municipios (nombre, departamento_id) VALUES (?, ?)', (municipio, resultado_departamento[0]))
                cantidad_Municipios += 1

        print(f"{cantidad_Municipios} municipios agregados y {cantidad_departamentos} departamentos agregados correctamente.")
    except Exception as e:
        print(f"Error al agregar datos desde Excel: {e}")
    finally:
        wb.close()
 