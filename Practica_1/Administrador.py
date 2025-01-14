from Practica_1.Investigador import Investigador
from Laboratorio_no_2.Usuario import Usuario

class Administrador(Investigador):
    
    def __init__(self, id, contrasena, nombre, cedula, fecha_nacimiento, ciudad_nacimiento, telefono, correo_electronico, direccion):
        self.id = id
        self.contrasena = contrasena
        self.nombre = nombre
        self.cedula = cedula 
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.direccion = direccion

    "falta, que se ingrese el rol en el archivo password, si es investigador o admin"
    def registrar_nuevo_usuario():
        try:
            with open("Practica_1/prueba.txt", "a") as file:
                usuario_agregado = Usuario.solicitar()
                file.write("{} {}\n".format(usuario_agregado.getNombre(),usuario_agregado.getCiudad_nacimiento()))
        except:
            print("no se pudo escribir en prueba")
     
    def  cambiar_contraseña():
        return
    
    def eliminar_usuario():
        return 
    
    def actualizar_empleadostxt():
        return
    
    def actualizar_passwordtxt():
        return
    
    def actualizar_control_cambios():
        return
    
    def agregar_nuevo_equipo():
        return 
    
    def revision_solicitudes_eliminacion_equipos():
        return 
    
    def revision_solicitudes_eliminacion_equipos():
        return
    
    def notificacion_respuesta_solicitud():
        return
    
    def eliminar_equipo():
        return 
    
    def agregar_equipo():
        return
    
    def generar_txt_inventario_investigador(id_investigador):
        return
    
    def generar_txt_inventario_general():
        return
    
    def generar_control_de_cambios():
        return 
    
    def generar_txt_solicitudes_agregar():
        return
    
    def generar_txt_solicitudes_eliminar():
        return