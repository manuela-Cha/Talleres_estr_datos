from Practica_1.Gestion_usuarios import GestionUsuarios
from Practica_1.Factory_usuarios import Factory_Usuario
from Laboratorio_no_4.Lista_doble import DoubleList
from Laboratorio_no_2.Fecha import Fecha
from Practica_1.Equipo import Equipo
from Practica_1.Solicitud import Solicitud

class carga:
    lista_investigadores_y_administradores = DoubleList()
    lista_investigadores = DoubleList()
    lista_administradores = DoubleList()

    @classmethod
    def get_listas(cls):
        return {
            'todos': cls.lista_investigadores_y_administradores,
            'investigadores': cls.lista_investigadores,
            'admins': cls.lista_administradores
        }

    @classmethod
    def cargar_Password_en_lista(cls):
        return GestionUsuarios.cargar_Password_en_lista()

    @classmethod
    def validacion_datos(cls, cedula, contraseña):
        return GestionUsuarios.validacion_datos(cedula, contraseña, cls.lista_investigadores_y_administradores)

    @classmethod
    def investigador_o_admin_datos(cls, cedula):
        lista_password = cls.cargar_Password_en_lista()
        return GestionUsuarios.investigador_o_admin_datos(cedula, lista_password)

    @classmethod
    def guardar_lista_en_archivo_password(cls, lista):
        with open("Practica_1/Password.txt", 'w') as archivo:
            nodo_actual = lista.first()
            while nodo_actual:
                archivo.write(nodo_actual.data + '\n')
                nodo_actual = nodo_actual.next

    @classmethod
    def guardar_lista_en_archivo_empleados(cls, lista):
        with open("Practica_1/Empleados.txt", 'w') as archivo:
            nodo_actual = lista.first()
            while nodo_actual:
                archivo.write(nodo_actual.data + '\n')
                nodo_actual = nodo_actual.next

    @classmethod
    def eliminar_usuario_Password_datos(cls, cedula):
        return GestionUsuarios.eliminar_usuario_Password_datos(cedula, cls.get_listas())

    @classmethod
    def eliminar_usuario_de_txt(cls, cedula):
        GestionUsuarios.eliminar_usuario_de_txt(cedula)

    @classmethod
    def inicializar_empleado(cls):
        try:
            with open("Practica_1/Empleados.txt", 'rb') as file:
                file.seek(-2, 2)
                while file.read(1) != b'\n':
                    file.seek(-2, 1)
                ultima_linea = file.readline().decode('utf-8').strip().split()

            cedula = ultima_linea[1]
            datos_empleado = [
                ultima_linea[0],
                ultima_linea[1],
                ultima_linea[2:5],
                ultima_linea[5],
                ultima_linea[6],
                ultima_linea[7],
                ultima_linea[8:],
            ]

            with open("Practica_1/Password.txt", "r") as file1:
                for linea in file1:
                    datos = linea.strip().split()
                    if datos[0] == cedula:
                        rol = datos[2]
                        obj = Factory_Usuario.crear_usuario(rol, datos[1], datos_empleado)
                        if rol == "investigador":
                            cls.lista_investigadores_y_administradores.addLast(obj)
                            cls.lista_investigadores.addLast(obj)
                        else:
                            cls.lista_investigadores_y_administradores.addLast(obj)
                            cls.lista_administradores.addLast(obj)
                        return
        except FileNotFoundError as e:
            print(f"Error: {e}")

    @classmethod
    def carga_empleados_existentes(cls):
        try:
            with open("Practica_1/Empleados.txt", 'rb') as file:
                for linea in file:
                    datos = linea.decode('utf-8').strip().split()
                    cedula = datos[1]
                    nacimiento_fecha = " ".join(datos[2:5])
                    direccion = " ".join(datos[8:])
                    datos_empleado = [
                        datos[0],
                        datos[1],
                        nacimiento_fecha,
                        datos[5],
                        datos[6],
                        datos[7],
                        direccion,
                    ]

                    with open("Practica_1/Password.txt", "r") as file1:
                        for linea in file1:
                            datos_password = linea.strip().split()
                            if datos_password[0] == cedula:
                                rol = datos_password[2]
                                obj = Factory_Usuario.crear_usuario(rol, datos_password[1], datos_empleado)
                                if rol == "investigador":
                                    cls.lista_investigadores_y_administradores.addLast(obj)
                                    cls.lista_investigadores.addLast(obj)
                                elif rol == "administrador":
                                    cls.lista_investigadores_y_administradores.addLast(obj)
                                    cls.lista_administradores.addLast(obj)
                                break
                        else:
                            print(f"No se encontró cédula {cedula} en Password.txt.")
        except FileNotFoundError as e:
            print(f"Error: {e}")

    @classmethod
    def carga_equipos_existentes(cls):
        try:
            with open("Practica_1/InventarioGeneral.txt", 'r', encoding='utf-8') as file:
                for linea in file:
                    datos = linea.strip().split()
                    cedula = datos[1]
                    fecha = Fecha(datos[4], datos[5], datos[6])
                    equipo = Equipo(datos[2], datos[3], fecha, datos[7])

                    nodo_actual = cls.lista_investigadores_y_administradores.first()
                    while nodo_actual:
                        if nodo_actual.data.getId() == cedula:
                            nodo_actual.data.equipos.addLast(equipo)
                            break
                        nodo_actual = nodo_actual.next

        except FileNotFoundError as e:
            print(f"Error: {e}")

    @classmethod
    def carga_solicitudes_existentes(cls):
        def esta_archivo_vacio(ruta_archivo):
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as file:
                    return not bool(file.read().strip())
            except FileNotFoundError:
                return True

        def procesar_solicitudes(ruta_archivo, tipo_solicitud):
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as file:
                    contenido = file.read().strip()
                    if not contenido:
                        return
                    
                    file.seek(0)
                    for linea in file:
                        datos = linea.strip().split()
                        if len(datos) < 4:
                            continue
                        cedula = datos[1]
                        numero_placa = datos[3]
                        solicitud = Solicitud(tipo_solicitud, numero_placa, "pendiente")
                        
                        nodo_actual = cls.lista_investigadores_y_administradores.first()
                        while nodo_actual:
                            if nodo_actual.data.getId() == cedula:
                                nodo_actual.data.solicitudes.addLast(solicitud)
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
                        datos = linea.strip().split()
                        if len(datos) < 8:
                            continue
                        
                        cedula = datos[0]
                        numero_placa = datos[1]
                        tipo_solicitud = datos[2]
                        estado = datos[9]
                        solicitud = Solicitud(tipo_solicitud, numero_placa, estado)
                        
                        nodo_actual = cls.lista_investigadores_y_administradores.first()
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

