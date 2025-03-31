from flask import jsonify
from flask import request
from flask import Blueprint
from src.auth import auth
from src.services import get_pokemon_type, get_random_pokemon, get_longest_pokemon_name

# Definir el Blueprint para modularizar
routes_bp = Blueprint('routes', __name__)

# Endpoint principal - define la ruta raiz y devuelve un mensaje
@routes_bp.route('/')
def index():
    return "Challenge MercadoLibre: Pokemons"

# Endpoint para obtener el tipo de un Pokemon 
@routes_bp.route('/pokemon/<name>', methods=['GET']) # define un endpoint q recibe el nombre del pokemon de la url
@auth.login_required # protege el endpoint con autenticacion 
def pokemon_type(name):
    return get_pokemon_type(name)

# Endpoint para obtener un Pokemon al azar de un tipo especifico
@routes_bp.route('/random_pokemon/<type>', methods=['GET']) # define un endpoint q recibe un tipo de pokemon de la url
@auth.login_required
def random_pokemon(type):
    return get_random_pokemon(type)

# Endpoint para obtener el Pokemon con nombre mas largo de un tipo
@routes_bp.route('/longest_pokemon_name/<type>', methods=['GET'])
@auth.login_required
def longest_pokemon(type):
    return get_longest_pokemon_name(type)

def configure_routes(app):
    app.register_blueprint(routes_bp)
