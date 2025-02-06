class Usuario:
    def __init__(self, nombre, id, tel, email, direc, fecha_nacimiento=None, ciudad_nacimiento=None):
        self.__nombre = nombre
        self.__id = id
        self.__fecha_nacimiento = fecha_nacimiento
        self.__ciudad_nacimiento = ciudad_nacimiento
        self.__tel = tel
        self.__email = email
        self.__dir = direc

    def get_nombre(self):
        return self.__nombre
    def get_id(self):
        return self.__id
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    def get_ciudad_nacimiento(self):
        return self.__ciudad_nacimiento
    def get_tel(self):
        return self.__tel
    def get_email(self):
        return self.__email
    def get_dir(self):
        return self.__dir
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_id(self, id):
        self.__id = id
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento
    def set_ciudad_nacimiento(self, ciudad_nacimiento):
        self.__ciudad_nacimiento = ciudad_nacimiento
    def set_tel(self, tel):
        self.__tel = tel
    def set_email(self, email):
        self.__email = email
    def set_dir(self, direc):
        self.__dir = direc

    def __str__(self):
            fecha_str = str(self.__fecha_nacimiento) if self.__fecha_nacimiento else "N/A"
            dir_str = str(self.__dir) if self.__dir else "N/A"
            return (f"{self.__nombre} {self.__id} {fecha_str} {self.__ciudad_nacimiento} {self.__tel} "
                    f"{self.__email} {dir_str}")