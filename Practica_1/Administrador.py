from Laboratorio_no_2.Usuario import Usuario
from Laboratorio_no_4.Lista_doble import DoubleList
from Practica_1.Equipo import Equipo
from datetime import datetime

class Administrador(Usuario):
    
    def __init__(self, contrasena, nombre, Id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir):
        self.contrasena = contrasena
        self.nombre = nombre
        self.Id = Id
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.tel = tel
        self.email = email
        self.dir = dir
        self.equipos = DoubleList()

    def registrar_nuevo_usuario(self):
        from Practica_1.carga_archivos import carga
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
        carga.inicializar_empleado()
        

    # LISTA A MAS NO PODER
    def eliminar_usuario(self):
        from Practica_1.carga_archivos import carga
        cedula = input("Ingrese el número de cédula del usuario que desea eliminar: ")
        carga.eliminar_usuario_Password_datos(cedula)
        carga.eliminar_usuario_de_txt(cedula)
        
    #LISTA A MAS NO PODER
    def cambiar_contrasena(self):
        from Practica_1.carga_archivos import carga
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
        except FileNotFoundError:
            print("El archivo no existe.")   

        nodo_actual = carga.lista_investigadores_y_administradores.first()
        while nodo_actual:
            datos = nodo_actual.data
            if datos.getId() == str(cedula):
                nodo_actual.data.contrasena = nueva_contrasena
                break
            nodo_actual = nodo_actual.next
    
    def crear_equipo_solicitado(numero_placa):
        """Crea el objeto equipo solicitado y lo retorna"""
        with open("Practica_1/solicitudes_agregar.txt", "r") as file:
                lineas = file.readlines()
                for linea in lineas:
                    datos = linea.strip().split()
                    if datos[3] == str(numero_placa):
                        fecha = " ".join(datos[4:7])
                        equipo = Equipo(datos[2], datos[3], fecha , datos[7])
                        return equipo
                    
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
        from Practica_1.carga_archivos import carga
        try:
            with open("Practica_1/solicitudes_agregar.txt", "r") as file:
                lineas = file.readlines()
                for linea in lineas:
                    datos = linea.strip().split()
                    nombre_solicitante = datos[0]
                    cedula_solicitante = datos[1]
                    nombre_equipo = datos[2]
                    numero_placa = datos[3]
                    dia_compra = datos[4]
                    mes_compra = datos[5]
                    anio_compra = datos[6]
                    valor_precio = datos[7]
                    hora_actual = datetime.now().strftime("%H %M %S") + f".{datetime.now().microsecond}"

                    decision = input(f"{linea}\n¿Tomar decisión? (s/n): ").lower()
                    if decision == "s":
                        with open("Practica_1/InventarioGeneral.txt", "a") as archivo:  
                            archivo.write("{} {} {} {} {} {} {} {}\n".format(nombre_solicitante, cedula_solicitante, nombre_equipo, numero_placa, dia_compra, mes_compra, anio_compra, valor_precio ))
                        carga.carga_equipos_existentes()
                        try:
                            with open("Practica_1/Control_de_cambios.txt", "a") as file:
                                file.write("{} {} {} {} {} {} {} {}\n".format(cedula_solicitante, numero_placa, "agregar", dia_compra, mes_compra, anio_compra, hora_actual,"Aprobada")) 
                        except:
                            print("No se pudo escribir en control de cambios el agregar")
                    else:
                        try:
                            with open("Practica_1/Control_de_cambios.txt", "a") as file:
                                file.write("{} {} {} {} {} {} {} {}\n".format(cedula_solicitante, numero_placa, "agregar", dia_compra, mes_compra, anio_compra, hora_actual,"Rechazada")) 
                        except:
                            print("No se pudo escribir en control de cambios el agregar")
                
                Administrador.eliminar_lineas("Practica_1/solicitudes_agregar.txt")
                carga.carga_solicitudes_existentes()
        except FileNotFoundError:
            print("Error: El archivo no existe.")


    def visualizar_solicitudes_eliminar(self):
        from Practica_1.carga_archivos import carga
        
        try:
            with open("Practica_1/solicitudes_eliminar.txt", "r") as file:
                lineas = file.readlines()
                for linea in lineas:
                    datos = linea.strip().split()
                    numero_placa = datos[3]
                    cedula_solicitante = datos[1]
                    numero_placa = datos[3]
                    dia_compra = datos[4]
                    mes_compra = datos[5]
                    anio_compra = datos[6]
                    hora_actual = datetime.now().strftime("%H %M %S") + f".{datetime.now().microsecond}"
                    decision = input(f"{linea}\n¿Tomar decisión? (s/n): ").lower()
                    if decision == "s":
                        with open("Practica_1/InventarioGeneral.txt", "r") as file:
                            lineas = file.readlines()
                            nuevas_lineas = [linea for linea in lineas if linea.strip().split()[3] != str(numero_placa)]

                        with open("Practica_1/InventarioGeneral.txt", "w") as file:
                            file.writelines(nuevas_lineas)
                        carga.carga_equipos_existentes()
                        try:
                            with open("Practica_1/Control_de_cambios.txt", "a") as file:
                                file.write("{} {} {} {} {} {} {} {}\n".format(cedula_solicitante, numero_placa, "eliminar", dia_compra, mes_compra, anio_compra, hora_actual,"Aprobada")) 
                        except:
                            print("No se pudo escribir en control de cambios el eliminar")
                    else:
                        try:
                            with open("Practica_1/Control_de_cambios.txt", "a") as file:
                                file.write("{} {} {} {} {} {} {} {}\n".format(cedula_solicitante, numero_placa, "eliminar", dia_compra, mes_compra, anio_compra, hora_actual,"Rechazada")) 
                        except:
                            print("No se pudo escribir en control de cambios el eliminar")
                Administrador.eliminar_lineas("Practica_1/solicitudes_eliminar.txt")
                carga.carga_solicitudes_existentes()
        except FileNotFoundError:
            print("Error: El archivo no existe.")
    
    def generar_txt_inventario_investigador(self):
        from Practica_1.carga_archivos import carga
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
        from Practica_1.carga_archivos import carga
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
    
    def agregar_un_equipo_al_inventario(self):
        """Agrega un equipo al inventario"""
        from Practica_1.carga_archivos import carga
        
        nombre_solicitante = self.nombre
        cedula_solicitante = self.Id
        nombre_equipo = input("Nombre del equipo: ")
        numero_placa = input("Numero de placa del equipo: ")
        dia_compra = input("Día de compra del equipo: ")
        mes_compra = input("Mes de compra del equipo: ")
        anio_compra = input("Año de compra del equipo: ")
        valor_precio = input("Precio del equipo: ")
        
        with open("Practica_1/InventarioGeneral.txt", "a") as archivo:  
            archivo.write("{} {} {} {} {} {} {} {}\n".format(nombre_solicitante, cedula_solicitante, nombre_equipo, numero_placa, dia_compra, mes_compra, anio_compra, valor_precio ))
        carga.carga_equipos_existentes()
    
    def mostrar_equipos(self):
        print(self.equipos)
        return

    
    def generar_txt_solicitudes_agregar(self):
        return
    
    def generar_txt_solicitudes_eliminar(self):
        return
    
    def __str__(self):
        return f"{self.nombre} {self.Id} {self.fecha_nacimiento} {self.ciudad_nacimiento} {self.tel} {self.email} {self.dir} {self.contrasena}\n"