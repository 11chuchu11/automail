import logging

ERROR = "ERROR"

logging.basicConfig(filename='registro.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', encoding="utf-8")
