# Un diccionario es una estructura de datos y un tipo de dato que permite almacenar cualquier tipo de valor ya
# sea enteros, flotantes, cadenas, listas e incluso funciones. Ademas, permite identificar cada elemento por una
# key.
#
# Estructura =>       variable = {key: datos, key: datos, key: datos ...}

diccionario = {"persona":"camilo", "perro":"lucky", "gato":"luna"}
print (diccionario["persona"])

diccionario["oveja"] = "oscar"
print (diccionario)

diccionario["gato"] = "agata"
print (diccionario)

# del diccionario["persona"]
# print (diccionario)

# for serVivo in diccionario.keys():
#     print(serVivo)

# for serVivo in diccionario.values():
#     print(serVivo)

#diccionario |= {"carro":"ferrari", "moto":"bmw", "chocolatina":"jumbo"}

for raza, nombre in diccionario.items():
    print("Key: " + raza + " value: " + nombre)
    
print(diccionario["gato"])
