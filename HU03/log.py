import logging
import re

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

def validarCamposLlenos(correo,contraseña):
    try: 
        logging.debug("Inicio de la validación del correo")
        logging.info("Validación en progreso")
        if correo != "" and contraseña != "":
            logging.info("Los datos están correctos")
            return True 
        else: 
            logging.info("El correo o la contraseña están vacíos")
            return False
        
    except Exception as e:
        logging.exception(f"Error inesperado durante la validación: {str(e)}")
    finally:
        logging.debug("Fin de la validación del correo")
        



def validar_correo(correo):
    try:
        logging.debug("Inicio de la validación del correo")
        logging.info("Validación en progreso")
        
        # Expresión regular para validar el formato del correo electrónico
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        if re.match(patron, correo):
            logging.info("El correo tiene un formato correcto")
            return "es_valido"

        else:
            logging.error("El correo tiene un formato incorrecto")
            
    
    except Exception as e:
        logging.exception(f"Error inesperado durante la validación: {str(e)}")
    finally:
        logging.debug("Fin de la validación del correo")

