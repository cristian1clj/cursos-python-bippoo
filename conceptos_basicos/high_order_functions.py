# Las high order functions son metodos de filtrado python que permiten filtrar datos de una lista o estructura de
# datos.

from functools import reduce

def run():
    numbers = [1, 3, 3, 5, 9, 0, 1, 4, 6, 8, 7]
    
    multipleThree = list(filter(lambda num: num % 3 == 0, numbers))
    squares = list(map(lambda num: num**2, numbers))
    result = reduce(lambda num1, num2: num1 + num2, numbers)

    print ("Multiples of three:")
    for num in multipleThree:
        print ("\t~" + str(num))
    
    print ("Squares numbers:")
    for num in squares:
        print ("\t~" + str(num))

    print ("Sum of all numbers:")
    print ("\t~" + str(result))


if __name__ == "__main__":
    run()
