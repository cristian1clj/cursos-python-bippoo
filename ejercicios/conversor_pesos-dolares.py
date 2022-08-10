constPC = 3836
constPM = 20.05
constPA = 98.54

def pesos_dolares (tipoPesos, constP):
    try:
        valor = input("\nIngrese el valor de " + tipoPesos +": ")
        resultado = float(valor) / constP
        resultado = str(round(resultado, 2))

        print ("Conversion: $" + resultado + " (dolares)")

    except:
        print("ERROR: solo se admiten valores numericos.")

def dolares_pesos (tipoPesos, constP):
    try:
        valor = input("\nIngrese el valor de dolares para pasar a " + tipoPesos + ": ")
        resultado = float(valor) * constP
        resultado = str(round(resultado, 2))

        print ("Conversion: $" + resultado + " (" + tipoPesos + ")")

    except:
        print("ERROR: solo se admiten valores numericos.")

def run():
    continuar = True

    while continuar:
        opcion = input("""
            [1] Pasar de pesos Colombianos a dolares.
            [2] Pasar de dolares a pesos Colombianos.
            [3] Pasar de pesos Mexicanos a dolares.
            [4] Pasar de dolares a pesos Mexicanos.
            [5] Pasar de pesos Argentinos a dolares.
            [6] Pasar de dolares a pesos Argentinos.
            [7] Salir del programa.
        + Ingrese la opcion: """)


        if opcion == "1":
            pesos_dolares("pesos colombianos", constPC)

        elif opcion == "2":
            dolares_pesos("pesos colombianos", constPC)

        elif opcion == "3":
            pesos_dolares("pesos mexicanos", constPM)

        elif opcion == "4":
            dolares_pesos("pesos mexicanos", constPM)

        elif opcion == "5":
            pesos_dolares("pesos argentinos", constPA)

        elif opcion == "6":
            pesos_dolares("pesos argentinos", constPA)

        elif opcion == "7":
            continuar = False
            print ("Salio del programa correctamente.")

        else :
            print ("\nEl valor ingresado no se encuentra dispnible como una opcion.")


if __name__ == "__main__":
    run()
    