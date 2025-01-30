class Factory_Usuario:
    @classmethod
    def crear_usuario(cls, tipo, contrasena, lista):
        if tipo == "administrador":
            from Practica_1.Administrador import Administrador
            return Administrador(contrasena, lista[0], lista[1], lista[2], 
                               lista[3], lista[4], lista[5], lista[6])
        elif tipo == "investigador":
            from Practica_1.Investigador import Investigador
            return Investigador(contrasena, lista[0], lista[1], lista[2], 
                              lista[3], lista[4], lista[5], lista[6])
        else:
            raise ValueError("Tipo de usuario no válido")
    
    @classmethod
    def es_instancia(cls, datos):
        from Practica_1.Administrador import Administrador
        from Practica_1.Investigador import Investigador
        
        if isinstance(datos, Administrador):
            return "administrador"
        elif isinstance(datos, Investigador):
            return "investigador"
        return "Error, el dato no pertenece a ningun usuario"