from Practica_1.Investigador import Investigador
from Practica_1.intfz_grafica import intfz_grafica
from Practica_1.Administrador import Administrador
from Practica_1.carga_archivos import carga

carga.carga_empleados_existentes()
carga.carga_equipos_existentes()
carga.carga_solicitudes_existentes()
"""
print("\nAntes de cambiar la contra: ",carga.lista_investigadores_y_administradores,"\n")
"""
inicio = intfz_grafica
inicio.investigador_o_admin()

"""print("\ndespues de cambiar la contra:", carga.lista_administradores,"\n")"""
