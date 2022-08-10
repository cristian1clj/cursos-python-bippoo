# Una secuencia de instrucciones de código ejecutada repetidas veces segun un condicional.

TMAX = 20

def run():
    print ("While:")
    contadorW = 0
    while contadorW < TMAX:
        print (f"+ {contadorW + 1}")
        contadorW += 1

    print ("\nFor:")
    frase = input("Escriba algo: ")

    for caracter in frase:
        print (caracter.upper())


if __name__ == "__main__":
    run()