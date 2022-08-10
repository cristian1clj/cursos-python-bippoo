cadena = input("Ingrese su nombre: ")
print (" +" + cadena)

cadena = cadena.upper()
print (" +" + cadena + " (upper)")

cadena  = cadena.capitalize()
print (" +" + cadena + " (capitalize)")

print (str(len(cadena)) + " (len)")

print (cadena[0:3] + " (cadena[0:3])")
print (cadena[2:] + " (cadena[2:])")
print (cadena[1:7:2] + " (cadena[1:7:2])")
print (cadena[::] + " (cadena[::])")
print (cadena[1::3] + " (cadena[1::3])")
print (cadena[::-1] + " (cadena[::-1])")
