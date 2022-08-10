def removeDuplicados(lista):
    return list(set(lista))

def run():
    lista = [1, 1, 2, 2, 4]
    final_lista = removeDuplicados(lista)
    print(final_lista)

if __name__ == '__main__':
    run()