import re as re
from Laboratorio_no_4.Lista_doble import DoubleList
from Laboratorio_no_2.Fecha import Fecha
from Practica_1.Solicitud import Solicitud
from Practica_1.Equipo import Equipo
from Practica_1.Factory_usuarios import Factory_Usuario

class GestionUsuarios:
    @staticmethod
    def cargar_Password_en_lista():
        lista = DoubleList()
        try:
            with open("Practica_1/Password.txt", "r") as file:
                for line in file:
                    lista.addLast(line.strip())
        except FileNotFoundError:
            print(f"Archivo no encontrado")
        return lista

    @staticmethod
    def validacion_datos(cedula, contraseña, lista_usuarios):
        nodo_actual = lista_usuarios.first()
        while nodo_actual:
            if nodo_actual.data.Id == str(cedula) and nodo_actual.data.contrasena == str(contraseña):
                return True 
            nodo_actual = nodo_actual.next
        return False 

    @staticmethod
    def investigador_o_admin_datos(cedula, lista_password):
        nodo_actual = lista_password.first()
        while nodo_actual:
            datos = nodo_actual.data.split(" ")
            if datos[0] == cedula:
                return datos[2]
            nodo_actual = nodo_actual.next
        return False

    @staticmethod
    def eliminar_usuario_Password_datos(cedula, listas):
        nodo_actual = listas['todos'].first()
        
        if nodo_actual is None:
            print("La lista está vacía.")
            return False

        nodo_a_eliminar = None
        while nodo_actual:
            datos = nodo_actual.data
            if datos.getId() == str(cedula):
                nodo_a_eliminar = nodo_actual
                break
            nodo_actual = nodo_actual.next
        
        if nodo_a_eliminar:
            datos = nodo_a_eliminar.data
            if Factory_Usuario.es_instancia(datos) == "administrador":
                admin_node = listas['admins'].encontrar_nodo(datos)
                if admin_node:
                    listas['admins'].remove(admin_node)
            elif Factory_Usuario.es_instancia(datos) == "investigador":
                invest_node = listas['investigadores'].encontrar_nodo(datos)
                if invest_node:
                    listas['investigadores'].remove(invest_node)
            
            listas['todos'].remove(nodo_a_eliminar)
            return True
        print(f"No se encontró un usuario con la cédula {cedula}.")
        return False

    @staticmethod
    def eliminar_usuario_de_txt(cedula):
        try:
            with open("Practica_1/Empleados.txt", "r") as file:
                lineas = file.readlines()
            nuevas_lineas = [linea for linea in lineas if linea.strip().split()[1] != str(cedula)]

            with open("Practica_1/Empleados.txt", "w") as file:
                file.writelines(nuevas_lineas)

            with open("Practica_1/Password.txt", "r") as file1:
                lineas1 = file1.readlines()
            nuevas_lineasp = [linea for linea in lineas1 if linea.strip().split()[0] != str(cedula)]

            with open("Practica_1/Password.txt", "w") as file1:
                file1.writelines(nuevas_lineasp)
            
        except FileNotFoundError:
            print("Error: Archivo no encontrado.")
        except IndexError:
            print("Error: Formato inesperado en el archivo.")
        except Exception as e:
            print(f"Error inesperado: {e}")

    @staticmethod
    def cargar_equipos(usuario, archivo="Practica_1/InventarioGeneral.txt"):
        try:
            with open(archivo, 'r', encoding='utf-8') as file:
                for linea in file:
                    datos = linea.strip().split()
                    if datos[1] == usuario.getId():
                        fecha = Fecha(datos[4], datos[5], datos[6])
                        equipo = Equipo(datos[2], datos[3], fecha, datos[7])
                        usuario.equipos.addLast(equipo)
        except FileNotFoundError as e:
            print(f"Error: {e}")

    @staticmethod
    def cargar_solicitudes(usuario, archivos):
        for archivo, tipo in archivos.items():
            try:
                with open(archivo, "r") as file:
                    for linea in file:
                        datos = linea.strip().split()
                        if datos[1] == usuario.getId():
                            solicitud = Solicitud(tipo, datos[3], "pendiente")
                            usuario.solicitudes.addLast(solicitud)
            except FileNotFoundError:
                continue