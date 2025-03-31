from flask import Flask
from src.routes import configure_routes
from src.auth import token_required, login
from src.utils import setup_logging
import logging

app = Flask(__name__)  # Inicia Flask

# Configuración de la clave secreta para JWT
app.config['SECRET_KEY'] = 'supersecretkey'

setup_logging()  # Configura logs

# Asocia autenticación y rutas, pasando la clave secreta a las funciones
configure_routes(app, app.config['SECRET_KEY'])

# Ejecutar la aplicación
if __name__ == '__main__':
    logging.info("Iniciando la aplicacion Flask - PokeAPI...")
    app.run(debug=True)
