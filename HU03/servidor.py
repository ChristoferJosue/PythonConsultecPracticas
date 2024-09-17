# http_handler.py
from log import validar_correo, validarCamposLlenos
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import bcrypt
from database import insert_user,obtener_usuarios
import requests
import json
import logging


class RequestHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):  
        if self.path == '/colaboradores':

            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length).decode('utf-8')

    
            
            try:
                params = json.loads(body)

                correo = params.get('correo', '')
                contraseña = params.get('contraseña', '')
                salt = bcrypt.gensalt()
                

                contraHasheada=bcrypt.hashpw(contraseña.encode('utf-8'),salt)
                print(type(contraHasheada))
                print(contraHasheada)
                
                if validar_correo(correo)== "es_valido" and validarCamposLlenos(correo,contraseña) == True:
                    insert_user(correo, contraHasheada.decode('utf-8'))
                    self.send_response(201)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'message': 'Usuario agregado exitosamente'}).encode('utf-8'))
                else: 
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'message': 'los campos tienen un formato incorrecto'}).encode('utf-8'))
            except Exception as e:
                logging.exception(f"Error inesperado durante la validación: {str(e)}")
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Error interno del servidor'}).encode('utf-8'))



            except Exception as e:
                logging.exception(f"Error inesperado durante la validación: {str(e)}")



            

            

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


