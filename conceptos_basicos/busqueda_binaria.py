# Metodo de busqueda que consiste en dividir una lista ordenada a la mitad, validar hacia que lado
# podria estar el valor buscado y repetir el ciclo (dividir y validar) hasta encontrar el valor.

import random

def buscar(lista, inicio, final, valor, contador = 0):
    contador += 1
    if inicio > final:
        return (False, contador)
    
    mitad = (final + inicio) // 2
    
    if lista[mitad] == valor:
        return (True, contador)
    
    elif lista[mitad] > valor:
        return buscar(lista, inicio, mitad - 1, valor, contador = contador)
        
    else:
        return buscar(lista, mitad + 1, final, valor, contador = contador)

if __name__ == '__main__':
    tamano_lista = int(input('\n¿De que tamaño es la lista?'))
    valor_buscar = int(input('¿Cual es el valor a buscar en la lista?'))
    
    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])
    (encontrado, contador) = buscar(lista, 0, len(lista), valor_buscar)
    
    print(encontrado)
    print(lista)
    print(f'\nEl valor {valor_buscar} {"esta" if encontrado else "no esta"} en la lista')
    print(f'\nEl numero de iteraciones ejecutadas con la busqueda lineal es de {contador} veces.')
