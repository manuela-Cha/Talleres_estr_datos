from Practica_1.Administrador import Administrador
from Practica_1.Investigador import Investigador

class Factory_Usuario:
    _administrador_class = None
    _investigador_class = None
    
    @classmethod
    def get_administrador_class(cls):
        if cls._administrador_class is None:
            from Practica_1.Administrador import Administrador
            cls._administrador_class = Administrador
        return cls._administrador_class
    
    @classmethod
    def get_investigador_class(cls):
        if cls._investigador_class is None:
            from Practica_1.Investigador import Investigador
            cls._investigador_class = Investigador
        return cls._investigador_class
    
    @classmethod
    def crear_usuario(cls, tipo, *args):
        if tipo == "administrador":
            return cls.get_administrador_class()(*args)
        elif tipo == "investigador":
            return cls.get_investigador_class()(*args)
        else:
            raise ValueError("Tipo de usuario no válido")
"""
class carga:
    # ... resto de tu código ...
    
    def carga_empleados_existentes():
        try:
            with open("Practica_1/Empleados.txt", 'rb') as file:
                for linea in file:
                    # ... tu código de procesamiento ...
                    if rol == "investigador":
                        obj = UsuarioFactory.crear_usuario("investigador", *datos_empleado)
                    elif rol == "administrador":
                        obj = UsuarioFactory.crear_usuario("administrador", *datos_empleado)"""