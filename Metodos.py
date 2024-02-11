import csv
import json


class Metodos:
    def __init__(self, connection, db_name='pokeplaza'):
        self.client = connection.get_client()
        self.db = self.client[db_name]

    def insert_document(self, collection_name, document):
        collection = self.db[collection_name]
        return collection.insert_one(document)

    def update_document(self, collection_name, query, new_values):
        collection = self.db[collection_name]
        return collection.update_many(query, {"$set": new_values})

    def replace_document(self, collection_name, query, document):
        collection = self.db[collection_name]
        return collection.replace_one(query, document)

    def delete_document(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query)

    def find_documents(self, collection_name, query={}):
        collection = self.db[collection_name]
        return collection.find(query)

    def search_document(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def delete_all_documents(self, collection_name):
        collection = self.db[collection_name]
        return collection.delete_many({})

    def show_all_documents(self, collection_name):
        collection = self.db[collection_name]
        return collection.find()

    def input_pokemon_data(self):
        pokemon_data = {}
        pokemon_data['nombre'] = input("Ingrese el nombre del Pokémon: ")
        pokemon_data['tipo'] = input("Ingrese el tipo del Pokémon: ")
        pokemon_data['nivel'] = int(input("Ingrese el nivel del Pokémon: "))
        return pokemon_data
    def input_update_values(self, collection_name):
        field_name = input(f"Ingrese el nombre del campo a actualizar en la colección {collection_name}: ")
        field_value = input("Ingrese el nuevo valor para {}: ".format(field_name))
        return {"$set": {field_name: field_value}}

    def input_replace_document(self, collection_name):
        field_name = input(f"Ingrese el nombre del campo en la colección {collection_name}: ")
        field_value = input("Ingrese el valor para {}: ".format(field_name))
        return {field_name: field_value}

    def input_query(self, collection_name):
        field_name = input(f"Ingrese el nombre del campo para la consulta en la colección {collection_name}: ")
        field_value = input("Ingrese el valor para {}: ".format(field_name))
        return {field_name: field_value}

    def export_to_csv(self, collection_name, csv_filename):
        if not csv_filename.endswith('.csv'):
            csv_filename += '.csv'  # Agrega la extensión CSV si no está presente

        # Obtener los documentos de la colección
        documents = list(self.find_documents(collection_name))

        # Abrir el archivo CSV en modo escritura
        with open(csv_filename, 'w', newline='') as csvfile:
            # Crear un escritor CSV
            csv_writer = csv.writer(csvfile)

            # Escribir el encabezado basado en las claves del primer documento
            if documents:  # Verifica si hay documentos en la lista
                header = list(documents[0].keys())
                csv_writer.writerow(header)

            # Escribir los documentos
            for doc in documents:
                csv_writer.writerow(list(doc.values()))

        print(f'Los datos de la colección {collection_name} han sido exportados a {csv_filename}')

    def import_from_csv(self, collection_name, csv_filename):
        if not csv_filename.endswith('.csv'):
            print("El archivo proporcionado no es un archivo CSV válido.")
            return

        # Conectar con la colección
        collection = self.db[collection_name]

        # Leer los datos del archivo CSV y agregarlos a la colección
        with open(csv_filename, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                # Insertar el documento en la colección
                collection.insert_one(row)

        print(f'Los datos del archivo CSV {csv_filename} han sido importados a la colección {collection_name}')

    def export_to_json(self, collection_name, json_filename):
        # Obtener los documentos de la colección
        documents = list(self.find_documents(collection_name))

        # Abrir el archivo JSON en modo escritura
        with open(json_filename, 'w') as json_file:
            # Utilizar json.dump() para escribir los documentos en formato JSON
            json.dump(documents, json_file, default=str)

        print(f'Los datos de la colección {collection_name} han sido exportados a {json_filename}')

    def import_from_json(self, collection_name, json_filename):
            if not json_filename.endswith('.json'):
                print("El archivo proporcionado no es un archivo JSON válido.")
                return

            # Conectar con la colección
            collection = self.db[collection_name]

            # Leer los datos del archivo JSON y agregarlos a la colección
            with open(json_filename, 'r') as json_file:
                json_data = json.load(json_file)
                if isinstance(json_data, list):
                    for document in json_data:
                        # Insertar el documento en la colección
                        collection.insert_one(document)
                    print(
                        f'Los datos del archivo JSON {json_filename} han sido importados a la colección {collection_name}')
                else:
                    print("El contenido del archivo JSON no es una lista de documentos.")