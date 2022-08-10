# Dictionary comprehensions es una manera especial de llenar un diccionario de manera dinamica, sencilla
# y estetica en python.
#
# Estructura =>        variable = {key:valor for iterador in valor_a_recorrer}

def run():
    squares = {i:i**0.5 for i in range(1, 1001)}

    for key, value in squares.items():
        print (f"\t~Raiz cuadrada de {key} = {round(value, 2)}")


if __name__ == "__main__":
    run()
