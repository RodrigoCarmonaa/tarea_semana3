class circulo:
    def __init__  (self, radio):
        self.radio=radio 

    def calcular_area(self):
        return 3,14* (self.radio**2)
    
    def calcular_Perimetro (self):
        return 2 * 3,14 * self.radio 
    
    def cambiar_radio( self, radio):
        self.radio=radio

Circulo= circulo(14)
print(Circulo.calcular_area())
print(Circulo.calcular_Perimetro())