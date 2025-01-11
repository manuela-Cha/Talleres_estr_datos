from Laboratorio_no_5.Ordenador import Ordenador
from Laboratorio_no_5.Ordenador_lista import OrdenarLista
from Laboratorio_no_5.Ordenador_agenda import Ordenador_agenda
from Laboratorio_no_2.Usuario import Usuario

ordenador = Ordenador(10)

print("Inicializado:     ")
ordenador.inicializar()
ordenador.mostrar()
print("Ordenando por burbuja...")
ordenador.ordenar_burbuja()
ordenador.mostrar()
print("------------------------------------------------\n")


ordenador.limpiar_ordenador()
print("inicializado de nuevo: ")
ordenador.inicializar()
ordenador.mostrar()
print("Ordenando por selección...")
ordenador.ordenar_seleccion()
ordenador.mostrar()
print("------------------------------------------------\n")

ordenador.limpiar_ordenador()
print("inicializado de nuevo: ")
ordenador.inicializar()
ordenador.mostrar()
print("Ordenando por inserción...")
ordenador.ordenar_insercion()
ordenador.mostrar()
print("------------------------------------------------\n")

ordenador.limpiar_ordenador()
print("inicializado de nuevo: ")
ordenador.inicializar()
ordenador.mostrar()
print("Ordenando por Merge Sort...")
ordenador.ordenar_mergeSort()
ordenador.mostrar()
print("\n------------------------------------------------\n")

ordenador.limpiar_ordenador()
ordenador.inicializar()
ordenador.mostrar()
print("Buscando valor 43:")
resultado = ordenador.busqueda_binaria(43)
print("Resultado de búsqueda:", f"Encontrado en posición {resultado}" if resultado != -1 else "No encontrado")
#---------------------------------------------------------------------------------------------------------------------------

ordenador_lista = OrdenarLista()
ordenador_lista.inicializar(12)
ordenador_lista.mostrar()  
ordenador_lista.ordenar()
ordenador_lista.mostrar()  

#----------------------------------------------------------------------------------------------------------------------------

ordenador_agenda = Ordenador_agenda()

usuario1 = Usuario("Manuela","5","27/3/2003", "Medellin", "1", "manucha@gmail.com", "cll 30#5813")
usuario2 = Usuario("alba","4","22/4/2004", "Cali", "3", "alba@gmail.com", "cll 29#5235")
usuario3 = Usuario("carlos","3","6/7/2005", "Barranquilla", "98766", "carlos@gmail.com", "cll 22#2314")
usuario4 = Usuario("Ana","2","2/7/2006", "Pereira", "75432", "Ana@gmail.com", "cll 27#3313")
usuario5 = Usuario("Melissa","1","8/1/2007", "Manizales", "68315", "Mel@gmail.com", "cll 20#9815")

ordenador_agenda.agregar_Usuario(usuario1)
ordenador_agenda.agregar_Usuario(usuario2)
ordenador_agenda.agregar_Usuario(usuario3)
ordenador_agenda.agregar_Usuario(usuario4)
ordenador_agenda.agregar_Usuario(usuario5)

ordenador_agenda.ordenar()
ordenador_agenda.mostrar()