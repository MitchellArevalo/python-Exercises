# Crear un programa para pedir los datos de 4 personas, que comprende: 
# nombre de la persona, su sexo y 4 notas parciales. 
# Calcular la nota definitiva de cada estudiante resultado de nota1 * 20% + nota2 * 25% + nota3 * 30% + nota4 * 25%.
# Con los datos ingresados y calculados, se debe desplegar:
# a. Estudiante con mayor promedio (desplegando la nota)
# a. Estudiante con el menor promedio (desplegando la nota)
# b. Porcentaje de estudiantes que aprueban.
# c. Porcentaje de estudiantes que reprueban.
# d. Promedio de nota1, nota2, nota3, nota4 y nota final.
# e. Promedio final por sexo.


nombres = []
sexos = []
notas1 = []
notas2 = []
notas3 = []
notas4 = []
notas_finales = []


for i in range(4):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")


    while True:
        sexo = input(f"Ingrese el sexo del estudiante {i + 1} (M/F): ")
        if sexo.upper() in ['M', 'F']:
            break
        else:
            print("Género no válido. Por favor, ingrese 'M' o 'F'.")

    
    while True:
        try:
            nota1 = float(input("Ingrese la nota 1: "))
            nota2 = float(input("Ingrese la nota 2: "))
            nota3 = float(input("Ingrese la nota 3: "))
            nota4 = float(input("Ingrese la nota 4: "))

            if all(0.0 <= nota <= 5.0 for nota in [nota1, nota2, nota3, nota4]):
                break
            else:
                print("Solo se pueden añadir valores numéricos de 0 a 5 para las notas.")
        except ValueError:
            print("Ingrese valores numéricos válidos para las notas.")

    nota_final = nota1 * 0.20 + nota2 * 0.25 + nota3 * 0.30 + nota4 * 0.25

    nombres.append(nombre)
    sexos.append(sexo)
    notas1.append(nota1)
    notas2.append(nota2)
    notas3.append(nota3)
    notas4.append(nota4)
    notas_finales.append(nota_final)


indice_max = notas_finales.index(max(notas_finales))
indice_min = notas_finales.index(min(notas_finales))


aprobados = sum(1 for nota in notas_finales if nota >= 3.0)
reprobados = 4 - aprobados


promedio_nota1 = sum(notas1) / 4
promedio_nota2 = sum(notas2) / 4
promedio_nota3 = sum(notas3) / 4
promedio_nota4 = sum(notas4) / 4
promedio_notas_finales = sum(notas_finales) / 4


notas_mujeres = [nota for i, nota in enumerate(notas_finales) if sexos[i] == 'F']
notas_hombres = [nota for i, nota in enumerate(notas_finales) if sexos[i] == 'M']

promedio_mujeres = sum(notas_mujeres) / len(notas_mujeres) if len(notas_mujeres) > 0 else 0
promedio_hombres = sum(notas_hombres) / len(notas_hombres) if len(notas_hombres) > 0 else 0


print(f"Estudiante con la mayor nota final: {nombres[indice_max]} con nota {notas_finales[indice_max]}")
print(f"Estudiante con la menor nota final: {nombres[indice_min]} con nota {notas_finales[indice_min]}")
print(f"Porcentaje de estudiantes que aprueban: {(aprobados / 4) * 100}%")
print(f"Porcentaje de estudiantes que reprueban: {(reprobados / 4) * 100}%")
print(f"Promedio de nota1: {promedio_nota1}")
print(f"Promedio de nota2: {promedio_nota2}")
print(f"Promedio de nota3: {promedio_nota3}")
print(f"Promedio de nota4: {promedio_nota4}")
print(f"Promedio de notas finales: {promedio_notas_finales}")
print(f"Promedio final por sexo - Mujeres: {promedio_mujeres}")
print(f"Promedio final por sexo - Hombres: {promedio_hombres}")
