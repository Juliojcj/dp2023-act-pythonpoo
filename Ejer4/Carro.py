from Vehiculo import Vehiculo


class Carro(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} km/h, {} ruedas, {} cc".format( self.color, self.velocidad, self.ruedas, self.cilindrada )


Carro = Carro("azul", 150, 4, 1200)
print(Carro)