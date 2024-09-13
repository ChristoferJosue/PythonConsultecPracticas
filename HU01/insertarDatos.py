import json
import database
import csv_files

def procesar_datos_desde_json():
    # Leer los datos del archivo JSON
    with open('datos.json', 'r') as archivo_json:
        data = json.load(archivo_json)

    # Guardar el JSON en un archivo CSV
    csv_files.guardar_datos_csv(data['usuarios'])

    # Insertar los usuarios en la base de datos SQLite
    database.insertar_usuarios(data['usuarios'])

    # Obtener los usuarios de la base de datos
    usuarios = database.obtener_usuarios()
    print(usuarios)

    print('Datos procesados correctamente.')
