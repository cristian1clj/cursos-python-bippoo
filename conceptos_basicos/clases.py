# Una clase es un molde para recrear objetos en el codigo.
# Un objeto es algo que cuenta con acciones y caracteristicas (Carro => Caracteristicas:[llantas, modelo, color...]
#                                                                    => Acciones:[Acelerar, frentar, encender...])
#
# Una clase debe tener un metodo __init__ donde se le definan los atributos del objeto.

class Persona:

    def __init__(self, nombre, anios):
        self.nombre = nombre
        self.anios = anios

    # def diferencia_edad(self, otra_persona):
    #     edad_diff = self.anios - otra_persona.anios

    #     return edad_diff

    def mostrar(self):
        return f"{self.nombre} = {self.anios}"


if __name__ == '__main__':
    persona1 = Persona("carlitos", "")
    persona2 = Persona("markos", 12)

    # print(persona1.diferencia_edad(persona2))
    print(persona1.mostrar())
