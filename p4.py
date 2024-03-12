# -*- coding: utf-8 -*-
"""

@author: Yanin Alejandra Escobar Aguas (1004616271)
         Juan Felipe Sierra Olaya (1114239077)
         Jennifer Reyes Arboleda (1004614696)

# Crear un programa en Python para pedir los datos de estudiantes, que comprende:
  nombre de la persona, sexo, carrera y 4 notas parciales (entre 0 y 5). Calcular la
  nota definitiva de cada estudiante resultado de self.nota1 * 20% + nota2 * 25% + nota3
  * 30% + nota4 * 25%. Con los datos ingresados y calculados por estudiante, se
  debe:
  a. Guardar la información en un archivo csv.
  b. Recuperar la información desde el archivo y desplegar:
  i. Relación de estudiantes con sus notas parciales y definitiva.
  ii. Estudiante con mayor promedio (desplegando la nota)
  iii. Estudiante con el menor promedio (desplegando la nota)
  iv. Porcentaje de estudiantes que aprueban.
  v. Porcentaje de estudiantes que reprueban.
  vi. Promedio de nota1, nota2, nota3, nota4 y nota final.
  vii. Promedio final por carrera.
  viii. Promedio final por sexo
  El usuario debe poder seleccionar qué opción quiere ejecutar.
  Las notas se deben desplegar con un decimal, y los promedios con 3 decimales.
  Deben entregar el archivo csv generado con un mínimo de 10 estudiantes.
"""

# -- IMPORTS --
import csv

# Función para ingresar los datos de un estudiante
def ingresar_estudiante():
    estudiante = {}
    estudiante['nombre'] = input("Nombre del estudiante: ")
    estudiante['sexo'] = input("Sexo del estudiante: ")
    estudiante['carrera'] = input("Carrera del estudiante: ")
    estudiante['nota1'] = float(input("Nota 1: "))
    estudiante['nota2'] = float(input("Nota 2: "))
    estudiante['nota3'] = float(input("Nota 3: "))
    estudiante['nota4'] = float(input("Nota 4: "))
    estudiante['nota_definitiva'] = calcular_nota_definitiva(estudiante)
    return estudiante
# Función para calcular la nota definitiva de un estudiante
def calcular_nota_definitiva(estudiante):
    nota1 = estudiante['nota1'] * 0.2
    nota2 = estudiante['nota2'] * 0.25
    nota3 = estudiante['nota3'] * 0.3
    nota4 = estudiante['nota4'] * 0.25
    nota_definitiva = nota1 + nota2 + nota3 + nota4
    return round(nota_definitiva, 1)

# Función para guardar la información en un archivo CSV
def guardar_estudiantes(estudiantes):
    with open('estudiantes.csv', 'w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(['Nombre', 'Sexo', 'Carrera', 'Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Nota Definitiva'])
        for estudiante in estudiantes:
            writer.writerow([estudiante['nombre'], estudiante['sexo'], estudiante['carrera'], estudiante['nota1'], estudiante['nota2'],
                             estudiante['nota3'], estudiante['nota4'], estudiante['nota_definitiva']])

# Función para recuperar la información desde el archivo CSV y desplegar los resultados
def mostrar_resultados():
    estudiantes = []
    with open('estudiantes.csv', 'r') as archivo_csv:
        reader = csv.reader(archivo_csv)
        next(reader) # Saltar la primera fila (encabezados)
        for row in reader:
            estudiante = {}
            estudiante['nombre'] = row[0]
            estudiante['sexo'] = row[1]
            estudiante['carrera'] = row[2]
            estudiante['nota1'] = float(row[3])
            estudiante['nota2'] = float(row[4])
            estudiante['nota3'] = float(row[5])
            estudiante['nota4'] = float(row[6])
            estudiante['nota_definitiva'] = float(row[7])
            estudiantes.append(estudiante)

    print("Relación de estudiantes con sus notas parciales y definitiva:")
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Nota 1: {estudiante['nota1']:.1f}")
        print(f"Nota 2: {estudiante['nota2']:.1f}")
        print(f"Nota 3: {estudiante['nota3']:.1f}")
        print(f"Nota 4: {estudiante['nota4']:.1f}")
        print(f"Nota Definitiva: {estudiante['nota_definitiva']:.1f}")
        print()

    promedios = {
        'nota1': [],
        'nota2': [],
        'nota3': [],
        'nota4': [],
        'nota_definitiva': [],
    }

    for estudiante in estudiantes:
        promedios['nota1'].append(estudiante['nota1'])
        promedios['nota2'].append(estudiante['nota2'])
        promedios['nota3'].append(estudiante['nota3'])
        promedios['nota4'].append(estudiante['nota4'])
        promedios['nota_definitiva'].append(estudiante['nota_definitiva'])

    promedio_nota1 = sum(promedios['nota1']) / len(promedios['nota1'])
    promedio_nota2 = sum(promedios['nota2']) / len(promedios['nota2'])
    promedio_nota3 = sum(promedios['nota3']) / len(promedios['nota3'])
    promedio_nota4 = sum(promedios['nota4']) / len(promedios['nota4'])
    promedio_nota_definitiva = sum(promedios['nota_definitiva']) / len(promedios['nota_definitiva'])

    print(f"Promedio de Nota 1: {promedio_nota1:.3f}")
    print(f"Promedio de Nota 2: {promedio_nota2:.3f}")
    print(f"Promedio de Nota 3: {promedio_nota3:.3f}")
    print(f"Promedio de Nota 4: {promedio_nota4:.3f}")
    print(f"Promedio de Nota Definitiva: {promedio_nota_definitiva:.3f}")

    promedios_carrera = {}
    promedios_sexo = {'H': [], 'M': []}

    for estudiante in estudiantes:
        carrera = estudiante['carrera']
        promedio = estudiante['nota_definitiva']

        if carrera in promedios_carrera:
            promedios_carrera[carrera].append(promedio)
        else:
            promedios_carrera[carrera] = [promedio]

            promedios_sexo[estudiante['sexo'].upper()].append(promedio)

    print("\nPromedio final por carrera:")
    for carrera, promedios in promedios_carrera.items():
        promedio_final_carrera = sum(promedios) / len(promedios)
        print(f"{carrera}: {promedio_final_carrera:.3f}")

    print("\nPromedio final por sexo:")
    for sexo, promedios in promedios_sexo.items():
        if promedios:  # Verificar si hay estudiantes de un determinado sexo
            promedio_final_sexo = sum(promedios) / len(promedios)
            print(f"{sexo}: {promedio_final_sexo:.3f}")
        else:
            print(f"{sexo}: No hay estudiantes")

    aprobados = [estudiante for estudiante in estudiantes if estudiante['nota_definitiva'] >= 3]
    reprobados = [estudiante for estudiante in estudiantes if estudiante['nota_definitiva'] < 3]

    porcentaje_aprobados = (len(aprobados) / len(estudiantes)) * 100
    porcentaje_reprobados = (len(reprobados) / len(estudiantes)) * 100

    print(f"\nPorcentaje de estudiantes que aprueban: {porcentaje_aprobados:.2f}%")
    print(f"Porcentaje de estudiantes que reprueban: {porcentaje_reprobados:.2f}%")

    estudiante_mayor_promedio = max(estudiantes, key=lambda estudiante: estudiante['nota_definitiva'])
    estudiante_menor_promedio = min(estudiantes, key=lambda estudiante: estudiante['nota_definitiva'])

    print(f"\nEstudiante con mayor promedio:")
    print(f"Nombre: {estudiante_mayor_promedio['nombre']}")
    print(f"Promedio: {estudiante_mayor_promedio['nota_definitiva']:.1f}")

    print(f"\nEstudiante con menor promedio:")
    print(f"Nombre: {estudiante_menor_promedio['nombre']}")
    print(f"Promedio: {estudiante_menor_promedio['nota_definitiva']:.1f}")

# Función para mostrar el menú y ejecutar la opción seleccionada por el usuario
def mostrar_menu(estudiantes):
    print("1. Ingresar datos de estudiantes")
    print("2. Guardar información en archivo CSV")
    print("3. Mostrar resultados")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        cantidad_estudiantes = int(input("Cuántos estudiantes desea ingresar? "))
        for _ in range(cantidad_estudiantes):
            estudiante = ingresar_estudiante()
            estudiantes.append(estudiante)
    elif opcion == '2':
        guardar_estudiantes(estudiantes)
        print("Datos guardados en archivo CSV.")
    elif opcion == '3':
        mostrar_resultados()  # Eliminamos el argumento estudiantes
    elif opcion == '4':
        exit()
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")

# Menú principal
def main():
    estudiantes = []
    while True:
        mostrar_menu(estudiantes)

