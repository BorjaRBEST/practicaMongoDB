import Conexion
import Metodos
import Menu

class Main:
    try:
        if __name__ == "__main__":
            # URI de conexión a la base de datos MongoDB
            uri = "mongodb+srv://borjarodriguez203:medac123@clustermedac.pzeoa6p.mongodb.net/?retryWrites=true&w=majority"
            # Creamos una instancia de la clase Conexion, pasando la URI como argumento
            conexion = Conexion.Conexion(uri)
            # Creamos una instancia de la clase Metodos, pasando la instancia de Conexion como argumento
            metodos = Metodos.Metodos(conexion)
            # Creamos una instancia de la clase Menu, pasando la instancia de Metodos como argumento
            menu = Menu.Menu(metodos)
            # Llamamos al método menu_principal() para iniciar el programa
            menu.menu_principal()
    except KeyboardInterrupt:
        print("Programa detenido por el usuario")
