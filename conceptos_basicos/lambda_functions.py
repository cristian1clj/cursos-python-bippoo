# Las funciones lambda son funciones anonimas, las cuales reciben parametros y ejecuta una instruccion de codigo.
#
# Estructura =>          lambda parametro: instrucción

def run():
    palindrome = lambda string: string == string[::-1]

    word = input("Write a word to know if its a palindrome: ")

    if palindrome(word):
        print (f"the word {word} is a palindrome")
    else:
        print (f"the word {word} isnt a palindrome")


if __name__ == "__main__":
    run()
