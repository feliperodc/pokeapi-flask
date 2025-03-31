# Pokémon API 🐉

Esta es una API en Flask que permite obtener información sobre Pokémon utilizando datos de la [PokeAPI](https://pokeapi.co/). 
Incluye autenticación básica y funciones para consultar tipos de Pokémon, obtener un Pokémon aleatorio y encontrar el Pokémon con el nombre más largo de un tipo específico.

## 📋 Requisitos Previos

- Python 3.8 o superior  
- pip (administrador de paquetes de Python)  
- Docker (opcional, si deseas ejecutar el proyecto con contenedores)

## 🚀 Instalación y Ejecución

1. Clona este repositorio:
   bash
   git clone https://github.com/feliperodc/pruebasmeli.git
   cd pokeapichallenge

2. Crea un entorno virtual (opcional, pero recomendado):
    python -m venv venv
    #macOS/Linux source venv/bin/activate # En Windows: venv\Scripts\activate

3. Instala las dependencias:
    pip install -r requirements.txt

4. Ejecuta la aplicación:
    python app.py

5. Accede a la API en tu navegador o Postman:
    http://localhost:5000

------------------------------------------------------------------------------

🎲 Obtener un Pokémon segun su nombre

GET /pokemon/{name}

Ejemplo
bash
http://localhost:5000/pokemon/pikachu

--------------------------------------------------
--------------------------------------------------

🎲 Obtener un Pokémon aleatorio de un tipo específico

GET /random_pokemon/{type}

Ejemplo:
bash
http://localhost:5000/random_pokemon/fire

--------------------------------------------------
--------------------------------------------------

🎲 Obtener el Pokémon con el nombre más largo de un tipo

GET /longest_pokemon_name/{type}

Ejemplo:
http://localhost:5000/longest_pokemon_name/water

------------------------------------------------------------------------------

