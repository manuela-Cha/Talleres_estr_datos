from Practica_1.carga_archivos import carga

class intfz_grafica:
        
    def validacion():
        print("Bienvenido al inventario, digite su cédula y contraseña\n")
        usuario = input("cédula: ")
        contraseña = input("Contraseña: ")
        
        while 1:
            if carga.carga_Password(usuario, contraseña):
                print("Bienvenido\n")
                break
            else:
                print("Usuario y/o contraseña inválidos")


        