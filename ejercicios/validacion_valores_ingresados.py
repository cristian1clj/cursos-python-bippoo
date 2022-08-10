def validacion_datos(numero):
    try:
        if len(numero) == 0:
            raise ValueError("Error: Debe ingresar algun valor numerico.")
        if int(numero) < 0:
            raise ValueError("Error: solo se admiten valores positivos.")

        return int(numero)

    except ValueError as ve:
        print (ve)

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
            numero1 = validacion_datos(input("\nIngrese el primer numero a : "))
            assert numero1.isnumeric(), "Error: solo se admiten valores numericos."
            numero2 = validacion_datos(input("Ingrese el segundo numero a : "))
            assert numero2.isnumeric(), "Error: solo se admiten valores numericos."

            resultado = numero1 + numero2
            print (f"\nEl resultado es {resultado}")

        elif opcion == "2":
            numero1 = validacion_datos(input("\nIngrese el primer numero a : "))
            assert numero1.isnumeric(), "Error: solo se admiten valores numericos."
            numero2 = validacion_datos(input("Ingrese el segundo numero a : "))
            assert numero2.isnumeric(), "Error: solo se admiten valores numericos."
                    
            resultado = numero1 - numero2
            print (f"\nEl resultado es {resultado}")

        elif opcion == "3":
            numero1 = validacion_datos(input("\nIngrese el primer numero a : "))
            assert numero1.isnumeric(), "Error: solo se admiten valores numericos."
            numero2 = validacion_datos(input("Ingrese el segundo numero a : "))
            assert numero2.isnumeric(), "Error: solo se admiten valores numericos."
                    
            resultado = numero1 * numero2
            print (f"\nEl resultado es {resultado}")

        elif opcion == "4":
            numero1 = validacion_datos(input("\nIngrese el primer numero a : "))
            assert numero1.isnumeric(), "Error: solo se admiten valores numericos."
            numero2 = validacion_datos(input("Ingrese el segundo numero a : "))
            assert numero2.isnumeric(), "Error: solo se admiten valores numericos."

            assert numero2 == 0, "Error: No se pueden realizar divisiones por 0."
                    
            resultado = numero1 / numero2
            print (f"\nEl resultado es {resultado}")

        elif opcion == "5":
            continuar = False
            print ("\nSaliendo del programa...")

        else:
            print ("error: El valor ingresado no se encuentra entre las opciones")
            


if __name__ == "__main__":
    run()
