class casillaDeVotacion:
    def __init__(self, documento, departamento):
        self.__documento = documento
        self.__departamento = departamento
        self.__municipio = None

    @property
    def documento(self, documento):
        return self.__documento

    @documento.setter
    def documento(self, documento):
        if documento.isdigit():
            self.__documento = documento
        
        else:
            raise ValueError("El documento solo inluye valores numericos.")

    @property
    def municipio(self, municipio):
        return self.__municipio

    @municipio.setter
    def municipio(self, municipio):
        if municipio in self.__departamento:
            self.__municipio = municipio
        
        else:
            raise ValueError(f"El municipio {municipio} no corresponde al departamento {self.__departamento}.")

def run():
    municipios = ["Abejorral", "Alejandria", "Argelia", "Carmen de Viboral", "Cocorna", "Concepcion", "El Peñol", "El Retiro", "El Santuario", "Granada", "Guarne", "Guatape", "La Ceja", "La Union", "Marinilla", "Nariño", "Rionegro", "San Carlos", "San Francisco", "San Luis", "San Rafael", "San Vicente", "Sonson"]
    
    documento = input("Ingrese su documento de identidad: ")
    casilla = casillaDeVotacion(documento, municipios)
    casilla.municipio = input("Escriba su municipio de residencia: ")


if __name__ == '__main__':
    run()

# Ejemplo funcion emcapsulada

# class Ejemplo_clase:
#     def __ejemplo():
#         pass