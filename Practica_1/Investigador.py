
from Laboratorio_no_2.Usuario import Usuario
from Laboratorio_no_4.Lista_doble import DoubleList
from Practica_1.Equipo import Equipo
from Practica_1.carga_archivos import carga 

class Investigador(Usuario):
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
        self.solicitudes = {}

    def getEquipos(self):
        return self.equipos
    
    def eliminar_equipo(self, numero_placa_eliminar):
        nodo_actual = self.equipos.first() 
        while nodo_actual is not None:
            if nodo_actual.get_numero_placa() == numero_placa_eliminar:
                nodo_actual.numero_placa = None
            nodo_actual = nodo_actual.next
        if nodo_actual == None:
            pass
    
    def getSolicitudes(self):
        return self.solicitudes

    def consultar_equipos(self):
        print("Equipos: ")
        nodo_actual = self.equipos.first() 
        while nodo_actual is not None:
            print(nodo_actual.data)
            nodo_actual = nodo_actual.next
         
    def solicitar_agregar_equipo(self):
        equipo = Equipo.crear_equipo()
        with open("Practica_1/solicitudes_agregar.txt", "a") as archivo:  
            archivo.write("{} {} {} {} {} {} {} {}\n".format(self.getNombre(), self.Id, equipo.get_nombre(), equipo.get_numero_placa(), equipo.get_fecha_compra().getDia(), equipo.get_fecha_compra().getMes(), equipo.get_fecha_compra().getAño(), equipo.get_valor_compra() ))
            self.solicitudes["agregar_equipo: {}".format(equipo.get_nombre())] = "Pendiente"
            return True
    
    def solicitar_eliminar_equipo(self):
        numero_placa_eliminar = input("Escriba el numero de placa del equipo que desea eliminar")
        nodo_actual = self.equipos.first()
        encontrado = False  # Bandera para verificar si se encontró el objeto

        while nodo_actual is not None:
            if nodo_actual.get_numero_placa() == numero_placa_eliminar:
                encontrado = True  # Marca como encontrado
                break  # Sale del bucle si encuentra el objeto
            nodo_actual = nodo_actual.next

        # Si al final del recorrido no se encontró el objeto
        if not encontrado:
            return "Equipo con número de placa no encontrado."

        current_node = self.equipos.first()  
        while current_node is not None:
            if current_node.data.get_numero_placa() == numero_placa_eliminar:
                with open("Practica_1/solicitudes_eliminar.txt", "a") as archivo:  
                    archivo.write("{} {} {} {} {} {} {} {}".format(self.getNombre(), self.Id, current_node.data.get_nombre(), current_node.data.get_numero_placa(), current_node.data.get_fecha_compra().getDia(), current_node.data.get_fecha_compra().getMes(), current_node.data.get_fecha_compra().getAño(), current_node.data.get_valor_compra() ))
                    return True
            current_node = current_node.next
    
    def escribir_inventario_en_txt(self):
        ruta_archivo = "{}.txt".format(self.getNombre())
        try:
            objetos_unicos = set()
            nodo_actual = self.equipos.first()
            while nodo_actual:
                objetos_unicos.add(str(nodo_actual.data))  # Convertimos el dato del nodo a string
                nodo_actual = nodo_actual.next

            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                for obj in objetos_unicos:
                    archivo.write(obj + "\n")

            print(f"Se escribieron {len(objetos_unicos)} objetos únicos en {ruta_archivo}")
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")

    def escribir_solicitudes_en_txt(self):
        ruta_archivo = "{}.txt".format(self.getNombre())
        try:
            objetos_unicos = set()
            nodo_actual = self.solicitudes.first()
            while nodo_actual:
                objetos_unicos.add(str(nodo_actual.data))  # Convertimos el dato del nodo a string
                nodo_actual = nodo_actual.next

            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                for obj in objetos_unicos:
                    archivo.write(obj + "\n")

            print(f"Se escribieron {len(objetos_unicos)} objetos únicos en {ruta_archivo}")
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")
    
    
    def generar_txt_solicitudes():
        return
    
    def __str__(self):
        return f"{self.nombre} {self.Id} {self.fecha_nacimiento} {self.ciudad_nacimiento} {self.tel} {self.email} {self.dir} {self.equipos} {self.solicitudes}\n"
    