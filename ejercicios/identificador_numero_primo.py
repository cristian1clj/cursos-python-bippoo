def es_primo(valor):
    verificacion = True

    if valor == 1 or valor == 0:
        verificacion = False
        return verificacion

    for i in range(1, valor):
        if (valor % i == 0) and (i != 1 and i != valor):
            verificacion = False
            break
    
    return verificacion

def run():
    try:
        numero = int(input("Ingrese el numero a validar: "))

        if es_primo(numero):
            print ("El numero ingresado SI es un numero primo.")
        
        else:
            print ("El numero ingresado NO es un numero primo")

    except:
        print ("Solo se admiten valores numericos.")


if __name__ == "__main__":
    run()
