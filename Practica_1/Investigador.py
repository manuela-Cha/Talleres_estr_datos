
from Laboratorio_no_2.Usuario import Usuario

class Investigador(Usuario):
    def __init__(self, Id, contrasena, nombre, cedula, fecha_nacimiento, ciudad_nacimiento, tel, email, dir):
        self.Id = Id
        self.contrasena = contrasena    
        self.nombre = nombre
        self.cedula = cedula 
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.tel = tel
        self.email = email
        self.dir = dir

    def consultar_equipos():
        return
    
    def solicitar_agregar_equipo():
        return
    
    def solicitar_eliminar_equipo(numero_placa):
        return
    
    def revisar_estado_solicitudes():
        return 
    
    def generar_txt_invetario():
        return 
    
    def generar_txt_solicitudes():
        return
    