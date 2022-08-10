def es_palindromo(palabra):
    palabra = palabra.replace(' ', '').upper()

    if palabra == palabra[::-1]:
        return True
        
    else:
        return False

def run():
    palabra = input("\nEscriba una palabra para saber si es un palindromo: ")

    if es_palindromo(palabra):
        print ("\nLa palabra '" + palabra + "' SI es un palindromo.")
    
    else:
        print ("\nLa palabra '" + palabra + "' NO es un palindromo.")


if __name__ == "__main__":
    run()
