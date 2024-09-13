import sqlite3
conexion =sqlite3.connect('mi_base_de_datos.bd')
cursor = conexion.cursor()

cursor.execute(''' CREATE TABLE usuarios(id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

#Insertar Datos en la tabla 
cursor.execute("INSERT INTO usuarios(nombre, edad) VALUES (?,?)", ('Luis Perez',30))
cursor.execute("INSERT INTO usuarios(nombre, edad) VALUES (?,?)", ('Christofer Gonzalez',30))

conexion.commit()

cursor.execute("SELECT * FROM usuarios")

resultados = cursor.fetchall()

# imrpimir resultados 
for fila in resultados:
    print(fila)
#cerrar cursor 


cursor.close()
conexion.close()



