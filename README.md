# PokeAPI con Flask

Esta es una API en Flask que permite obtener información sobre Pokemon utilizando datos de la [PokeAPI](https://pokeapi.co/).

Incluye autenticacion básica y las siguientes funciones:
- Consultar tipos de Pokemon
- Obtener un Pokemon aleatorio de un tipo especifico
- Encontrar el Pokemon con el nombre mas largo de un tipo especifico.

## 📋 Requisitos Previos

- Python 3.8 o superior  
- pip (administrador de paquetes de Python)  
- Docker (opcional, si deseas ejecutar el proyecto con contenedores)

## 🚀 Instalación y Ejecución

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

5. Accede a la API en tu navegador:
    http://localhost:5000

------------------------------------------------------------------------------

🎲 Obtener un Pokemon segun su nombre

    GET /pokemon/{name}

Ejemplo
```bash
    http://localhost:5000/pokemon/pikachu
```

--------------------------------------------------

🎲 Obtener un Pokemon aleatorio de un tipo específico

    GET /random_pokemon/{type}

Ejemplo:
```bash
    http://localhost:5000/random_pokemon/fire
```

--------------------------------------------------

🎲 Obtener el Pokemon con el nombre más largo de un tipo

    GET /longest_pokemon_name/{type}

Ejemplo:
```bash
    http://localhost:5000/longest_pokemon_name/water
```

------------------------------------------------------------------------------

