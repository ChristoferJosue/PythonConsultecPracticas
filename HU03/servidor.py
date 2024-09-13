# http_handler.py

from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import bcrypt
from database import insert_user,obtener_usuarios
import requests
import json

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        if self.path == '/colaboradores':

            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode('utf-8')

    
            params = json.loads(body)

            correo = params.get('correo', '')
            contraseña = params.get('contraseña', '')
            salt = bcrypt.gensalt()
            

            contraHasheada=bcrypt.hashpw(contraseña.encode('utf-8'),salt)
            print(type(contraHasheada))
            print(contraHasheada)

            insert_user(correo, contraHasheada.decode('utf-8'))

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Usuario agregado exitosamente'}).encode('utf-8'))

    def do_GET(self) -> None:
        if self.path == '/colaboradores':
            #Enviar resp exitosa
            self.send_response(200)

            #establecer cabecera de la resp
            self.send_header('Content-type','application/json')
            self.end_headers()

            #crear diccionarion para el cont de la resp formaot json
            respuesta_json=obtener_usuarios()


            #convertir el diccionario en json y enviar cont
            respuesta_json_str = json.dumps(respuesta_json)
            self.wfile.write(respuesta_json_str.encode('utf-8'))


