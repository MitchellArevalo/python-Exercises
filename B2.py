import requests
import random

def planetData(planet_1, planet_2):
    
    rotation_period_unknow_planet_1 = False
    diameter_unknow_planet_1 = False
    population_unknow_planet_1 = False
    rotation_period_unknow_planet_2 = False
    diameter_unknow_planet_2 = False
    population_unknow_planet_2 = False
    rotation_period_result = 'nocambia'
    diameter_result = 'nocambia'
    population_result = 'nocambia'
    
    name_planet_1 = planet_1['name']
    rotation_period_planet_1 = planet_1['rotation_period']
    diameter_planet_1 = planet_1['diameter']
    population_planet_1 = planet_1['population']  
 
    if rotation_period_planet_1 == 'unknown':
        rotation_period_unknow_planet_1 = True
    if  diameter_planet_1 == 'unknown':
        diameter_unknow_planet_1 = True
    if population_planet_1 == 'unknown':
        population_unknow_planet_1 = True
    
    name_planet_2 = planet_2['name']
    rotation_period_planet_2 = planet_2['rotation_period']
    diameter_planet_2 = planet_2['diameter']
    population_planet_2 = planet_2['population'] 
    
    if rotation_period_planet_2 == 'unknown':
        rotation_period_unknow_planet_2 = True
    if  diameter_planet_2 == 'unknown':
        diameter_unknow_planet_2 = True
    if population_planet_2 == 'unknown':
        population_unknow_planet_2 = True 
    
    if rotation_period_unknow_planet_2 == True or rotation_period_unknow_planet_1 == True:
        if rotation_period_unknow_planet_1 == True and rotation_period_unknow_planet_2 == True:
            rotation_period_result = 'N/A'
        if rotation_period_unknow_planet_1 == True:
            rotation_period_result = name_planet_2
        if rotation_period_unknow_planet_2 == True:
            rotation_period_result = name_planet_1
            
    else:    
        
        if int(rotation_period_planet_1) < int(rotation_period_planet_2):
            rotation_period_result = name_planet_2
        if int(rotation_period_planet_2) < int(rotation_period_planet_1):
            rotation_period_result = name_planet_1
            
    if diameter_unknow_planet_2 == True or diameter_unknow_planet_1 == True:
        if diameter_unknow_planet_1 == True and diameter_unknow_planet_2 == True:
            diameter_result = 'N/A'
        if diameter_unknow_planet_1 == True:
            diameter_result = name_planet_2
        if diameter_unknow_planet_2 == True:
            diameter_result = name_planet_1
            
    else:   
        if int(diameter_planet_1) < int(diameter_planet_2):
            diameter_result = name_planet_2
        if int(diameter_planet_2) < int(diameter_planet_1):
            diameter_result = name_planet_1
    
    
    if population_unknow_planet_2 == True or population_unknow_planet_1 == True:
        if population_unknow_planet_1 == True and population_unknow_planet_2 == True:
            population_result = 'N/A'
        if population_unknow_planet_1 == True:
            population_result = name_planet_2
        if population_unknow_planet_2 == True:
            population_result = name_planet_1
            
    else:           
        if int(population_planet_1) < int(population_planet_2):
            population_result = name_planet_2
        if int(population_planet_2) < int(population_planet_1):
            population_result = name_planet_1
        
   
    print(f'El planeta con mayor periodo de rotacion es {rotation_period_result}')
    print(f'El planeta con mayor diametro es {diameter_result}')
    print(f'El planeta con mayor población es {population_result}')
    
    
   

numero_aleatorio = random.randint(1, 60)
responsePlanet1 = requests.get('https://swapi.dev/api/planets/' + str(numero_aleatorio) + '/')

if responsePlanet1.status_code == 200:
    planet_1 = responsePlanet1.json()
else:
    print("Error en la petición: ", responsePlanet1.status_code)
    
    
numero_aleatorio2 = random.randint(1, 60)
if numero_aleatorio2 == numero_aleatorio:
    if numero_aleatorio2 == 60:
        numero_aleatorio2 = numero_aleatorio2 - 1
    else:
        numero_aleatorio2 = numero_aleatorio2 + 1
        
responsePlanet2 = requests.get('https://swapi.dev/api/planets/' + str(numero_aleatorio2) + '/')

if responsePlanet2.status_code == 200:
    planet_2 = responsePlanet2.json()
else:
    print("Error en la petición: ", responsePlanet2.status_code)

    
planetData(planet_1, planet_2)
    
    
