from Laboratorio_no_2 import Usuario

class Agenda:
    def __init__(self, capacity):
        self.registro = [None] * capacity  
        self.no_reg = 0  

    def agregar(self, u):
        if self.buscar(u.getId()) != -1:  
            return False
        if self.no_reg < len(self.registro):  
            self.registro[self.no_reg] = u
            self.no_reg += 1
            return True
        return False

    def buscar(self, id):
        for i in range(self.no_reg): 
            if self.registro[i] is not None and self.registro[i].getId() == id:
                return i
        return -1

    def eliminar(self, id):
        pos = self.buscar(id)  
        if pos == -1: 
            return False
        
        for i in range(pos, self.no_reg - 1):
            self.registro[i] = self.registro[i + 1]
        self.registro[self.no_reg - 1] = None  
        self.no_reg -= 1
        return True

    def toFile(self):
        with open("agenda.txt", "w") as file:
            for i in range(self.no_reg):
                if self.registro[i] is not None:
                    usuario = self.registro[i]
                    file.write(f"{usuario.getNombre()}, {usuario.getId()}, {usuario.getFecha_nacimiento()}, {usuario.getCiudad_nacimiento()}, "
                            f"{usuario.getTel()}, {usuario.getEmail()}, {usuario.getDir()}\n")


    def importFile(self):
        try:
            with open("agenda.txt", "r") as file:
                for line in file:
                    atributos = line.strip().split(", ")
                    if len(atributos) == 7: 
                        nombre, id, fecha_nacimiento, ciudad_nacimiento, tel, email, dir = atributos
                        u = Usuario(nombre, int(id), fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
                        self.agregar(u)
        except FileNotFoundError:
            print("El archivo agenda.txt no existe.")



obj = Agenda(12)
