import insertarDatos
import database

# Crear la base de datos al iniciar la aplicación
database.crear_base_datos()

# Iniciar el servidor web
insertarDatos.procesar_datos_desde_json()