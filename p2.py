# -*- coding: utf-8 -*-
"""

@author:  Yanin Alejandra Escobar Aguas (1004616271)
          Juan Felipe Sierra Olaya (1114239077)
          Jennifer Reyes Arboleda (1004614696)


# Proyecto Euler: the sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. 
  Find the sum of all the primes below two million.
"""

# -- IMPORTS --
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def suma_primos(n):
    suma = 0
    for i in range(2, n):
        if es_primo(i):
            suma += i
    return suma

def main():
    limite = 2000000
    print("Por favor espere mientras se realiza el calculo")
    resultado = suma_primos(limite)
    numero_formateado = "{:,}".format(resultado)
    print("La suma de todos los números primos por debajo de", limite, "es:", numero_formateado)
