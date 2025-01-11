class Usuario:
    def __init__(self, nombre, Id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir):
        self.nombre = nombre
        self.Id = Id
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.tel = tel
        self.email = email
        self.dir = dir 

    def setNombre(self, nombre):
        self.nombre = nombre

    def setId(self, Id):
        self.Id = Id

    def setFecha_nacimiento(self, f):
        self.fecha_nacimiento = f

    def setCiudad_nacimiento(self, c):
        self.ciudad_nacimiento = c
    
    def setTel(self, t):
        self.tel = t

    def setEmail(self, e):
        self.email = e

    def setDir(self, d):
        self.dir = d


    def getNombre(self):
        return self.nombre

    def getId(self):
        return self.Id

    def getFecha_nacimiento(self):
        return self.fecha_nacimiento

    def getCiudad_nacimiento(self):
        return self.ciudad_nacimiento
    
    def getTel(self):
        return self.tel

    def getEmail(self):
        return self.email

    def getDir(self):
        return self.dir
    
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
        return usuario

    def __str__(self):
        return f"{self.nombre} {self.Id} {self.fecha_nacimiento} {self.ciudad_nacimiento} {self.tel} {self.email} {self.dir}\n"


