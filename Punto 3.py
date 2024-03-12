# Crear un programa que lea el nombre, sexo y edad de n personas (mínimo 4) 
# y despliegue un saludo personalizado, además calcule la edad promedio general y por sexo

edades_hombres = 0
edades_mujeres = 0
contador_hombres = 0
contador_mujeres = 0
edad_promedio_general = 0


while True:
    num_personas = int(input("Ingrese el número de personas (mínimo 4): "))
    if num_personas >= 4:
        break
    else:
        print("Debe ingresar al menos 4 personas.")

for i in range(num_personas):
    nombre = input("Ingrese el nombre de la persona {}: ".format(i + 1))

    while True:
        sexo = input("Ingrese el sexo de la persona (H para hombre, M para mujer): ")
        if sexo.upper() in ['H', 'M']:
            break
        else:
            print("Sexo no válido. Por favor, ingrese 'H' para hombre o 'M' para mujer.")

    edad = int(input("Ingrese la edad de la persona {}: ".format(i + 1)))

    edad_promedio_general += edad

    if sexo.upper() == 'H':
        edades_hombres += edad
        contador_hombres += 1
    elif sexo.upper() == 'M':
        edades_mujeres += edad
        contador_mujeres += 1

    if sexo.upper() == 'H':
        print("Hola, Sr. {}. Tienes {} años.".format(nombre, edad))
    elif sexo.upper() == 'M':
        print("Hola, Sra. {}. Tienes {} años.".format(nombre, edad))

    
    if i >= 3:  
        promedio_general = edad_promedio_general / (i + 1)
        print("Promedio de edad general:", promedio_general)
        if contador_hombres > 0:
            promedio_hombres = edades_hombres / contador_hombres
            print("Promedio de edad de hombres:", promedio_hombres)
        if contador_mujeres > 0:
            promedio_mujeres = edades_mujeres / contador_mujeres
            print("Promedio de edad de mujeres:", promedio_mujeres)
