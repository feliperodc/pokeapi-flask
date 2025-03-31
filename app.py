from flask import Flask
from src.routes import configure_routes
from src.auth import auth
from src.utils import setup_logging
import logging

app = Flask(__name__)  # Inicia Flask
setup_logging()  # Configura logs

# Asocia autenticación y rutas
app.config["AUTH"] = auth
configure_routes(app)

# Ejecutar la aplicación
if __name__ == '__main__':
    logging.info("Iniciando la aplicacion Flask - PokeAPI...")
    app.run(debug=True)
