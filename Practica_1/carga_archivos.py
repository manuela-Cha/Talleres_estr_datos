import re as re
from Laboratorio_no_4.Lista_doble import DoubleList
from Practica_1.Administrador import Administrador
from Practica_1.Investigador import Investigador
from Laboratorio_no_2.Fecha import Fecha
from Practica_1.Solicitud import Solicitud
class carga:
    lista_investigadores_y_administradores = DoubleList()
    lista_investigadores = DoubleList()
    lista_administradores = DoubleList()

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

                        

    def inicializar_empleado():
        from Practica_1.Administrador import Administrador
        from Practica_1.Investigador import Investigador
        """Inicializa el nuevo empleado y lo agrega a la lista correspondiente."""
        try:
           
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

        except FileNotFoundError as e:
                    print(f"Error: {e}")
    
    def carga_solicitudes_existentes():
        """
        Carga las solicitudes existentes siguiendo un orden específico:
        1. Revisa solicitudes_agregar.txt
        2. Si está vacío, revisa solicitudes_eliminar.txt
        3. Si está vacío, revisa Control_de_cambios.txt

        """
        def esta_archivo_vacio(ruta_archivo):
            
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as file:
                    contenido = file.read().strip()
                    return not bool(contenido)
            except FileNotFoundError:
                print(f"El archivo {ruta_archivo} no existe.")
                return True

        def procesar_solicitudes(ruta_archivo, tipo_solicitud):
            
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as file:
                    contenido = file.read().strip()
                    if not contenido:  
                        return
                    
                    file.seek(0)  
                    for linea in file:
                        linea = linea.strip()
                        if not linea:  
                            continue        
                        datos = linea.split()
                        if len(datos) < 4:  
                            continue
                        cedula = datos[1]
                        numero_placa = datos[3]
                        solicitud = Solicitud(tipo_solicitud, numero_placa, "pendiente")
                        
                        nodo_actual = carga.lista_investigadores_y_administradores.first()
                        while nodo_actual:
                            usuario = nodo_actual.data
                            if usuario.getId() == cedula:
                                usuario.solicitudes.addLast(solicitud)
                                break
                            nodo_actual = nodo_actual.next
            except FileNotFoundError:
                print(f"El archivo {ruta_archivo} no existe.")

        def procesar_control_cambios():
            try:
                with open("Practica_1/Control_de_cambios.txt", 'r', encoding='utf-8') as file:
                    contenido = file.read().strip()
                    if not contenido: 
                        return
                        
                    file.seek(0)  
                    for linea in file:
                        linea = linea.strip()
                        if not linea: 
                            continue
                            
                        datos = linea.split()
                        if len(datos) < 8:  
                            continue
                            
                        cedula = datos[0]
                        numero_placa = datos[1]
                        tipo_solicitud = datos[2]
                        estado = datos[9]
                        solicitud = Solicitud(tipo_solicitud, numero_placa, estado)
                        
                        
                        nodo_actual = carga.lista_investigadores_y_administradores.first()
                        while nodo_actual:
                            usuario = nodo_actual.data
                            if usuario.getId() == cedula:
                                usuario.solicitudes.addLast(solicitud)
                                break
                            nodo_actual = nodo_actual.next
            except FileNotFoundError:
                print("El archivo Control_de_cambios.txt no existe.")

        if not esta_archivo_vacio("Practica_1/solicitudes_agregar.txt"):
            procesar_solicitudes("Practica_1/solicitudes_agregar.txt", "agregar")
        
        else:
            if not esta_archivo_vacio("Practica_1/solicitudes_eliminar.txt"):
                procesar_solicitudes("Practica_1/solicitudes_eliminar.txt", "eliminar")
            
            else:
                if not esta_archivo_vacio("Practica_1/Control_de_cambios.txt"):
                    procesar_control_cambios()
                
    def merge_sort_double_list_equipos(double_list):
        """
        Ordena una DoubleList de objetos Equipo utilizando Merge Sort,
        basado en el atributo numero_placa de cada objeto.
        """

        def split_list(head):
            """Divide la lista en dos mitades y retorna los nodos iniciales de cada mitad."""
            slow = head
            fast = head

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            middle = slow
            second_half = middle.next
            middle.next = None  # Divide la lista en dos partes
            if second_half:
                second_half.prev = None  # Rompe el enlace anterior

            return head, second_half

        def merge_sorted_lists(first, second):
            """Fusiona dos sublistas ordenadas y retorna la cabeza de la nueva lista."""
            if not first:
                return second
            if not second:
                return first

            if first.data.get_numero_placa() <= second.data.get_numero_placa():
                merged_head = first
                merged_head.next = merge_sorted_lists(first.next, second)
                if merged_head.next:  # Establece el puntero `prev` del siguiente nodo
                    merged_head.next.prev = merged_head
            else:
                merged_head = second
                merged_head.next = merge_sorted_lists(first, second.next)
                if merged_head.next:  # Establece el puntero `prev` del siguiente nodo
                    merged_head.next.prev = merged_head

            return merged_head

        def merge_sort(head):
            """Aplica Merge Sort a partir de un nodo cabeza y retorna la cabeza de la lista ordenada."""
            if not head or not head.next:
                return head

            first_half, second_half = split_list(head)
            sorted_first = merge_sort(first_half)
            sorted_second = merge_sort(second_half)

            return merge_sorted_lists(sorted_first, sorted_second)

        if double_list.isEmpty() or double_list.size == 1:
            return

        double_list.head = merge_sort(double_list.head)

        current = double_list.head
        while current.next:
            current = current.next
        double_list.tail = current


    def ordenar_equipos_usuarios(lista_usuarios):
        """
        Ordena los equipos de cada usuario en una lista de usuarios de tipo DoubleList.
        """
        current_usuario = lista_usuarios.first()  # Obtén el primer nodo de la lista de usuarios
        while current_usuario:
            # Obtén la lista de equipos del usuario actual
            equipos = current_usuario.data.getEquipos()
            # Ordena la lista de equipos utilizando Merge Sort
            carga.merge_sort_double_list_equipos(equipos)
            current_usuario = current_usuario.next  # Pasa al siguiente usuario

