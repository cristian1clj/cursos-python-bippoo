# Una lista es una estructura de datos y un tipo de dato que permite almacenar cualquier tipo de valor ya
# sea enteros, flotantes, cadenas, listas e incluso funciones.
#
# Estructura =>       variable = [datos, datos, datos ...]

lista = ["camilo", 2, 3.345, 'a', "jaime"]
#lista.append ([5, 4, 3, 2, 1])
lista.insert (2, "holaaaaa")
#lista.extend ([243, "arroz", 234.4])

print (lista[0])
print (lista[-3])
print (lista[:])
print (lista[0:3])

for i in range(len(lista)):
    print (lista[i])
