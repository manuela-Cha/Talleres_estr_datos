import re as re
class carga:

    def validacion_datos(cedula, contraseña):
        ruta = 'Practica_1/Password.txt'
        with open(ruta, 'r') as file:
            for line in file:
                lista = line.strip().split(" ")
                if lista[0] == cedula and lista[1] == contraseña:
                    return True
        return False
                
            
    def investigador_o_admin_datos(cedula):
        file= open('Practica_1/Password.txt','r')
        for line in file:
            lista = line.lower().split(" ")
            if lista[0] == cedula:
                file.close()
                return lista[2]
