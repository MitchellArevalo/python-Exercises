# -*- coding: utf-8 -*-
"""

@author: Yanin Alejandra Escobar Aguas (1004616271)
         Juan Felipe Sierra Olaya (1114239077)
         Jennifer Reyes Arboleda (1004614696)

Menú para acceder a los diferentes programas: P1, P2, P3, P4, P5
"""
import p1
import p2
import p3
import p4
import p5

def prints(texto):
    ancho = 80
    print("+" + "-" * ancho + "+")
    print("|" + " " * ancho + "|")
    lineas = texto.split('\n')
    for linea in lineas:
        linea_len = len(linea)
        for i in range(0, linea_len, 78):
            print(f"| {linea[i:i+78].ljust(78)} |")
    print("|" + " " * ancho + "|")
    print("+" + "-" * ancho + "+")


def printp(text):
    ancho = 80
    print("+" + "-" * ancho + "+")
    print("|" + " " * ancho + "|")
    lineas = text.split('\n')
    for linea in lineas:
        linea_len = len(linea)
        for i in range(0, linea_len, 78):
            print(f"| {linea[i:i+78].ljust(78)} |")
    print("|" + " " * ancho + "|")
    print("+" + "-" * ancho + "+")
    
def styled_input(mensaje):
    ancho = 62
    print(f"| {mensaje.ljust(58)}: |")
    return input(f"• {''.rjust(ancho//99,)}: ")

#CUERPO DEL MENÚ
def menu():
    prints("Bienvenido a la resolución del taller 2 de Algoritmos y Programación.\nPor favor digite el número de la opción que desea para acceder al programa correspondiente")

    while True:
        try:
            prints("1. Problema 1: Programa para realizar las operaciones básicas entre matrices: suma, resta y multiplicación\n-\n2. Problema 2: Proyecto Euler punto 10: the sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.\n-\n3. Problema 3: Proyecto Euler punto 1. In the 20×20 grid below, four numbers along a diagonal linea have been marked in red.\n-\n4. Problema 4: Manejo y estadísticas de datos de estudiantes\n-\n5. Problema 5: Generación y graficación de ecuaciones trigonométricas y polares\n-\n6. Salir")
            opcion = int(styled_input("Ingrese el número de la opción que desea: "))
            if opcion not in range(1,7):
                prints("\033[31m¡La opción ingresada no es válida, por favor ingrese un valor entre 1 y 6!\033[0m")
                continue
            else:
                if opcion == 1:
                   p1.main()
                elif opcion == 2:
                    p2.main()
                elif opcion == 3:
                    p3.main()
                elif opcion == 4:
                    p4.main()
                elif opcion == 5:
                    p5.main()
                else:
                    prints("\033[32m¡Gracias por utilizar el programa!\033[0m")
                    break
        except ValueError:
            prints("\033[31m¡El valor ingresado no es un número entero!\033[0m")
            continue


if __name__ == "__main__":
    menu()
