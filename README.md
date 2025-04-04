# PokeAPI con Flask

Esta es una API en Flask que permite obtener información sobre Pokemon utilizando datos de la [PokeAPI](https://pokeapi.co/).

Incluye autenticacion JWT y las siguientes funciones:
- Consultar tipos de Pokemon.
- Obtener un Pokemon aleatorio de un tipo especifico.
- Encontrar el Pokemon con el nombre mas largo de un tipo especifico.

## 📋 Requisitos Previos

- Python 3.8 o superior  
- pip (administrador de paquetes de Python)  
- Docker (opcional, si deseas ejecutar el proyecto con contenedores)

## 🚀 Instalación y Ejecución.

1. Clona este repositorio:
   ```bash
        git clone https://github.com/feliperodc/pokeapi-flask.git
        cd pokeapi-flask
    ```

2. Crea un entorno virtual (opcional, pero recomendado):
    ```bash
        python -m venv venv
        source venv/bin/activate # En macOS/Linux 
        venv\Scripts\activate # En Windows
    ```

3. Instala las dependencias:
    ```bash
        pip install -r requirements.txt
    ```

4. Ejecuta la aplicación:
    ```bash
        python app.py
    ```
5. Para poder ejecutar la API, se require autenticación (explicada en el punto siguiente)


------------------------------------------------------------------------------

## 🔑 Autenticacion JWT.

Para acceder a los endpoints de la API, se requiere autenticación mediante un token JWT. 
Este token tiene una expiración de una hora para mayor seguridad.

Para obtener un token, realiza una solicitud POST a la ruta /login con las credenciales:

### Obtener un Token JWT

    POST /login

Ejemplo con `curl`:
```bash
curl -X POST "http://localhost:5000/login" -H "Content-Type: application/json" -d '{"username": "admin", "password": "password1"}'
```

Esto devolverá un token JWT que deberás incluir en las siguientes peticiones.

### Uso del Token JWT
Agrega el token en los headers de las solicitudes:
```bash
curl -X GET "http://localhost:5000/pokemon/pikachu" -H "x-access-token: <TOKEN>"
```

------------------------------------------------------------------------------

## 🐳 Ejecución con Docker.

Se puede ejecutar la API dentro de un contenedor Docker para facilitar su despliegue.

### Construir la imagen
```bash
docker build -t pokeapi-flask .
```

### Ejecutar el contenedor
```bash
docker run -p 5000:5000 pokeapi-flask
```

### Ver contenedores en ejecución
```bash
docker ps
```

### Detener el contenedor
```bash
docker stop <CONTAINER_ID>
```

------------------------------------------------------------------------------

## 📡 Uso de la API.

#### 🎲 Obtener los tipos de un Pokemon segun su nombre:

    GET /pokemon/{name}

Ejemplo en bash:
```bash
    curl -H "x-access-token: <token>" http://localhost:5000/pokemon/pikachu
```

--------------------------------------------------

#### 🎲 Obtener un Pokemon aleatorio de un tipo específico:

    GET /random_pokemon/{type}

Ejemplo en bash:
```bash
    curl -H "x-access-token: <token>" http://localhost:5000/random_pokemon/grass
```

--------------------------------------------------

#### 🎲 Obtener el Pokemon con el nombre más largo de un tipo:

    GET /longest_pokemon_name/{type}

Ejemplo en bash:
```bash
    curl -H "x-access-token: <token>" http://localhost:5000/longest_pokemon_name/water
```

------------------------------------------------------------------------------

