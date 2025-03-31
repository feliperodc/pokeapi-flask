import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO, # Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(levelname)s - %(message)s", # Formato del mensaje de log
        handlers=[
            logging.FileHandler("logs/app.log"),  # Guardar logs en el archivo
            logging.StreamHandler()  # Mostrar logs en la terminal
        ]
    )
