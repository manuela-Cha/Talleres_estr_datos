from Laboratorio_no_2.Usuario import Usuario
from Practica_1.carga_archivos import carga
from Laboratorio_no_4.Lista_doble import DoubleList
from Practica_1.Investigador import Investigador
from Practica_1.Equipo import Equipo
from Laboratorio_no_2.Fecha import Fecha
from Laboratorio_no_4.Nodo_doble import DoubleNode

class Administrador(Usuario):
    
    def __init__(self, contrasena, nombre, Id, fecha_nacimiento, ciudad_nacimiento, telefono, correo_electronico, direccion):
        self.contrasena = contrasena
        self.nombre = nombre
        self.Id = Id
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.direccion = direccion

    #Linea de archivos siempre en la ultima linea sin saltos de linea LISTA
    def registrar_nuevo_usuario(self):
        usuario_agregado = Usuario.solicitar()
        try:
            with open("Practica_1/Password.txt", "a") as file:
                rol = input("Rol: ")
                contrasena = input("Contrasena: ")
                file.write("{} {} {}\n".format(usuario_agregado.getId(), contrasena, rol)) 
        except:
            print("No se pudo escribir en Password")

        try: 
            with open("Practica_1/Empleados.txt", "a") as file1:
                file1.write("{} {} {} {} {} {}\n".format(usuario_agregado.getNombre(), usuario_agregado.getId(), usuario_agregado.getFecha_nacimiento(), usuario_agregado.getTel(), usuario_agregado.getEmail(), usuario_agregado.getDir()))      
        except:
            print("No se pudo escribir en Empleados")

    # LISTA
    def eliminar_usuario(self):
        cedula = input("Ingrese el número de cédula del usuario que desea eliminar: ")
        if carga.eliminar_usuario_Password_datos(cedula) and carga.eliminar_usuario_Empleados_datos(cedula):
            print("El usuario ha sido eliminado.")
            return True
        
        else:
            print("No se encontró un usuario con esta cédula.")
            print(carga.eliminar_usuario_Empleados_datos)
            return False
        
    #LISTA
    def cambiar_contrasena(self):
        cedula = input("Ingrese el número de cédula del usuario que desea cambiar su contraseña: ")
        nueva_contrasena = input("Ingrese la contraseña nueva: ")
        try:
            with open("Practica_1/Password.txt", "r") as archivo:
                lineas = archivo.readlines()
            usuario_encontrado = False
            for i, linea in enumerate(lineas):
                datos = linea.strip().split(" ") 
                if datos[0] == cedula: 
                    datos[1] = nueva_contrasena 
                    lineas[i] = " ".join(datos) + "\n"  
                    usuario_encontrado = True
                    break
            if not usuario_encontrado:
                print(f"Cedula {cedula} no encontrada.")
                return False
            with open("Practica_1/Password.txt", "w") as archivo:
                archivo.writelines(lineas)
            print(f"La contraseña de {cedula} se ha actualizado correctamente.")
            return True
        
        except FileNotFoundError:
            print("El archivo no existe.")
            return False

    
    def seleccionar_equipo(numero_placa=None):
        lista_equipos_solicitados = DoubleList()
        with open("Practica_1/solicitudes_agregar.txt", "r") as file:
                lineas = file.readlines()
                for linea in lineas:
                    datos = linea.strip().split()
                    equipo = Equipo(datos[2], datos[3], datos[4:7], datos[7])
                    if equipo.get_numero_placa() == str(numero_placa):
                        return equipo
                    lista_equipos_solicitados.addLast(equipo)
        if numero_placa == None:
            return lista_equipos_solicitados
        
    def eliminar_lineas(archivo):
        try:
            with open(archivo, "r", encoding="utf-8") as file:
                lineas = file.readlines()
            lineas_actualizadas = [""]
            with open(archivo, "w", encoding="utf-8") as file:
                file.writelines(lineas_actualizadas)
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")

        
            

    def visualizar_solicitudes_agregar(self):
        try:
            with open("Practica_1/solicitudes_agregar.txt", "r") as file:
                lineas = file.readlines()
                for linea in lineas:
                    datos = linea.strip().split()
                    decision = input(f"{linea}\n¿Tomar decisión? (s/n): ").lower()
                    if decision == "s":

                        nodo_actual = carga.lista_investigadores_y_administradores.first()
                        while nodo_actual:
                            if nodo_actual.data.Id == str(datos[1]):
                                nuevo_nodo = DoubleNode(Administrador.seleccionar_equipo(datos[3]))
                                nodo_actual.data.equipos.addLast(nuevo_nodo)
                                nodo_actual.data.solicitudes["agregar_equipo: {}".format(datos[3])] = 'aprobada'
                                break
                            nodo_actual = nodo_actual.next
                        
                        nodo_actual = carga.lista_investigadores.first()
                        while nodo_actual:
                            if nodo_actual.data.Id == str(datos[1]):
                                nuevo_nodo = DoubleNode(Administrador.seleccionar_equipo(datos[3]))
                                nodo_actual.data.equipos.addLast(nuevo_nodo)
                                nodo_actual.data.solicitudes["agregar_equipo: {}".format(datos[3])] = 'aprobada'
                                break
                            nodo_actual = nodo_actual.next
                        try:
                            with open("Practica_1/Control_de_cambios.txt", "a") as file:
                                file.write("{} {} {}\n".format(datos[1], datos[3], "agregar", datos[4])) 
                                print( "escrito exitosamente en el control de cambios")
                        except:
                            print("No se pudo escribir en control de cambios el agregar")
                    else:
                        nodo_actual = carga.lista_investigadores.first()
                        while nodo_actual:
                            if nodo_actual.data.Id == str(datos[1]):
                                nodo_actual.data.solicitudes["agregar_equipo: {}".format(datos[3])] = 'rechazada'
                                break
                            nodo_actual = nodo_actual.next
                Administrador.eliminar_lineas("Practica_1/solicitudes_agregar.txt")
        except FileNotFoundError:
            print("Error: El archivo no existe.")


    """def visualizar_solicitudes_eliminar(self):
        try:
            with open("Practica_1/solicitudes_eliminar.txt", "r") as file:
                lineas = file.readlines()
                for linea in lineas:
                    datos = linea.strip().split()
                    decision = input(f"{linea}\n¿Tomar decisión? (s/n): ").lower()
                    if decision == "s":
                        investigador = carga.obtener_investigadores(datos[1]).first().getData()
                        investigador.eliminar_equipo(str(datos[3]))
                    
                        solicitudes = carga.obtener_investigadores(datos[1]).first().getData().getSolicitudes()
                        solicitudes["eliminar_equipo: {}".format(datos[3])] = 'aprobada'
                        
                        nodo_actual = carga.lista_investigadores_y_administradores.first()
                        print("nodo actual", nodo_actual)
                        while nodo_actual:
                            if nodo_actual.data.Id == str(datos[1]):
                                nuevo_nodo = DoubleNode(Administrador.seleccionar_equipo(datos[3]))
                                nodo_actual.data.equipos.addLast(nuevo_nodo)
                                nodo_actual.data.solicitudes["agregar_equipo: {}".format(datos[3])] = 'aprobada'
                                break
                            nodo_actual = nodo_actual.next
                        
                        nodo_actual = carga.lista_investigadores.first()
                        while nodo_actual:
                            if nodo_actual.data.Id == str(datos[1]):
                                nuevo_nodo = DoubleNode(Administrador.seleccionar_equipo(datos[3]))
                                nodo_actual.data.equipos.addLast(nuevo_nodo)
                                nodo_actual.data.solicitudes["agregar_equipo: {}".format(datos[3])] = 'aprobada'
                                break
                            nodo_actual = nodo_actual.next

                        try:
                            with open("Practica_1/Control_de_cambios.txt", "a") as file:
                                file.write("{} {} {}\n".format(datos[1], datos[3], "eliminar", datos[4])) 
                                print( "escrito exitosamente en el control de cambios")
                        except:
                            print("No se pudo escribir en control de cambios el agregar")
                    else:
                        investigador.solicitudes["eliminar_equipo: {}".format(datos[1])] = 'rechazada'
        except FileNotFoundError:
            print("Error: El archivo no existe.")"""
    
    def generar_txt_inventario_investigador(self):
        id_investigador = input("Ingrese la cedula del investigador: ")
        nodo_actual = carga.lista_investigadores.first()
        while nodo_actual:
            if nodo_actual.data.Id == str(id_investigador):
                ruta_archivo = "{}-desdeAdmin.txt".format(nodo_actual.data.getNombre())
                with open(ruta_archivo, "w", encoding="utf-8") as archivo:    
                    archivo.write(str(nodo_actual.data.equipos))
                break
            nodo_actual = nodo_actual.next
        return
    
    def generar_txt_inventario_general(self ):
        id_investigador = input("Ingrese la cedula del investigador: ")
        nodo_actual = carga.lista_investigadores.first()
        while nodo_actual:
            if nodo_actual.data.Id == str(id_investigador):
                ruta_archivo = "{}-desdeAdmin.txt".format(nodo_actual.data.getNombre())
                with open(ruta_archivo, "w", encoding="utf-8") as archivo:    
                    archivo.write(str(nodo_actual.data.equipos))
                break
            nodo_actual = nodo_actual.next
        return
    
    def generar_control_de_cambios(self):
        return 
    
    def generar_txt_solicitudes_agregar(self):
        return
    
    def generar_txt_solicitudes_eliminar(self):
        return
    
    def __str__(self):
        return f"{self.nombre} {self.Id} {self.fecha_nacimiento} {self.ciudad_nacimiento} {self.telefono} {self.correo_electronico} {self.direccion}\n"