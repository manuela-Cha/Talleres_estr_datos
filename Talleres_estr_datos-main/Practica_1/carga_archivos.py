import re as re
from Laboratorio_no_4.Lista_doble import DoubleList
from Laboratorio_no_2.Usuario import Usuario

class carga:
    lista_investigadores_y_administradores = DoubleList()
    lista_investigadores = DoubleList()
    lista_administradores = DoubleList()

    def cargar_Empleados_en_lista(cedula=None):
        ruta_archivo = "Practica_1/Empleados.txt"
        empleados_lista_doble = DoubleList()

        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(" ")

                    if len(datos) < 8:
                        continue

                    nombre = datos[0]
                    cedula_actual = datos[1]
                    fecha_nacimiento = datos[2:5]
                    ciudad_nacimiento = datos[5]
                    tel = datos[6]
                    email = datos[7]
                    dir = datos[8:]

                    usuario = Usuario(nombre, cedula_actual, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)

                    if cedula is None or str(cedula_actual) == str(cedula):
                        empleados_lista_doble.addLast(usuario)

        except FileNotFoundError:
            print(f"El archivo en la ruta {ruta_archivo} no fue encontrado.")
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")

        return empleados_lista_doble


    def cargar_Password_en_lista():
        lista = DoubleList()
        try:
            with open("Practica_1/Password.txt", "r") as file:
                for line in file:
                    lista.addLast(line.strip())
        except FileNotFoundError:
            print(f"Archivo no encontrado")
        return lista
    
    def validacion_datos(cedula, contraseña):
        nodo_actual = carga.lista_investigadores_y_administradores.first()
        while nodo_actual:
            if nodo_actual.data.Id == str(cedula) and nodo_actual.data.contrasena == str(contraseña):
                return True 
            nodo_actual = nodo_actual.next
        
        return False 


                
    def investigador_o_admin_datos(cedula):
        lista_password = carga.cargar_Password_en_lista()
        nodo_actual = lista_password.first()
        while nodo_actual:
            datos = nodo_actual.data.split(" ")
            if datos[0] == cedula:
                return datos[2]
            nodo_actual = nodo_actual.next
        return False

    def guardar_lista_en_archivo_password(lista):
        with open("Practica_1/Password.txt", 'w') as archivo:
            nodo_actual = lista.first()
            while nodo_actual:
                archivo.write(nodo_actual.data + '\n')
                nodo_actual = nodo_actual.next

    def guardar_lista_en_archivo_empleados(lista):
        with open("Practica_1/Empleados.txt", 'w') as archivo:
            nodo_actual = lista.first()
            while nodo_actual:
                archivo.write(nodo_actual.data + '\n')
                nodo_actual = nodo_actual.next

    def eliminar_usuario_Password_datos(cedula):
        lista_password = carga.cargar_Password_en_lista()
        nodo_actual = lista_password.first()
        while nodo_actual:
            datos = nodo_actual.data.split(" ")
            if datos[0] == cedula:
                lista_password.remove(nodo_actual)
                carga.guardar_lista_en_archivo_password(lista_password)
                return True
            nodo_actual = nodo_actual.next
        return False  

    def eliminar_usuario_Empleados_datos(cedula):
        lista = DoubleList()
        try:
            with open("Practica_1/Empleados.txt", "r") as file:
                for line in file:
                    lista.addLast(line.strip())
        except FileNotFoundError:
            print(f"Archivo no encontrado")

        nodo_actual = lista.first()
        while nodo_actual:
            datos = nodo_actual.data.split(" ")
            if datos[1] == cedula:
                lista.remove(nodo_actual)
                carga.guardar_lista_en_archivo_empleados(lista)
                return True
            nodo_actual = nodo_actual.next
        return False

    def obtener_administradores(cedula_buscar=None):
        from Practica_1.Administrador import Administrador
        administradores = DoubleList()

        try:
            ruta_password = "Practica_1/Password.txt"
            roles = {}
            with open(ruta_password, "r", encoding="utf-8") as archivo_password:
                for linea in archivo_password:
                    datos = linea.strip().split(" ")
                    if len(datos) < 3:
                        continue
                    cedula = datos[0]
                    rol = datos[2].lower()
                    roles[cedula] = rol
                    contrasena = datos[1]

            ruta_empleados = "Practica_1/Empleados.txt"
            with open(ruta_empleados, "r", encoding="utf-8") as archivo_empleados:
                for linea in archivo_empleados:
                    datos = linea.strip().split(" ")
                    if len(datos) < 8:
                        continue
                    nombre = datos[0]
                    cedula = datos[1]
                    fecha_nacimiento = datos[2:5]
                    ciudad_nacimiento = datos[5]
                    tel = datos[6]
                    email = datos[7]
                    direccion = " ".join(datos[8:])

                    if cedula in roles and roles[cedula] == "administrador":
                        "contrasena = '...'"
                        administrador = Administrador(
                            contrasena, nombre, cedula, fecha_nacimiento,
                            ciudad_nacimiento, tel, email, direccion
                        )
                        administradores.addLast(administrador)
                        carga.lista_investigadores_y_administradores.addLast(administrador)
                        carga.lista_administradores.addLast(administrador)  # Agregar a la lista combinada

            if cedula_buscar:
                resultado = DoubleList()
                nodo_actual = administradores.first()
                while nodo_actual:
                    if nodo_actual.data.Id == str(cedula_buscar):
                        resultado.addLast(nodo_actual.data)
                        break
                    nodo_actual = nodo_actual.next
                return resultado

        except Exception as e:
            print(f"Error al procesar los archivos: {e}")

        return administradores

    def obtener_investigadores(cedula_buscar=None):
        from Practica_1.Investigador import Investigador
        investigadores = DoubleList()

        try:
            ruta_password = "Practica_1/Password.txt"
            roles = {}
            with open(ruta_password, "r", encoding="utf-8") as archivo_password:
                for linea in archivo_password:
                    datos = linea.strip().split(" ")
                    if len(datos) < 3:
                        continue
                    cedula = datos[0]
                    rol = datos[2].lower()
                    roles[cedula] = rol
                    
            ruta_empleados = "Practica_1/Empleados.txt"
            with open(ruta_empleados, "r", encoding="utf-8") as archivo_empleados:
                for linea in archivo_empleados:
                    datos = linea.strip().split(" ")
                    if len(datos) < 8:
                        continue
                    nombre = datos[0]
                    cedula = datos[1]
                    fecha_nacimiento = datos[2:5]
                    ciudad_nacimiento = datos[5]
                    tel = datos[6]
                    email = datos[7]
                    direccion = " ".join(datos[8:])
                    contrasena = "..."

                    if cedula in roles and roles[cedula] == "investigador":
                        investigador = Investigador(
                            contrasena, nombre, cedula, fecha_nacimiento,
                            ciudad_nacimiento, tel, email, direccion
                        )
                        investigadores.addLast(investigador)
                        carga.lista_investigadores_y_administradores.addLast(investigador)
                        carga.lista_investigadores.addLast(investigador)  
            
            if cedula_buscar:
                resultado = DoubleList()
                nodo_actual = investigadores.first()
                while nodo_actual:
                    if nodo_actual.data.Id == str(cedula_buscar):
                        resultado.addLast(nodo_actual.data)
                        break
                    nodo_actual = nodo_actual.next
                return resultado

        except Exception as e:
            print(f"Error al procesar los archivos: {e}")

        return investigadores
    
    @staticmethod
    def cuadrar_contraseñas_lista_completa():
        ruta_password = "Practica_1/Password.txt"
        with open(ruta_password, "r", encoding="utf-8") as archivo_password:
            for linea in archivo_password:
                datos = linea.strip().split(" ")
                if len(datos) < 3:
                    continue
                nodo_actual = carga.lista_investigadores_y_administradores.first()
                while nodo_actual:
                    if nodo_actual.data.Id == datos[0]:
                        nodo_actual.data.contrasena = datos[1]
                        break
                    nodo_actual = nodo_actual.next
    
    def cuadrar_contraseñas_lista_investigadores():
        ruta_password = "Practica_1/Password.txt"
        with open(ruta_password, "r", encoding="utf-8") as archivo_password:
            for linea in archivo_password:
                datos = linea.strip().split(" ")
                if len(datos) < 3:
                    continue
                nodo_actual = carga.lista_investigadores.first()
                while nodo_actual:
                    if nodo_actual.data.Id == datos[0]:
                        nodo_actual.data.contrasena = datos[1]
                        break 
                    nodo_actual = nodo_actual.next

    def cuadrar_contrseñas_lista_admins():
        ruta_password = "Practica_1/Password.txt"
        with open(ruta_password, "r", encoding="utf-8") as archivo_password:
            for linea in archivo_password:
                datos = linea.strip().split(" ")
                if len(datos) < 3:
                    continue
                nodo_actual = carga.lista_administradores.first()
                while nodo_actual:
                    if nodo_actual.data.Id == datos[0]:
                        nodo_actual.data.contrasena = datos[1]
                        break 
                    nodo_actual = nodo_actual.next



