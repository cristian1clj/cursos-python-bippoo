import random

def validar_numero(numeroCorrecto, numeroUsuario):

    if numeroUsuario > numeroCorrecto:
        print ("Busca un numero mas pequeño.")
        return False

    elif numeroUsuario < numeroCorrecto:
        print ("Busca un numero mas grande.")
        return False

    elif numeroUsuario == numeroCorrecto:
        print ("GANASTE!!! el numero es " + str(numeroCorrecto) + ".")
        return True

def run():
    correcto = False
    numeroAleatorio = random.randint(1, 100)

    while correcto == False:
        try:
            numeroUsuario = int(input("\nIntente adivinar el numero (entre 1 y 100): "))

            if numeroUsuario > 100 or numeroUsuario < 1:
                print ("Solo se pueden ingresar numeros entre el 1 y el 100.")
                continue

            correcto = validar_numero(numeroAleatorio, numeroUsuario)

        except:
            print ("Solo se admiten valores numericos.")


if __name__ == "__main__":
    run()
