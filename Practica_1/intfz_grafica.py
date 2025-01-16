from Practica_1.carga_archivos import carga

class intfz_grafica:
    usuario_actual = None
    contrasena_actual = None
    
    @staticmethod
    def investigador_o_admin():
        while True:  
            
            cedula_ingresada = input("Ingrese su cédula: ").strip()
            if not cedula_ingresada:
                print("Cédula no válida. Por favor, intente de nuevo.")
                continue
            
            contrasena_ingresada = input("Ingrese su contraseña: ").strip()
            if not contrasena_ingresada:
                print("Contraseña no válida. Por favor, intente de nuevo.")
                continue
            
            if not carga.validacion_datos(cedula_ingresada, contrasena_ingresada):
                print("Cédula o contraseña incorrectos. Intente nuevamente.")
                continue

            rol = carga.investigador_o_admin_datos(cedula_ingresada)
            
            if rol == "investigador":
                print("\nBienvenido investigador")
               
                nodo_actual = carga.lista_investigadores.first()
                while nodo_actual:
                    if nodo_actual.data.Id == str(cedula_ingresada):
                        investigador = nodo_actual.data
                        break 
                    nodo_actual = nodo_actual.next
                if investigador == None:
                    print(f"No se encontró un investigador")
                    continue 
                
                while True: 
                    print("\nSeleccione la acción que desee realizar:")
                    print("1) Consultar inventario")
                    print("2) Solicitar agregar un nuevo equipo")
                    print("3) generar txt inventario")
                    print("4) generar txt solicitudes")
                    print("5) Salir")
                    
                    try:
                        respuesta = input("Ingrese el número de la acción deseada: ")
                        if respuesta == "1":
                            investigador.consultar_equipos() #LISTA
                        elif respuesta == "2":
                            investigador.solicitar_agregar_equipo() #LISTA
                        elif respuesta == "3":
                            investigador.escribir_inventario_en_txt() #LISTA
                        elif respuesta == "4":
                            investigador.escribir_solicitudes_en_txt()
                        elif respuesta == "5":
                            print("Saliendo del menú de investigador...")
                            break  
                        else:
                            print("Opción no válida.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número.")
            
            elif rol == "administrador":
                print("\nBienvenido administrador")
                nodo_actual = carga.lista_administradores.first()
                while nodo_actual:
                    if nodo_actual.data.Id == str(cedula_ingresada):
                        admin = nodo_actual.data
                        break 
                    nodo_actual = nodo_actual.next
                if admin == None:
                    print(f"No se encontró un investigador")
                    continue
                
                while True: 
                    print("\nSeleccione la acción que desee realizar:")
                    print("1) Consultar inventario")
                    print("2) Agregar un nuevo usuario")
                    print("3) Eliminar un usuario")
                    print("4) Cambiar una contraseña")
                    print("5) Observar solicitudes")
                    print("6) Salir")
                    
                    try:
                        respuesta = input("Ingrese el número de la acción deseada: ")
                        if respuesta == "1":
                            admin.consultar_inventario()
                        elif respuesta == "2":
                            admin.registrar_nuevo_usuario()  # Lista
                        elif respuesta == "3":
                            admin.eliminar_usuario()  # Lista
                        elif respuesta == "4":
                            admin.cambiar_contrasena()  # Lista
                        elif respuesta == "5":
                            admin.visualizar_solicitudes_agregar() #LISTA
                        elif respuesta == "6":
                            print("Saliendo del menú de administrador...")
                            break
                        else:
                            print("Opción no válida.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número.")
            
            else:
                print("Rol no reconocido. Acceso denegado.")
                continue  

    
    

                    
                    


            