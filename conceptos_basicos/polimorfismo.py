class Coche:
    def ruedas(self):
        print("Este es un carro con cuatro ruedas")

class Moto:
    def ruedas(self):
        print("Esta es una moto con dos ruedas")

class Camion:
    def ruedas(self):
        print("Este es un camion con seis ruedas")

def ruedasVehiculo(vehiculo):
    vehiculo.ruedas()

if __name__ == '__main__':
    # vehiculo = Moto()
    # vehiculo = Camion()
    vehiculo = Coche()
    ruedasVehiculo(vehiculo)
