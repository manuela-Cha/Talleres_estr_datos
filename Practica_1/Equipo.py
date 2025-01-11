class Equipo:

    def __init__(self, nombre_equipo, numero_placa, fecha_compra, valor_compra, empleado_asociado):
        self.nombre_equipo = nombre_equipo
        self.numero_placa = numero_placa
        self.fecha_compra = fecha_compra
        self.valor_compra = valor_compra
        self.empleado_asociado = empleado_asociado


    def crear_equipo(nombre_equipo, numero_placa, fecha_compra, valor_compra, empleado_asociado):
        return