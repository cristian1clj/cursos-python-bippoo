
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
        try:
            opcion = menu()

            if opcion == "1":
                numero1 = int(input("Ingrese el primer numero a : "))
                numero2 = int(input("Ingrese el segundo numero a : "))

                if numero1 < 0 or numero2 < 0:
                    raise ValueError

                resultado = numero1 + numero2
                print (f"\nEl resultado es {resultado}")

            elif opcion == "2":
                numero1 = int(input("Ingrese el primer numero a : "))
                numero2 = int(input("Ingrese el segundo numero a : "))

                if numero1 < 0 or numero2 < 0:
                    raise ValueError
                    
                resultado = numero1 - numero2
                print (f"\nEl resultado es {resultado}")

            elif opcion == "3":
                numero1 = int(input("Ingrese el primer numero a : "))
                numero2 = int(input("Ingrese el segundo numero a : "))

                if numero1 < 0 or numero2 < 0:
                    raise ValueError
                    
                resultado = numero1 * numero2
                print (f"\nEl resultado es {resultado}")

            elif opcion == "4":
                numero1 = int(input("Ingrese el primer numero a : "))
                numero2 = int(input("Ingrese el segundo numero a : "))

                if numero1 < 0 or numero2 < 0:
                    raise ValueError
                    
                resultado = numero1 / numero2
                print (f"\nEl resultado es {resultado}")

            elif opcion == "5":
                continuar = False
                print ("\nSaliendo del programa...")

            else:
                print ("error: El valor ingresado no se encuentra entre las opciones")

        except ValueError:
            print ("\nerror: solo se admiten numeros positivos.")
            


if __name__ == "__main__":
    run()
