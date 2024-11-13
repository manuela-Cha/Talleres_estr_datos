from Fecha import Fecha
from Direccion import Direccion
from Usuario import Usuario

direccion = Direccion("30", "58-15", "paris","Medellin", "mónaco", "302")
print(direccion,"\n")

fecha = Fecha(27,7,2003)
print(fecha,"\n")

usuario = Usuario("Manuela","12345","27/7/2003", "Medellin", "123456", "manucha@gmail.com", "cll 27#5815")
print(usuario,"\n")


Usuario.solicitar()