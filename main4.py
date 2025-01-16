from Practica_1.Investigador import Investigador
from Practica_1.intfz_grafica import intfz_grafica
from Practica_1.Administrador import Administrador
from Practica_1.carga_archivos import carga

carga.obtener_administradores()
carga.obtener_investigadores()
carga.cuadrar_contraseñas_lista_completa()
carga.cuadrar_contraseñas_lista_investigadores()
carga.cuadrar_contrseñas_lista_admins()


inicio = intfz_grafica
inicio.investigador_o_admin()






