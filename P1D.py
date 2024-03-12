import sqlite3
import openpyxl
import os
import random
from tkinter import Tk, filedialog

def ingresar_registro_interactivo(cursor):
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = cursor.fetchall()

        print("Tablas disponibles:")
        for i, tabla in enumerate(tablas, start=1):
            print(f"{i}. {tabla[0]}")

        seleccion_tabla = int(input("Seleccione la tabla (número): "))

        tabla_seleccionada = tablas[seleccion_tabla - 1][0]

        cursor.execute(f"PRAGMA table_info({tabla_seleccionada})")
        columnas = cursor.fetchall()

        valores = []
        for columna in columnas:
            valor = input(f"Ingrese el valor para '{columna[1]}' ({columna[2]}): ")
            valores.append(valor)

        cursor.execute(f"INSERT INTO {tabla_seleccionada} VALUES ({', '.join(['?']*len(valores))})", valores)

        print("Registro ingresado correctamente.")
    except Exception as e:
        print(f"Error al ingresar registro: {e}")
