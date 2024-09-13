import http.server
import socketserver
import dicttoxml
import database  # Asegúrate de que este módulo esté disponible

# Definir el puerto en el que ejecutará el servidor
puerto = 8088

# Crear clase para el manejador de peticiones
class MiHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Enviar respuesta exitosa
        self.send_response(200)

        # Establecer cabecera de la respuesta
        self.send_header('Content-type', 'application/xml')
        self.end_headers()

        # Obtener datos JSON de la base de datos
        respuesta_json = database.obtener_usuarios()

        # Convertir el diccionario JSON a XML
        respuesta_xml = dicttoxml.dicttoxml(respuesta_json)
        #print(respuesta_json)

        # Enviar contenido XML
        self.wfile.write(respuesta_xml)

# Iniciar el servidor
with socketserver.TCPServer(('', puerto), MiHandler) as servidor:
    print(f'Servidor web iniciado en el puerto {puerto}.')
    servidor.serve_forever()
