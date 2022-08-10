
from typing import List


def run():
    lista = [1, "hola", 4.5, True]
    diccionario = {"nombre":"camilo", "apellido":"losada"}

    lista_diccionarios = [
        {"nombre":"camilo", "apellido":"losada"}, 
        {"nombre":"rojelio", "apellido":"martinez"}, 
        {"nombre":"martha", "apellido":"jimenez"}, 
        {"nombre":"Ricardo", "apellido":"losada"}, 
        {"nombre":"Lucky", "apellido":"Primero"}
    ]

    diccionario_listas = {
        "numeros naturales":[1, 2, 3, 4, 5, 6, 7, 8, 9],
        "numeros enteros":[-4, -3, -2, -1, 0, 1, 2, 3, 4],
        "numeros decimales":[1.1, 2.3, 5.2, 7.8, 9.9]
    }

    # print ("Lista de diccionarios:")
    # for valores in lista_diccionarios:
    #     for key, value in valores.items():
    #         print ("\t" + key + ": " + value)
    #     print ("|-----------------------|")
            
    # print ("\nDiccionario de listas:")
    # for key, value in diccionario_listas.items():
    #     print ("\t+Key: " + key + " +value: " +str(value))
        
    print(lista_diccionarios[1].values())


if __name__ == "__main__":
    run()
