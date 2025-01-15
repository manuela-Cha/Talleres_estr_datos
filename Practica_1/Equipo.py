class Equipo:

    def __init__(self, nombre_equipo, numero_placa, fecha_compra, valor_compra):
        self.nombre_equipo = nombre_equipo
        self.numero_placa = numero_placa
        self.fecha_compra = fecha_compra
        self.valor_compra = valor_compra
        self.empleado_asociado = ""

    def get_nombre(self):
        return self.nombre_equipo
    
    def get_numero_placa(self):
        return self.numero_placa
    
    def get_fecha_compra(self):
        return self.fecha_compra
    
    def get_valor_compra(self):
        return self.valor_compra
    
    @staticmethod
    def crear_equipo():
        "print('Ingrese los datos del equipo:\n')"
        
        nombre_equipo = input("Nombre del equipo: ")
        numero_placa = input("numero de la placa: ")
        fecha_compra = input("Fecha de compra: ")
        valor_compra = input("valor de la compra: ")
        
        equipo = Equipo(nombre_equipo, numero_placa, fecha_compra, valor_compra)
        return equipo