from Practica_1.carga_archivos import carga
from Practica_1.Administrador import Administrador

class intfz_grafica:
        
    def validacion():
        print("Bienvenido al inventario, digite su cédula y contraseña\n")
        while True:
            usuario = input("Cédula: ")
            contraseña = input("Contraseña: ")
        
            try:
        
                if carga.validacion_datos(usuario, contraseña):
                    print("Bienvenido\n")
                    return usuario
                else:
                    print("Usuario y/o contraseña inválidos")

            except FileNotFoundError:
                print("Error: El archivo de contraseñas no existe.")
                break

    def investigador_o_admin ():
        
        if carga.investigador_o_admin_datos(intfz_grafica.validacion()) == "investigador":
            print("resultado de la funcion:", )
            print("Bienvenido investigador\nSeleccione la acción que desee realizar:1) consultar inventario\n2)solicitar agregar un nuevo equipo")
        else:
            print("Bienvenido administrador\nSeleccione la acción que desee realizar:1) consultar inventario\n2)solicitar agregar un nuevo equipo")
            agregar = input("agregar usuario: ")
            if agregar == "si":
                Administrador.registrar_nuevo_usuario()
            
            


        