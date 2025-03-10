
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
        self.solicitudes = DoubleList()

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
        print(self.equipos)
         
    def solicitar_agregar_equipo(self):
        "from Practica_1.carga_archivos import carga"
        equipo = Equipo.crear_equipo()
        with open("Practica_1/solicitudes_agregar.txt", "a") as archivo:  
            archivo.write("{} {} {} {} {} {} {} {}\n".format(self.getNombre(), self.Id, equipo.get_nombre(), equipo.get_numero_placa(), equipo.get_fecha_compra().getDia(), equipo.get_fecha_compra().getMes(), equipo.get_fecha_compra().getAño(), equipo.get_valor_compra() ))
        carga.carga_solicitudes_existentes()
    
    def solicitar_eliminar_equipo(self):
        "from Practica_1.carga_archivos import carga"
        print(self.equipos)
        numero_placa_eliminar = input("Escriba el numero de placa del equipo que desea eliminar: ")
        nodo_actual = self.equipos.first()
        while nodo_actual:
            if nodo_actual.data.get_numero_placa() == str(numero_placa_eliminar):
                with open("Practica_1/solicitudes_eliminar.txt", "a") as archivo:  
                    archivo.write("{} {} {} {} {} {} {} {}\n".format(self.getNombre(), self.Id, nodo_actual.data.get_nombre(), nodo_actual.data.get_numero_placa(), nodo_actual.data.get_fecha_compra().getDia(), nodo_actual.data.get_fecha_compra().getMes(), nodo_actual.data.get_fecha_compra().getAño(), nodo_actual.data.get_valor_compra() ))
                    bandera = True
            nodo_actual = nodo_actual.next
        if not bandera:
            print("No hay un numero de placa en su inventario de  equipos que coincida con el dado")
        carga.carga_solicitudes_existentes()
    
    def escribir_inventario_en_txt(self):
        ruta_archivo = "Practica_1/{}_inventario.txt".format(self.getNombre())
        try:
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:    
                archivo.write(str(self.equipos))
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")

    def escribir_solicitudes_en_txt(self):
        ruta_archivo = "Practica_1/{}_solicitudes.txt".format(self.getNombre())
        try:
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:    
                archivo.write(str(self.solicitudes))
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")
        
    def consultar_estado_solicitudes(self):
        print(self.solicitudes)
    
    
    def __str__(self):
        return f"{self.nombre} {self.Id} {self.fecha_nacimiento} {self.ciudad_nacimiento} {self.tel} {self.email} {self.dir} {self.equipos} {self.solicitudes} {self.contrasena}\n"
    