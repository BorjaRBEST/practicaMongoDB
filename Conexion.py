from pymongo import MongoClient

# Clase Conexion donde ubicamos pymongo para llamarlo en el Main
class Conexion:
    # Constructor de la clase, recibe la URI de conexión como parámetro
    def __init__(self, uri):
        # Creamos una instancia de MongoClient utilizando la URI proporcionada
        self.client = MongoClient(uri)

    # Método para obtener el cliente de conexión a la base de datos qie devuelve el cliente de conexión
    def get_client(self):
        return self.client
