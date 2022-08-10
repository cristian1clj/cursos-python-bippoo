# La herencia es la manera por la que una clase puede heredar los metodos y atributos de otra clase.
# La clase de la que se va a heredar los metodos y atributos es llamada clase padre, mientras que la que
# recive la herencia es llamada clase hija.
# Para generar herencia entre clases hay que pasar el nombre de la clase padre como parametro de la clase hija.
#
# Estructura:          class nombre_clase(nombre_clase_padre):
#                           def __init__ (self, parametros):
#                               codigo...
#                           codigo...

class Figuras_geometricas:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Rectangulo(Figuras_geometricas):
    def __init__(self, base, altura):
        super().__init__(base, altura)

class Cuadrado(Figuras_geometricas):
    def __init__(self, lado):
        super().__init__(lado, lado)

class Triangulo(Figuras_geometricas):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def area(self):
        return super().area()/2


if __name__ == '__main__':
    rectangulo = Rectangulo(4, 9)
    cuadrado = Cuadrado(5)
    triangulo = Triangulo(5, 5)

    print("Area Rectangulo: " + str(rectangulo.area()))
    print("Area Cuadrado: " + str(cuadrado.area()))
    print("Area Triangulo: " + str(triangulo.area()))
