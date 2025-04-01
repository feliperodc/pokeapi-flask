from flask import Flask, request  # Importa las clases necesarias de Flask
from src.routes import configure_routes  # Importa la función para configurar las rutas
from src.auth import login  # Importa la función de login que genera el token JWT
import logging  # Importa el módulo de logging para registrar mensajes de la aplicación

app = Flask(__name__)  # Crea la instancia de la aplicación Flask

# Define la clave secreta para JWT, se utiliza para firmar y verificar los tokens
app.config['SECRET_KEY'] = 'supersecretkey'

# Configura las rutas de la API utilizando la función configure_routes definida en routes.py
configure_routes(app)

# Ruta para login, permite obtener un token JWT en la respuesta
@app.route('/login', methods=['POST'])  # Define la ruta /login para la autenticación (POST)
def login_route():
    auth = request.json  # Obtiene los datos JSON enviados en la solicitud
    return login(auth, app.config['SECRET_KEY'])  # Llama a la función login para generar el token

# Condición para ejecutar la aplicación solo si este archivo es ejecutado directamente
if __name__ == '__main__':
    logging.info("Iniciando la aplicación Flask - PokeAPI...")  # Registra un mensaje de inicio de la aplicación
    app.run(debug=True)  # Ejecuta la aplicación Flask en modo de depuración (debug)