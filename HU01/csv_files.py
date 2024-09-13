import csv

# Guardar los usuarios en un archivo CSV
def guardar_datos_csv(usuarios):
    with open('usuarios.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nombre', 'Edad', 'Extranjero'])
        for usuario in usuarios:
            nombre = usuario['nombre']
            edad = usuario['edad']
            extranjero = usuario['extranjero']
            writer.writerow([nombre, edad, extranjero])