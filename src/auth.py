from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

# Guarda usuarios para autenticacion
users = {
    "admin": "pass1",
    "admin2": "pass2"
}

# Funcion de autenticacion - verifica el usuario y la contraseña y retorna el username si la auth fue correcta 
@auth.verify_password
def verify_password(username, password): 
    if username in users and users[username] == password:
        return username
