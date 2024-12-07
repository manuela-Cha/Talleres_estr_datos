class Usuario:
    def __init__(self, nombre, Id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir):
        self.__nombre = nombre
        self.__Id = Id
        self.__fecha_nacimiento = fecha_nacimiento
        self.__ciudad_nacimiento = ciudad_nacimiento
        self.__tel = tel
        self.__email = email
        self.__dir = dir 

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setId(self, Id):
        self.__Id = Id

    def setFecha_nacimiento(self, f):
        self.__fecha_nacimiento = f

    def setCiudad_nacimiento(self, c):
        self.__ciudad_nacimiento = c
    
    def setTel(self, t):
        self.__tel = t

    def setEmail(self, e):
        self.__email = e

    def setDir(self, d):
        self.__dir = d


    def getNombre(self):
        return self.__nombre

    def getId(self):
        return self.__Id

    def getFecha_nacimiento(self):
        return self.__fecha_nacimiento

    def getCiudad_nacimiento(self):
        return self.__ciudad_nacimiento
    
    def getTel(self):
        return self.__tel

    def getEmail(self):
        return self.__email

    def getDir(self):
        return self.__dir
    
    @staticmethod
    def solicitar():
        print("Ingrese sus datos: ")
        
        nombre = input("Nombre: ")
        id_usuario = input("ID: ")
        fecha_nacimiento = input("Fecha de nacimiento: ")
        ciudad_de_nacimiento = input("Ciudad donde nació: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        direccion = input("Dirección: ")
        
        usuario = Usuario(nombre, id_usuario, fecha_nacimiento, ciudad_de_nacimiento, telefono, email, direccion)
        print(usuario)

    def __str__(self):
        return f"\nNombre={self.__nombre}\nId={self.__Id}\nFecha_nacimiento={self.__fecha_nacimiento}\nCiudad_de_nacimiento={self.__ciudad_nacimiento}\nTelefono={self.__tel}\nEmail={self.__email}\nDireccion={self.__dir}"


