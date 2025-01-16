class Direccion:
    def __init__(self, calle,  nomencalatura,  barrio, 
     ciudad,  edificio, apto):
        self.calle = calle
        self.nomencalatura = nomencalatura
        self.barrio = barrio
        self.ciudad = ciudad
        self.edificio = edificio
        self.apto = apto
    
    def setCalle(self,nCalle):
        self.calle = nCalle

    def setNomenclatura(self, nNomenclatura):
        self.nomencalatura = nNomenclatura

    def setBarrio(self, nBarrio):
        self.barrio = nBarrio

    def setCiudad(self, nCiudad):
        self.ciudad = nCiudad

    def setEdificio(self, nEdificio):
        self.edificio = nEdificio

    def getApto(self):
        return self.apto

    def getCalle(self):
        return self.calle

    def getNomenclatura(self):
        return self.nomenclatura

    def getBarrio(self):
        return self.barrio

    def getCiudad(self):
        return self.ciudad

    def getEdificio(self):
        return self.edificio

    
    def __str__(self):
        return "Ciudad: {}\nCalle: {}\nBarrio: {}\nNomenclatura: {}\nEdificio: {}\nApartamento: {}".format(self.ciudad, self.calle, self.barrio, self.nomencalatura, self.edificio, self.apto)