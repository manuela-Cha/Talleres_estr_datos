import re as re
class carga:

    def carga_Password(cedula, contraseña):
        file= open('Password.txt','r')
        for line in file:
            lista = line.lower().split(" ")
            if lista[0] == cedula and lista[1]== contraseña:
                file.close()
                return True
            else:
                file.close() 
                return False
