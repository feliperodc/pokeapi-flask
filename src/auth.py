import jwt
import datetime
from functools import wraps
from flask import request, jsonify

# Clave secreta se pasa como argumento al usar el decorador
def token_required(secret_key):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('x-access-token')
            if not token:
                return jsonify({'error': 'Token es requerido'}), 401
            try:
                # Verifica el token con la clave secreta pasada
                data = jwt.decode(token, secret_key, algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                return jsonify({'error': 'El token ha expirado'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'error': 'Token inválido'}), 401
            return f(*args, **kwargs)
        return decorated
    return decorator

# Ruta para generar el token de acceso
def login(auth, secret_key):
    auth_data = auth
    if not auth_data or not auth_data.get('username') or not auth_data.get('password'):
        return jsonify({'error': 'Usuario y contraseña requeridos'}), 400

    if auth_data['username'] == 'admin' and auth_data['password'] == 'password1':
        # Genera el token con expiración en 1 hora
        token = jwt.encode({'user': auth_data['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, 
                           secret_key, algorithm="HS256")
        return jsonify({'token': token})
    
    return jsonify({'error': 'Credenciales inválidas'}), 401
