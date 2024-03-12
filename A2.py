import requests
import random


def film_description(film_dict):
    
    if not isinstance(film_dict, dict):
        print("Error de argumento")
        return
    
    film_info = []

    director = film_dict['director']
    title = film_dict['title']
    opening_crawl = film_dict['opening_crawl']  
    release_date = str(film_dict['release_date'])
    producer = film_dict['producer']

    film_info.append(director)
    film_info.append(title)
    film_info.append(opening_crawl)
    film_info.append(release_date)
    film_info.append(producer)

    print("Director: {}".format(director))
    print("Título: {}".format(title))
    print("Apertura: {}".format(opening_crawl))
    print("Fecha de estreno: {}".format(release_date))
    print("Productor: {}".format(producer))
    
    return film_info


numero_aleatorio = random.randint(1, 6)
response = requests.get('https://swapi.dev/api/films/' + str(numero_aleatorio) + '/')

if response.status_code == 200:
    film = response.json()

    film_description(film)
else:
    print("Error en la petición: ", response.status_code)