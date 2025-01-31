from Practica_1.intfz_grafica import intfz_grafica
from Practica_1.carga_archivos import carga

carga.carga_empleados_existentes()
carga.carga_equipos_existentes()
carga.carga_solicitudes_existentes()

inicio = intfz_grafica
inicio.investigador_o_admin()

