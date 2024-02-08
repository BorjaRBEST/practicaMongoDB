import Conexion
import Metodos
import Menu

class Main:
    if __name__ == "__main__":
        uri = "mongodb+srv://borjarodriguez203:medac123@clustermedac.pzeoa6p.mongodb.net/?retryWrites=true&w=majority"
        conexion = Conexion.Conexion(uri)
        metodos = Metodos.Metodos(conexion)
        menu = Menu.Menu(metodos)
        menu.menu_principal()
