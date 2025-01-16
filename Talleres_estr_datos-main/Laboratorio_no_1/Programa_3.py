class ingreso:

    usuarios = {"Juan1223": "J12an*.",
                "Maria2345": "M23a*.",
                "Pablo1459": "P14o*.",
                "Ana3456": "A34a*."}
    
    @staticmethod
    def validacion(usuarios):
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")

        bandera = False
        for i in range(2):
            if usuario in usuarios.keys() and contraseña in usuarios.values():
                print("Acceso permitido")
                bandera = True
                break
            else:
                print("Datos incorrectos")
                usuario = input("Ingrese su nombre de usuario: ")
                contraseña = input("Ingrese su contraseña: ")

        if not bandera:
            print("Lo siento, su acceso no es permitido")   
    
    def main():
        ingreso.validacion(ingreso.usuarios)


ejecucion = ingreso
ejecucion.main()  
        

                
