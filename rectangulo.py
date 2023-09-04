class rectangulo:
    def __init__ (self, longitud, ancho):
        self.longitud= longitud
        self.ancho=ancho

    def calcularArea(self):
        self.Area= self.longitud * self.ancho
        return self.Area
    
    def calcularPerimetro (self):
        self.suma= self.longitud + self.ancho
        self.Perimetro= 2 * self.suma
        return self.Perimetro
    
    def cambiarLongitud(self, longitud):
        self.longitud=longitud
        
    def cambiarAncho(self, ancho):
        self.ancho=ancho

Rectangulo=rectangulo(6,8)
print(Rectangulo.calcularArea())
print(Rectangulo.calcularPerimetro())