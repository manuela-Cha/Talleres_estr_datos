class Solicitud:

    def __init__(self, tipo_solicitud, numero_placa_equipo, estado):
        self.tipo_solicitud = tipo_solicitud
        self.numero_placa_equipo = numero_placa_equipo
        self.estado = estado

    def __str__(self):
        return "{} {} {}\n".format(self.tipo_solicitud,self.numero_placa_equipo, self.estado)