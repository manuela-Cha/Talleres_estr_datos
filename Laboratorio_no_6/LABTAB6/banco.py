from nodo_simple import NodoSimple, ListaSimple
from queue import Queue
from stack import Stack
from usuario import Usuario

class TurnoUsuario:
    def __init__(self):
        self.registro = Queue()
        self.usuarioAtendidos = Stack()

    def registrar(self, usuario):
        self.registro.enqueue(usuario)

    def atenderSiguiente(self):
        usuario = self.registro.dequeue()
        if usuario:
            self.usuarioAtendidos.push(usuario)
        return usuario

    def toFile(self):
        with open("usuariospendientes.txt", "w") as pendientes:
            actual = self.registro.lista.cabeza
            while actual:
                pendientes.write(f"{actual.dato.get_nombre()} {actual.dato.get_id()}\n")
                actual = actual.siguiente

        with open("usuariosatendidos.txt", "w") as atendidos:
            actual = self.usuarioAtendidos.lista.cabeza
            while actual:
                atendidos.write(f"{actual.dato.get_nombre()} {actual.dato.get_id()}\n")
                actual = actual.siguiente

    def fromFile(self):
        try:
            with open("usuariospendientes.txt", "r") as pendientes:
                for line in pendientes:
                    nombre, id = line.strip().split()
                    self.registro.enqueue(Usuario(nombre, int(id), None, None, None))
        except FileNotFoundError:
            pass

# Pruebas sugeridas
if __name__ == "__main__":
    sistema = TurnoUsuario()
    sistema.fromFile()

    while True:
        print("\nMenú:")
        print("1. Registrar usuario")
        print("2. Atender siguiente usuario")
        print("3. Guardar en archivo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            id = int(input("Ingrese el ID del usuario: "))
            usuario = Usuario(nombre, id, None, None, None)
            sistema.registrar(usuario)
        elif opcion == "2":
            usuario = sistema.atenderSiguiente()
            if usuario:
                print(f"Atendiendo a: {usuario.get_nombre()} {usuario.get_id()}")
            else:
                print("No hay usuarios en la cola.")
        elif opcion == "3":
            sistema.toFile()
            print("Datos guardados en archivo.")
        elif opcion == "4":
            sistema.toFile()
            break
        else:
            print("Opción no válida. Intente de nuevo.")
