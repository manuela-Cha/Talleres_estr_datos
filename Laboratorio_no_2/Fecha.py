class Fecha:
    def __init__(self, dd, mm, aa):
        self.dd = dd
        self.mm = mm
        self.aa = aa

    def setDia(self,  ndd):
        self.dd = ndd

    def setMes(self, nmm):
        self.mm = nmm

    def setAño(self, naa):
        self.aa = naa
    
    def getDia(self):
        return self.dd

    def getMes(self):
        return self.mm

    def getAño(self):
        return self.aa
    
    def __str__(self):
        return "{}-{}-{}".format(self.dd,self.mm,self.aa)