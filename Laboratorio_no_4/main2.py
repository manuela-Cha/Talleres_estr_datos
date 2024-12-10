from Laboratorio_no_4.Lista_simple import Lista_Simple
from Laboratorio_no_4.Lista_doble import DoubleList
from Laboratorio_no_2.Usuario import Usuario
from Laboratorio_no_4.Nodo_doble import DoubleNode

coleccion1 = DoubleList()
for i in range(0, 21, 2):
    coleccion1.addLast(i)
print(coleccion1)
coleccion1.remove(coleccion1.encontrar_nodo(10))
coleccion1.removeLast()
coleccion1.removeFirst()
print(coleccion1)

#------------------------------------------------------------------------------------------------------------------------
usuario1 = DoubleNode(Usuario("Manuela","12345","27/3/2003", "Medellin", "123456", "manucha@gmail.com", "cll 30#5813"))
usuario2 = DoubleNode(Usuario("alba","54321","22/4/2004", "Cali", "67891", "alba@gmail.com", "cll 29#5235"))
usuario3 = DoubleNode(Usuario("carlos","23415","6/7/2005", "Barranquilla", "98766", "carlos@gmail.com", "cll 22#2314"))
usuario4 = DoubleNode(Usuario("Ana","45321","2/7/2006", "Pereira", "75432", "Ana@gmail.com", "cll 27#3313"))
usuario5 = DoubleNode(Usuario("Melissa","51235","8/1/2007", "Manizales", "68315", "Mel@gmail.com", "cll 20#9815"))

lista_nodos = [usuario1, usuario2, usuario3, usuario4, usuario5]

coleccion2 = DoubleList()
for i in lista_nodos:
    coleccion2.addLast(i)
print(coleccion2)

nuevo_usuario_principio = Usuario.solicitar()
coleccion2.addFirst(nuevo_usuario_principio)
print(coleccion2)

nuevo_usuario_final = Usuario.solicitar()
coleccion2.addLast(nuevo_usuario_final)
print(coleccion2)

nuevo_usuario_cuarto_nodo = DoubleNode(Usuario.solicitar())

coleccion2.addBefore(coleccion2.obtener_nodo_en_posicion(3),nuevo_usuario_cuarto_nodo)
print(coleccion2)
