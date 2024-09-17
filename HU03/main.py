# main.py
from http.server import HTTPServer
from servidor import RequestHandler
from database import init_db,insert_user

# Inicializar la base de datos
init_db()

# Configurar y correr el servidor
port = 8081
server_address = ('', port)
httpd = HTTPServer(server_address, RequestHandler)
print(f"Servidor en ejecución en el puerto {port}")
httpd.serve_forever()
