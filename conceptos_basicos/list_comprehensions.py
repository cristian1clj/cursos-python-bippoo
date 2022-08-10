# List comprehensions es una manera especial de llenar una lista de manera dinamica, sencilla
# y estetica en python.
#
# Estructura =>        variable = [valor for iterador in valor_a_recorrer]

def run():
    squares = [i for i in range(1, 100000) if i % 36 == 0]

    for value in squares:
        print ("\t~" + str(value))


if __name__ == "__main__":
    run()
