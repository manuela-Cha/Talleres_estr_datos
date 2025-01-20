import re as re
from Laboratorio_no_4.Lista_doble import DoubleList
from Laboratorio_no_2.Usuario import Usuario
from Practica_1.Administrador import Administrador
from Practica_1.Investigador import Investigador
from Laboratorio_no_2.Fecha import Fecha

class carga:
    lista_investigadores_y_administradores = DoubleList()
    lista_investigadores = DoubleList()
    lista_administradores = DoubleList()
    dic_Equipos = {}

    
    """Investigadores y admin ya existentes:"""
    """obj1 = Investigador("j4an1980$", "Juan-Perez", "24567898", "12 10 1980", "Medellin", "3003233234", "juanperez@edl.edu.co", "kr74 4T-35 Boston Medellin null null")
    obj2 = Investigador("d13go1979", "Diego-Palacio", "34568910", "20 12 1979", "Envigado", "3013234567", "diegopalacio@edl.edu.co", "Robledo Medellin Balcones-de-la-Quinta 405")
    obj3 = Administrador("c4100l485Cal$", "Camila-Jimenez", "2345902", "15 09 1985", "Cali", "3003234567", "camilajimenez@edl.edu.co",  " tr45 4S-73 Poblado Medellin null null")
    obj4 = Investigador("p3dr41990.$", "Pedro-Gomez", "1075689", "20 02 1990", "Popayan", "3003012323", "pedrogomez@edl.edu.co", "kr23 8-10 SanJuan Envigado Mirador 503")
    obj5 = Investigador("r482novMed.", "Tatiana-Ramirez", "2345934", "15 11 1982", "Medellin", "3004567890", "tatianaramirez@edl.edu.co", "cll5 4S-69 Poblado Medellin UrbColina 1023")
    
    lista_investigadores_y_administradores.addLast(obj1)
    lista_investigadores_y_administradores.addLast(obj2)
    lista_investigadores_y_administradores.addLast(obj3)
    lista_investigadores_y_administradores.addLast(obj4)
    lista_investigadores_y_administradores.addLast(obj5)

    lista_investigadores.addLast(obj1)
    lista_investigadores.addLast(obj2)
    lista_investigadores.addLast(obj4)
    lista_investigadores.addLast(obj5)

    lista_administradores.addLast(obj3)"""

    """def cargar_Empleados_en_lista(cedula=None):
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

        return empleados_lista_doble"""


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
        """Elimina el usuario dado de las listas de empleados."""
        nodo_actual = carga.lista_investigadores_y_administradores.first()
        
        if nodo_actual is None:
            print("La lista está vacía, no hay nada que eliminar.")
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
            if isinstance(datos, Administrador):
                admin_node = carga.lista_administradores.encontrar_nodo(datos)
                if admin_node:
                    carga.lista_administradores.remove(admin_node)
            elif isinstance(datos, Investigador):
                invest_node = carga.lista_investigadores.encontrar_nodo(datos)
                if invest_node:
                    carga.lista_investigadores.remove(invest_node)
            
            carga.lista_investigadores_y_administradores.remove(nodo_a_eliminar)
            
            return True
        print(f"No se encontró un usuario con la cédula {cedula}.")
        return False
        
    def eliminar_usuario_de_txt(cedula):
        """Elimina la línea correspondiente a la cédula del archivo Empleados.txt."""
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
            print("Error: El archivo Practica_1/Empleados.txt no existe.")
        except IndexError:
            print("Error: Formato inesperado en el archivo.")
        except Exception as e:
            print(f"Error inesperado: {e}")

                        

    """def eliminar_usuario_Empleados_datos(cedula):
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
        return False"""

    """def obtener_administradores(cedula_buscar=None):
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

        return administradores"""

    """def obtener_investigadores(cedula_buscar=None):
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

        return investigadores"""
    
    """@staticmethod
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
                    nodo_actual = nodo_actual.next"""
    
    """def cuadrar_contraseñas_lista_investigadores():
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
                    nodo_actual = nodo_actual.next"""

    def inicializar_empleado():
        from Practica_1.Administrador import Administrador
        from Practica_1.Investigador import Investigador
        """Inicializa el nuevo empleado y lo agrega a la lista correspondiente."""
        try:
            # Lee la última línea del archivo Empleados.txt
            with open("Practica_1/Empleados.txt", 'rb') as file:
                file.seek(-2, 2)
                while file.read(1) != b'\n': 
                    file.seek(-2, 1)
                ultima_linea = file.readline().decode('utf-8').strip().split()

            cedula = ultima_linea[1]
            datos_empleado = [
                ultima_linea[0],         # Nombre
                ultima_linea[1],         # Cédula
                ultima_linea[2:5],       # Fecha de nacimiento
                ultima_linea[5],         # Ciudad de nacimiento
                ultima_linea[6],         # Telefono
                ultima_linea[7],         # Email
                ultima_linea[8:],        # Direccion
            ]

            with open("Practica_1/Password.txt", "r") as file1:
                for linea in file1:
                    datos = linea.strip().split()
                    if datos[0] == cedula:
                        rol = datos[2]

                        if rol == "investigador":
                            obj = Investigador(datos[1], *datos_empleado)
                            carga.lista_investigadores_y_administradores.addLast(obj)
                            carga.lista_investigadores.addLast(obj)
                        elif rol == "administrador":
                            obj = Administrador(datos[1], *datos_empleado)
                            carga.lista_investigadores_y_administradores.addLast(obj)
                            carga.lista_administradores.addLast(obj)
                        else:
                            print("Rol del empleado no identificado")
                        return
                print("desde inicializar empleado cedula en empleados: ", cedula) 
                print("desde inicializar empleado cedula en password: ", datos[0]) 
                print("Ninguna cédula coincide en los dos archivos.")
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def carga_empleados_existentes():
        from Practica_1.Administrador import Administrador
        from Practica_1.Investigador import Investigador
        """Inicializa los empleados y los agrega a las listas correspondientes."""
        try:
            with open("Practica_1/Empleados.txt", 'rb') as file:
                for linea in file:
                    datos = linea.decode('utf-8').strip().split()
                    cedula = datos[1]
                    nacimiento_fecha = " ".join(datos[2:5])
                    direccion = " ".join(datos[8:])
                    datos_empleado = [
                        datos[0],  # Nombre
                        datos[1],  # Cédula
                        nacimiento_fecha,  # Fecha de nacimiento
                        datos[5],  # Ciudad de nacimiento
                        datos[6],  # Teléfono
                        datos[7],  # Email
                        direccion,  # Dirección
                    ]

                    # Procesar el archivo Password.txt para encontrar el rol
                    with open("Practica_1/Password.txt", "r") as file1:
                        for linea in file1:
                            datos_password = linea.strip().split()
                            if datos_password[0] == cedula:
                                rol = datos_password[2]
                                if rol == "investigador":
                                    obj = Investigador(datos_password[1], *datos_empleado)
                                    carga.lista_investigadores_y_administradores.addLast(obj)
                                    carga.lista_investigadores.addLast(obj)
                                elif rol == "administrador":
                                    obj = Administrador(datos_password[1], *datos_empleado)
                                    carga.lista_investigadores_y_administradores.addLast(obj)
                                    carga.lista_administradores.addLast(obj)
                                else:
                                    print(f"Rol del empleado con cédula {cedula} no identificado.")
                                break  # Salir del bucle de Password.txt una vez encontrado el rol
                        else:
                            print(f"No se encontró cédula {cedula} en Password.txt.")
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def carga_equipos_existentes():
        """carga los equipos y los agrega a quien sea debido"""
        from Practica_1.Equipo import Equipo
        try:
            with open("Practica_1/InventarioGeneral.txt", 'r', encoding='utf-8') as file:
                for linea in file:
                    datos = linea.strip().split()
                    cedula = datos[1]
                    fecha = Fecha(datos[4],datos[5], datos[6])
                    equipo = Equipo(datos[2], datos[3], fecha, datos[7])
        

                    encontrado = False
                    nodo_actual = carga.lista_investigadores_y_administradores.first()

                    while nodo_actual and not encontrado:
                        usuario = nodo_actual.data
                        if usuario.getId() == cedula:
                            usuario.equipos.addLast(equipo)
                            encontrado = True 
                        nodo_actual = nodo_actual.next

                    """nodo_actual = carga.lista_investigadores.first()
                    while nodo_actual:
                        datos = nodo_actual.data
                        if datos.getId() == str(cedula):
                            nodo_actual.data.equipos.addLast(equipo)
                            break
                        nodo_actual = nodo_actual.next"""

                    """nodo_actual = carga.lista_administradores.first()
                    while nodo_actual:
                        datos = nodo_actual.data
                        if datos.getId() == str(cedula):
                            nodo_actual.data.equipos.addLast(equipo)
                            break
                        nodo_actual = nodo_actual.next"""

        except FileNotFoundError as e:
                    print(f"Error: {e}")


        