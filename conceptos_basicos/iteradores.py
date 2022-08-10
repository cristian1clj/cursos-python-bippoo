lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
iterador = iter(lista)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
