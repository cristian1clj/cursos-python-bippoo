# "assert statements" son usados para continuar la ejecución si la condición se cumple, de otra manera
# se generará un AssertError exception con la especificación dada.
#
# Estrucutra =>     assert condición, mensaje_error

def menu():
    opcion = input("""
        [1] suma.
        [2] resta.
        [3] multiplicacion.
        [4] division.
        [5] Salir.
    Ingrese la opcion: """)

    return opcion

def run():
    continuar = True

    while continuar:
        opcion = menu()

        if opcion == "1":
            numero1 = int(input("Ingrese el primer numero a : "))
            assert numero1 > 0, "No se pueden ingresar valores menores a"
            numero2 = int(input("Ingrese el segundo numero a : "))
            assert numero2 > 0, "No se pueden ingresar valores menores a"

            resultado = numero1 + numero2
            print (f"\nEl resultado es {resultado}")

        elif opcion == "2":
            numero1 = int(input("Ingrese el primer numero a : "))
            assert numero1 > 0, "No se pueden ingresar valores menores a"
            numero2 = int(input("Ingrese el segundo numero a : "))
            assert numero2 > 0, "No se pueden ingresar valores menores a"
                
            resultado = numero1 - numero2
            print (f"\nEl resultado es {resultado}")

        elif opcion == "3":
            numero1 = int(input("Ingrese el primer numero a : "))
            assert numero1 > 0, "No se pueden ingresar valores menores a"
            numero2 = int(input("Ingrese el segundo numero a : "))
            assert numero2 > 0, "No se pueden ingresar valores menores a"
                
            resultado = numero1 * numero2
            print (f"\nEl resultado es {resultado}")

        elif opcion == "4":
            numero1 = int(input("Ingrese el primer numero a : "))
            assert numero1 > 0, "No se pueden ingresar valores menores a"
            numero2 = int(input("Ingrese el segundo numero a : "))
            assert numero2 > 0, "No se pueden ingresar valores menores a"
                
            resultado = numero1 / numero2
            print (f"\nEl resultado es {resultado}")

        elif opcion == "5":
            continuar = False
            print ("\nSaliendo del programa...")

        else:
            print ("error: El valor ingresado no se encuentra entre las opciones")        


if __name__ == "__main__":
    run()
