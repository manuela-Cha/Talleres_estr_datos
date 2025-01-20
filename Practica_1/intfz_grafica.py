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
                    print("5) consultar estado solicitudes")
                    print("6) solicitar eliminar equipo")
                    print("7) Salir")
                    
                    try:
                        respuesta = input("Ingrese el número de la acción deseada: ")
                        if respuesta == "1":
                            investigador.consultar_equipos() 
                        elif respuesta == "2":
                            investigador.solicitar_agregar_equipo() 
                        elif respuesta == "3":
                            investigador.escribir_inventario_en_txt() 
                        elif respuesta == "4":
                            investigador.escribir_solicitudes_en_txt() 
                        elif respuesta == "5":
                            investigador.consultar_estado_solicitudes() 
                        elif respuesta == "6":
                            investigador.solicitar_eliminar_equipo()
                        elif respuesta == "7":
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
                    print("1) Agregar un nuevo usuario")
                    print("2) Eliminar un usuario")
                    print("3) Cambiar una contraseña")
                    print("4) Observar solicitudes para agregar equipos")
                    print("5) Generar txt investigador dado")
                    print("6) Agregar un equipo al inventario propio")
                    print("7) Consultar inventario" )
                    print("8) Observar solicitudes para eliminar equipos")
                    print("9) Salir")
                    
                    try:
                        respuesta = input("Ingrese el número de la acción deseada: ")
                        if respuesta == "1":
                            admin.registrar_nuevo_usuario()  # Lista A MAS NO PODER
                        elif respuesta == "2":
                            admin.eliminar_usuario()  # Lista A MAS NO PODER
                        elif respuesta == "3":
                            admin.cambiar_contrasena()  # Lista A MAS NO PODER
                        elif respuesta == "4":
                            admin.visualizar_solicitudes_agregar() #LISTA
                        elif respuesta == "5":
                            admin.generar_txt_inventario_investigador()
                        elif respuesta == "6":
                            admin.agregar_un_equipo_al_inventario()
                        elif respuesta == "7":
                            admin.mostrar_equipos()
                        elif respuesta == "8":
                            admin.visualizar_solicitudes_eliminar()
                        elif respuesta == "9":
                            print("Saliendo del menú de administrador...")
                            break
                        else:
                            print("Opción no válida.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número.")
            
            else:
                print("Rol no reconocido. Acceso denegado.")
                continue  

    
    

                    
                    


            