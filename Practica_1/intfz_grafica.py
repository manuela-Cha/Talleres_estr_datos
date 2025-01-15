from Practica_1.carga_archivos import carga
from Practica_1.Administrador import Administrador
from Laboratorio_no_2.Usuario import Usuario
from Practica_1.Investigador import Investigador

class intfz_grafica:
    usuario_actual = None
    contrasena_actual = None

    @staticmethod
    def validacion():
        global usuario_actual, contrasena_actual
        print("Bienvenido al inventario, digite su cédula y contraseña\n")
        while True:
            usuario = input("Cédula: ")
            contraseña = input("Contraseña: ")
        
            try:
                if carga.validacion_datos(usuario, contraseña):
                    usuario_actual = usuario
                    contrasena_actual = contraseña
                    return usuario
                else:
                    print("Usuario y/o contraseña inválidos")
            except FileNotFoundError:
                print("Error: El archivo no existe.")
                break

    @staticmethod
    def investigador_o_admin():
        rol = carga.investigador_o_admin_datos(intfz_grafica.validacion())
        if rol == "investigador":
            print("\nBienvenido investigador")
            print("Seleccione la acción que desee realizar:")
            print("1) Consultar inventario")
            print("2) Solicitar agregar un nuevo equipo")
            nombre, cedula, fecha_nacimiento, ciudad_nacimiento, tel, email, dir = carga.inicializador(usuario_actual) 
            investigador = Investigador(contrasena_actual, nombre, cedula, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
            try:
                respuesta = input("Ingrese el número de la acción deseada: ")
                if respuesta == "1":
                    investigador.consultar_equipos()
                elif respuesta == "2":
                    investigador.solicitar_agregar_equipo()
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

        elif rol == "administrador":
            print("\nBienvenido administrador")
            print("Seleccione la acción que desee realizar:")
            print("1) Consultar inventario")
            print("2) Agregar un nuevo usuario")
            print("3) Eliminar un usuario")
            print("4) Cambiar una contraseña")
            nombre, cedula, fecha_nacimiento, ciudad_nacimiento, tel, email, dir = carga.inicializador(usuario_actual) 
            admin = Administrador(contrasena_actual, nombre, cedula, fecha_nacimiento, ciudad_nacimiento, tel, email, dir)
            try:
                respuesta = input("Ingrese el número de la acción deseada: ")
                if respuesta == "2":
                    admin.registrar_nuevo_usuario()
                elif respuesta == "3":
                    admin.eliminar_usuario()  
                elif respuesta == "4":
                    admin.cambiar_contrasena() 
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        else:
            print("Rol no reconocido. Acceso denegado.")

            
            


        