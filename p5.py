# -*- coding: utf-8 -*-
"""

@author: Yanin Alejandra Escobar Aguas (1004616271)
         Juan Felipe Sierra Olaya (1114239077)
         Jennifer Reyes Arboleda (1004614696)

# Gráficas: Crear un submenú con:
  a. Una opción para generar los datos de dos ecuaciones trigonométricas con
  dominio entre [-2pi, 2pi], en 2 dimensiones, guardando la información (datos),
  incluyendo títulos, ejes, y leyenda, en un archivo, utilizando funciones.
  
  b. Una opción para generar los datos de una ecuación en coordenadas polares,
  guardando información de títulos.
  
  c. Una opción que me permita leer los datos guardados sobre las ecuaciones en
  dos dimensiones y generar la gráfica requerida, en una sola gráfica, utilizando
  funciones. Todos los títulos y encabezados se deben leer desde el archivo.
  
  d. Una opción que permita leer los datos guardados sobre la ecuación polar y
  generar la gráfica requerida, utilizando funciones. Todos los títulos y
  encabezados se deben leer desde el archivo.
  Deben entregar los 2 archivos con los datos generados.
"""
# -- IMPORTS --
import math
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Función para generar los datos de las ecuaciones trigonométricas
def generar_datos_trigonometricas():
    x = []
    y1 = []
    y2 = []

    for i in range(-628, 629, 1):
        rad = i / 100.0
        x.append(rad)

        y1.append(math.sin(rad))
        y2.append(math.cos(rad))

    return x, y1, y2

# Función para generar los datos de la ecuación polar
def generar_datos_polar():
    theta = []
    r = []

    for i in range(-628, 629, 1):
        rad = i / 100.0
        theta.append(rad)
        r.append(math.cos(3 * rad))

    return theta, r

# Función para guardar los datos en un archivo CSV con un nombre único basado en la fecha y hora actual
def guardar_datos_en_csv(titulo, encabezados, datos):
    fecha_hora_actual = datetime.now().strftime("%Y%m%d%H%M%S")
    nombre_archivo = f"{titulo}_{fecha_hora_actual}.csv"
    
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(encabezados)
        writer.writerows(datos)
    
    return nombre_archivo

# Función para leer los datos desde un archivo CSV
def leer_datos_desde_csv(archivo_csv):
    with open(archivo_csv, 'r') as archivo:
        reader = csv.reader(archivo)
        encabezados = next(reader)
        datos = list(reader)
    
    return encabezados, datos

# Función para generar la gráfica de las ecuaciones en dos dimensiones
def generar_grafica_dos_dimensiones(encabezados, datos):
    x = [float(dato[0]) for dato in datos]
    y1 = [float(dato[1]) for dato in datos]
    y2 = [float(dato[2]) for dato in datos]

    plt.plot(x, y1, label=encabezados[1])
    plt.plot(x, y2, label=encabezados[2])

    plt.title(encabezados[0])
    plt.xlabel(encabezados[1])
    plt.ylabel(encabezados[2])
    plt.legend()

    plt.show()

# Función para generar la gráfica de la ecuación polar
def generar_grafica_polar(encabezados, datos):
    theta = [float(dato[0]) for dato in datos]
    r = [float(dato[1]) for dato in datos]

    plt.polar(theta, r)

    plt.title(encabezados[0])

    plt.show()

# Submenú
def mostrar_submenu():
    while True:
        print("Submenú:")
        print("a. Generar datos de ecuaciones trigonométricas en 2D y guardar en archivo")
        print("b. Generar datos de ecuación en coordenadas polares y guardar en archivo")
        print("c. Leer datos de ecuaciones en 2D desde archivo y generar gráfica")
        print("d. Leer datos de ecuación polar desde archivo y generar gráfica")
        print("e. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == 'a':
            x, y1, y2 = generar_datos_trigonometricas()
            datos = list(zip(x, y1, y2))
            encabezados = ['X', 'Y1', 'Y2']
            archivo_csv = guardar_datos_en_csv('datos_trigonometricas', encabezados, datos)
            print(f"Datos de ecuaciones trigonométricas generados y guardados en el archivo: {archivo_csv}")
        elif opcion == 'b':
            theta, r = generar_datos_polar()
            datos = list(zip(theta, r))
            encabezados = ['Theta', 'R']
            archivo_csv = guardar_datos_en_csv('datos_polar', encabezados, datos)
            print(f"Datos de ecuación polar generados y guardados en el archivo: {archivo_csv}")
        elif opcion == 'c':
            archivo_csv = input("Ingrese el nombre del archivo CSV: ")
            encabezados, datos = leer_datos_desde_csv(archivo_csv)
            generar_grafica_dos_dimensiones(encabezados, datos)
        elif opcion == 'd':
            archivo_csv = input("Ingrese el nombre del archivo CSV: ")
            encabezados, datos = leer_datos_desde_csv(archivo_csv)
            generar_grafica_polar(encabezados, datos)
        elif opcion == 'e':
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

def main():
    mostrar_submenu()

