import re as re
from Laboratorio_no_4.Lista_doble import DoubleList
class carga:

    #carga de empleados en lista
    def cargar_Empleados_en_lista():
        lista = DoubleList()
        try:
            with open("Practica_1/Empleados.txt", "r") as file:
                for line in file:
                    lista.addLast(line.strip())  
        except FileNotFoundError:
            print(f"Archivo no encontrado")
        return lista

    #carga de datos de Password en una lista
    def cargar_Password_en_lista():
        lista = DoubleList()
        try:
            with open("Practica_1/Password.txt", "r") as file:
                for line in file:
                    lista.addLast(line.strip())  
        except FileNotFoundError:
            print(f"Archivo no encontrado")
        return lista


    def validacion_datos(cedula, contrasena):
        lista_empleados = carga.cargar_Password_en_lista()
        nodo_actual = lista_empleados.first()
        while nodo_actual:
            datos = nodo_actual.data.split(" ") 
            if datos[0] == cedula and datos[1] == contrasena:
                return True
            nodo_actual = nodo_actual.next  
        return False
                
            
    def investigador_o_admin_datos(cedula):
        lista_password = carga.cargar_Password_en_lista()
        nodo_actual = lista_password.first()
        while nodo_actual:
            datos = nodo_actual.data.split(" ") 
            if datos[0] == cedula:
                return datos[2]
            nodo_actual = nodo_actual.next  
        return False
            

    def guardar_lista_en_archivo_password(lista):
        with open("Practica_1/Password.txt", 'w') as archivo:
            nodo_actual = lista.first()
            while nodo_actual:
                archivo.write(nodo_actual.data + '\n')
                nodo_actual = nodo_actual.next

    def guardar_lista_en_archivo_empleados(lista):
        with open("Practica_1/Empleados.txt", 'w') as archivo:
            nodo_actual = lista.first()
            while nodo_actual:
                archivo.write(nodo_actual.data + '\n')
                nodo_actual = nodo_actual.next


    def eliminar_usuario_Password_datos(cedula):
        lista_password = carga.cargar_Password_en_lista()  
        nodo_actual = lista_password.first()
        while nodo_actual:
            datos = nodo_actual.data.split(" ") 
            if datos[0] == cedula: 
                lista_password.remove(nodo_actual) 
                carga.guardar_lista_en_archivo_password(lista_password)
                return True  
            nodo_actual = nodo_actual.next  
        return False  
    
    def eliminar_usuario_Empleados_datos(cedula):
        lista_empleados = carga.cargar_Empleados_en_lista()
        nodo_actual = lista_empleados.first()
        while nodo_actual:
            datos = nodo_actual.data.split(" ") 
            if datos[1] == cedula: 
                lista_empleados.remove(nodo_actual) 
                carga.guardar_lista_en_archivo_empleados(lista_empleados)
                return True  
            nodo_actual = nodo_actual.next  
        return False 
        
    
    def inicializador(cedula):
        lista_empleados = carga.cargar_Empleados_en_lista()
        nodo_actual = lista_empleados.first()
        while nodo_actual:
            datos = nodo_actual.data.split(" ") 
            if datos[1] == cedula:
                nombre = datos[0]
                fecha_nacimiento = datos[2:5]
                ciudad_nacimiento = datos[5]
                tel = datos[6]
                email = datos[7]
                dir = datos[8:]
                return nombre,cedula,fecha_nacimiento,ciudad_nacimiento,tel,email,dir
            nodo_actual = nodo_actual.next  
        return False
        


                
             

