# -*- coding: utf-8 -*-
"""

@author:  Yanin Alejandra Escobar Aguas (1004616271)
          Juan Felipe Sierra Olaya (1114239077)
          Jennifer Reyes Arboleda (1004614696)

# Cree un programa que realice operaciones básicas entre matrices (suma, resta y 
  multiplicación) con dimensiones aleatorias entre 3 y 10. El usuario selecciona la operación, y 
  se validan las dimensiones de las matrices ingresadas. La suma y la resta se ejecutan 
  mediante una función conjunta, mientras que la multiplicación se lleva a cabo con una 
  función separada. Los resultados se muestran a través de una tercera función que despliega 
  las tres matrices. Además, el programa permite trabajar con matrices no cuadradas.
"""

# -- IMPORTS --
import random

def generar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(1, 8))
        matriz.append(fila)
    return matriz

def sumar_restar_matrices(matriz1, matriz2, operacion):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if operacion == "suma":
                fila.append(matriz1[i][j] + matriz2[i][j])
            elif operacion == "resta":
                fila.append(matriz1[i][j] - matriz2[i][j])
        resultado.append(fila)
    return resultado

def multiplicar_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    columnas_matriz2 = len(matriz2[0])
    resultado = []
    for i in range(filas_matriz1):
        fila = []
        for j in range(columnas_matriz2):
            suma = 0
            for k in range(columnas_matriz1):
                suma += matriz1[i][k] * matriz2[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

def mostrar_matrices(matriz1, matriz2, resultado):
    print("Matriz 1:")
    for fila in matriz1:
        print(fila)
    print("Matriz 2:")
    for fila in matriz2:
        print(fila)
    print("Resultado:")
    for fila in resultado:
        print(fila)

def validar_dimensiones(filas, columnas):
    if filas < 3 or filas > 10 or columnas < 3 or columnas > 10:
        print("Las dimensiones de las matrices deben estar entre 3 y 10.")
        return False
    return True

def solicitar_dimensiones():
    filas = int(input("Ingrese el número de filas de las matrices: "))
    columnas = int(input("Ingrese el número de columnas de las matrices: "))
    return filas, columnas

def solicitar_operacion():
    operacion = input("Ingrese la operación a realizar (suma, resta, multiplicación): ")
    while operacion not in ["suma", "resta", "multiplicación"]:
        operacion = input("Operación inválida. Ingrese la operación a realizar (suma, resta, multiplicación): ")
    return operacion

def main():
    filas, columnas = solicitar_dimensiones()
    if not validar_dimensiones(filas, columnas):
        return
    matriz1 = generar_matriz(filas, columnas)
    matriz2 = generar_matriz(filas, columnas)
    operacion = solicitar_operacion()
    if operacion == "multiplicación":
        resultado = multiplicar_matrices(matriz1, matriz2)
    else:
        resultado = sumar_restar_matrices(matriz1, matriz2, operacion)
    mostrar_matrices(matriz1, matriz2, resultado)

