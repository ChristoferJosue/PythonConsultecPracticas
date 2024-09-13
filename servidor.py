import http.server
import socketserver
import json

#definir el puerto en el que ejecutara el servidor
puerto = 8080

#crear clase para el manejador de particiones
class MiHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        #Enviar resp exitosa
        self.send_response(200)

        #establecer cabecera de la resp
        self.send_header('Content-type','application/json')
        self.end_headers()

        #crear diccionarion para el cont de la resp formaot json

        respuesta_json = {'mensaje': 'Hola, este es un servidor web basico en Python'}

        #convertir el diccionario en json y enviar cont
        respuesta_json_str = json.dumps(respuesta_json)
        self.wfile.write(respuesta_json_str.encode('utf-8'))

#bakabaka
with socketserver.TCPServer(('',puerto),MiHandler) as servidor:
    print(f'Servidor web iniciado en el puerto {puerto}.')

    servidor.serve_forever()

 