from flask import jsonify, request, Blueprint
from src.auth import token_required, login
from src.services import get_pokemon_type, get_random_pokemon, get_longest_pokemon_name

# Definir el Blueprint para modularizar
routes_bp = Blueprint('routes', __name__)

# Endpoint principal
@routes_bp.route('/')
def index():
    return "Challenge MercadoLibre: Pokemons"

# Endpoint para obtener el tipo de un Pokemon
@routes_bp.route('/pokemon/<name>', methods=['GET'])
@token_required(secret_key='supersecretkey')  # Usar la clave secreta de la app
def pokemon_type(name):
    return get_pokemon_type(name)

# Endpoint para obtener un Pokemon al azar de un tipo específico
@routes_bp.route('/random_pokemon/<type>', methods=['GET'])
@token_required(secret_key='supersecretkey')  # Usar la clave secreta de la app
def random_pokemon(type):
    return get_random_pokemon(type)

# Endpoint para obtener el Pokemon con nombre más largo de un tipo
@routes_bp.route('/longest_pokemon_name/<type>', methods=['GET'])
@token_required(secret_key='supersecretkey')  # Usar la clave secreta de la app
def longest_pokemon(type):
    return get_longest_pokemon_name(type)

def configure_routes(app, secret_key):
    app.register_blueprint(routes_bp)
    app.secret_key = secret_key  # Agregar la clave secreta a la app
