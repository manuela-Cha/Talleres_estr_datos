#from Practica_1.Investigador import Investigador
from Laboratorio_no_2.Usuario import Usuario
from Practica_1.carga_archivos import carga
from Laboratorio_no_4.Lista_doble import DoubleList
from Practica_1.carga_archivos import carga
from Practica_1.Investigador import Investigador
from Practica_1.Equipo import Equipo

class Administrador(Usuario):
    
    def __init__(self, contrasena, nombre, cedula, fecha_nacimiento, ciudad_nacimiento, telefono, correo_electronico, direccion):
        self.contrasena = contrasena
        self.nombre = nombre
        self.cedula = cedula 
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.direccion = direccion


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
            with open("Practica_1/Empleados.txt", "a") as file: 
                file.write("{} {} {} {} {} {}\n".format(usuario_agregado.getNombre(), usuario_agregado.getId(), usuario_agregado.getFecha_nacimiento(), usuario_agregado.getTel(), usuario_agregado.getEmail(), usuario_agregado.getDir()))      
        except:
            print("No se pudo escribir en Empleados")


    def eliminar_usuario(self):
        cedula = input("Ingrese el número de cédula del usuario que desea eliminar: ")
        if carga.eliminar_usuario_Password_datos(cedula) and carga.eliminar_usuario_Empleados_datos(cedula):
            print("El usuario ha sido eliminado.")
            return True
        
        else:
            print("No se encontró un usuario con esta cédula.")
            return False
    
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

   
    def actualizar_control_cambio(self):
        return
    
    # FALTA PROBAR
    def agregar_nuevo_equipo(self):
        cedula_investigador = ""
        contrasena_investigador = ""
        nombre_equipo = ""
        numero_placa = ""
        fecha_compra = ""
        valor_compra = ""
        lista_solicitudes = DoubleList()
        with open("Practica_1/solicitudes_agregar.txt", "a") as file:
            nodo_actual = lista_solicitudes.first()
            while nodo_actual:
                datos = nodo_actual.data.split(" ") 
                datos[0] = cedula_investigador
                datos[1] = contrasena_investigador
                datos[2] = nombre_equipo
                datos[3] = numero_placa
                datos[4] = fecha_compra
                datos[5] = valor_compra
                nodo_actual = nodo_actual.next
        equipo = Equipo(nombre_equipo, numero_placa, fecha_compra, valor_compra)  
        nombre,cedula_investigador,fecha_nacimiento,ciudad_nacimiento,tel,email,dir = carga.inicializador(cedula_investigador)
        investigador = Investigador(contrasena_investigador,nombre, cedula_investigador, fecha_nacimiento, ciudad_nacimiento, tel, email, dir )
        investigador.equipos.addLast(equipo)

        with open("Practica_1/inventarioGeneral.txt", "r") as archivo:
            lineas = archivo.readlines()

        usuario_encontrado = False

        for i, linea in enumerate(lineas):
            datos = linea.strip().split(" ")
            if datos[0] == investigador.nombre: 
                nueva_linea = "Nueva información que deseas agregar\n".format(investigador.nombre, investigador.cedula, equipo.get_nombre(), equipo.get_numero_placa(), equipo.get_valor_compra()) 
                lineas.insert(i + 1, nueva_linea)  
                usuario_encontrado = True
                break

        if not usuario_encontrado:
            print(f"Nombre no encontrado.")
        else:
            with open("Practica_1/inventarioGeneral.txt", "w") as archivo:
                archivo.writelines(lineas)
            print(f"Equipo agregado correctamente.")

        
    
    def revision_solicitudes_eliminacion_equipos(self):
        return 
    
    def revision_solicitudes_eliminacion_equipos(self):
        return
    
    def notificacion_respuesta_solicitud(self):
        return
    
    def eliminar_equipo(self):
        return 
    
    def agregar_equipo(self):
        return
    
    def generar_txt_inventario_investigador(self, id_investigador):
        return
    
    def generar_txt_inventario_general(self ):
        return
    
    def generar_control_de_cambios(self):
        return 
    
    def generar_txt_solicitudes_agregar(self):
        return
    
    def generar_txt_solicitudes_eliminar(self):
        return
    
    def __str__(self):
        return f"{self.nombre} {self.fecha_nacimiento} {self.ciudad_nacimiento} {self.telefono} {self.correo_electronico} {self.direccion}\n"