# La busqueda lineal, como su nombre lo dice es un algoritmo en el cual se busca un valor en una lista
# recorriendo cada una de las posiciones hasta encontrarlo, de manera que el tiempo de ejecución aumentará
# linealmente conforme aumenten los valores a recorrer, lo que se puede representar como O(n).

import random

def buscar_valor(lista, valor, contador = 0):
    for i in lista:
        contador += 1
        
        if i == valor:
            return (True, contador)
        
    return (False, contador)

if __name__ == '__main__':
    tamano_lista = int(input('\n¿De que tamano es la lista? '))
    valor_buscar = int(input('¿Que valor desea buscar en la lista? '))
    
    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    
    (encontrado, contador) = buscar_valor(lista, valor_buscar)
    print(lista)
    print(f'\nEl valor {valor_buscar} {"esta" if encontrado else "no esta"} en la lista')
    print(f'\nEl numero de iteraciones ejecutadas con la busqueda lineal es de {contador} veces.')
