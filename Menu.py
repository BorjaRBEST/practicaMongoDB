class Menu:
    def __init__(self, metodos):
        self.metodos = metodos

    # Menú principal en el que se realizan las diferentes opciones
    def menu_principal(self):
        while True:
            print("1. Insertar documento")
            print("2. Actualizar documento")
            print("3. Reemplazar documento")
            print("4. Eliminar documento")
            print("5. Mostrar todos los documentos")
            print("6. Búsqueda de documento")
            print("7. Eliminar todos los documentos")
            print("8. Exportar a CSV")
            print("9. Importar desde CSV")
            print("10. Exportar a JSON")
            print("11. Importar desde JSON")
            print("12. Salir")

            choice = input("Seleccione una opción: ")

            if choice == '1':
                collection_name = input("Ingrese el nombre de la colección: ")
                pokemon_data = self.metodos.input_pokemon_data()
                self.metodos.insert_document(collection_name, pokemon_data)
            elif choice == '2':
                collection_name = input("Ingrese el nombre de la colección: ")
                query = self.metodos.input_query(collection_name)  # Pasa el nombre de la colección como argumento
                new_values = self.metodos.input_update_values(collection_name)  # También pasa el nombre de la colección aquí
                self.metodos.update_document(collection_name, query, new_values)
            elif choice == '3':
                collection_name = input("Ingrese el nombre de la colección: ")
                query = self.metodos.input_query(collection_name)  # Pasa el nombre de la colección como argumento
                document = self.metodos.input_replace_document(collection_name)  # Y aquí también
                self.metodos.replace_document(collection_name, query, document)
            elif choice == '4':
                collection_name = input("Ingrese el nombre de la colección: ")
                query = self.metodos.input_query(collection_name)  # Pasa el nombre de la colección como argumento
                self.metodos.delete_document(collection_name, query)
            elif choice == '5':
                collection_name = input("Ingrese el nombre de la colección: ")
                documents = self.metodos.find_documents(collection_name)
                for doc in documents:
                    print(doc)
            elif choice == '6':
                collection_name = input("Ingrese el nombre de la colección: ")
                query = self.metodos.input_query(collection_name)  # Pasa el nombre de la colección como argumento
                document = self.metodos.search_document(collection_name, query)
                print(document)
            elif choice == '7':
                collection_name = input("Ingrese el nombre de la colección: ")
                self.metodos.delete_all_documents(collection_name)
                print("Todos los documentos han sido eliminados.")
            elif choice == '8':
                collection_name = input("Ingrese el nombre de la colección: ")
                csv_filename = input("Ingrese el nombre del archivo CSV de destino: ")
                self.metodos.export_to_csv(collection_name, csv_filename)
            elif choice == '9':
                collection_name = input("Ingrese el nombre de la colección: ")
                csv_filename = input("Ingrese el nombre del archivo CSV a importar: ")
                self.metodos.import_from_csv(collection_name, csv_filename)
            elif choice == '10':
                collection_name = input("Ingrese el nombre de la coleccion: ")
                json_filename = input("Ingrese el nombre del archivo JSON a importar: ")
                self.metodos.export_to_json(collection_name, json_filename)
                print("Los datos han sido correctamente exportados a JSON")
            elif choice == '11':
                collection_name = input("Ingrese el nombre de la coleccion: ")
                json_filename = input("Ingrese el nombre del archivo JSON a importar: ")
                self.metodos.import_from_json(collection_name, json_filename)
            elif choice == '12':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
