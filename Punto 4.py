# Crear programa que lea un valor n, y despliegue y calcule: 
# a) la suma y promedio de los primeros n pares, 
# b) suma y promedio de los primeros n impares,
# c) suma y promedio de los primeros n múltiplos de 3.

def calcular_suma_promedio(n, tipo):
    suma = 0
    contador = 0

    if tipo == 'pares':
        for i in range(1, n + 1):
            if i % 2 == 0:
                suma+= i
                contador+= 1
    elif tipo == 'impares':
        for i in range(1, n + 1):
            if i % 2 == 1:
                suma+= i
                contador+= 1
    elif tipo == 'multiplos de 3':
        for i in range(1, n + 1):
            if i % 3 == 0:
                suma+= i
                contador+= 1

    promedio = suma / contador if contador > 0 else 0
    return suma, promedio

n = -1 

while n < 0:
    n = int(input("Ingrese un valor para n (debe ser no negativo): "))
    if n<0:
        print('El número no puede ser negativo')


suma_pares, promedio_pares = calcular_suma_promedio(n, 'pares')
suma_impares, promedio_impares = calcular_suma_promedio(n, 'impares')
suma_multiplos_3, promedio_multiplos_3 = calcular_suma_promedio(n, 'multiplos de 3')

print(f"La suma de los primeros {n} números pares es: {suma_pares}")
print(f"El promedio de los primeros {n} números pares es: {promedio_pares}")

print(f"La suma de los primeros {n} números impares es: {suma_impares}")
print(f"El promedio de los primeros {n} números impares es: {promedio_impares}")

print(f"La suma de los primeros {n} números múltiplos de 3 es: {suma_multiplos_3}")
print(f"El promedio de los primeros {n} números múltiplos de 3 es: {promedio_multiplos_3}")
0