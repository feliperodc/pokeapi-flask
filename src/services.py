import requests
import random
import logging
from flask import jsonify

# Para recibir el tipo del pokemon
def get_pokemon_type(name):
    logging.info(f"Peticion recibida para obtener tipo de Pokemon: {name}")
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}" # construye la url de la pokeapi para obtener la data del pokemon
    response = requests.get(url) # solicitud http a pokeapi
    
    if response.status_code == 200: # si la solicitud es exitosa (200), convierte respuesta a JSON, extrae los tipos de pokemon y retorna JSON con el nombre y lista de tipos
        data = response.json()
        types = [type_info['type']['name'] for type_info in data['types']]
        logging.info(f"Pokemon encontrado: {name} - Tipos: {types}")
        return jsonify({'pokemon': name, 'types': types})
    else:
        logging.warning(f"Pokemon no encontrado: {name}")
        return jsonify({'error': 'Pokemon no encontrado'}), 404

# Para obtener un Pokemon al azar de un tipo especifico
def get_random_pokemon(type):
    logging.info(f"Peticion para obtener un Pokemon aleatorio del tipo: {type}")
    url = f"https://pokeapi.co/api/v2/type/{type.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pokemons = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
        random_pokemon = random.choice(pokemons) # random para seleccionar un pokemon al azar , si no existe devuelve error (404)
        logging.info(f"Pokemon aleatorio obtenido: {random_pokemon}")
        return jsonify({'random_pokemon': random_pokemon})
    else:
        logging.error(f"Tipo de Pokemon no encontrado: {type}")
        return jsonify({'error': 'Tipo no encontrado'}), 404

# Para obtener el Pokemon con nombre mas largo de un tipo
def get_longest_pokemon_name(type):
    logging.info(f"Peticion para obtener el Pokemon con nombre mas largo del tipo: {type}")
    url = f"https://pokeapi.co/api/v2/type/{type.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json() # data es el JSON q devuelve la PokeAPI cuando se solicita informacion sobre un tipo de pokemon
        pokemon_list = data['pokemon']
        pokemons = []
        for p in pokemon_list:
            pokemons.append(p['pokemon']['name']) # recorre cada elemento de la lista, extrae el nombre de cada pokemon y almacena los nombres en la lista pokemons
        longest_pokemon = max(pokemons, key=len)
        logging.info(f"Pokemon con nombre mas largo obtenido: {longest_pokemon}")
        return jsonify({'longest_pokemon_name': longest_pokemon})
    else:
        logging.error(f"Tipo de Pokemon no encontrado: {type}")
        return jsonify({'error': 'Tipo no encontrado'}), 404
