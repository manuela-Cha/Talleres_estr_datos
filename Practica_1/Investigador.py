
from Laboratorio_no_2.Usuario import Usuario
from Laboratorio_no_4.Lista_simple import Lista_Simple
from Practica_1.Equipo import Equipo

class Investigador(Usuario):
    def __init__(self, contrasena, nombre, cedula, fecha_nacimiento, ciudad_nacimiento, tel, email, dir):
        self.contrasena = contrasena    
        self.nombre = nombre
        self.cedula = cedula 
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.tel = tel
        self.email = email
        self.dir = dir
        self.equipos = Lista_Simple()

    def consultar_equipos(self):
        nodo_actual = self.equipos.head 
        while nodo_actual is not None:
            print(nodo_actual)
            nodo_actual = nodo_actual.next
         
    
    def solicitar_agregar_equipo(self):
        equipo = Equipo.crear_equipo()
        with open("Practica_1/solicitudes_agregar.txt", "a") as archivo:  
            archivo.write("{} {} {} {} {} {}".format(self.getNombre(), self.cedula, equipo.get_nombre(), equipo.get_numero_placa(), equipo.get_fecha_compra(), equipo.get_valor_compra() ))
            return True
    
    def solicitar_eliminar_equipo(self, numero_placa):
        return
    
    def revisar_estado_solicitudes(self):
        return 
    
    #falta probar
    def generar_txt_invetario(self):
        ruta = "{}.txt".format(self.getNombre())
        with open(ruta, "w") as archivo:  
            nodo_actual = self.equipos.head 
            while nodo_actual is not None:
                archivo.write(nodo_actual) 
                nodo_actual = nodo_actual.next
        print("Archivo creado y contenido escrito.")
        return 
    
    def generar_txt_solicitudes():
        return
    