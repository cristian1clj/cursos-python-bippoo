from collections import Counter, defaultdict, OrderedDict, UserDict

lista = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
cnt = Counter(lista)
print(cnt)
print(cnt[1])

diccionario = defaultdict(int)
diccionario['uno'] = 1
print(diccionario)

diccionario1 = OrderedDict()
diccionario1[3] = 'hola'
diccionario1[1] = 'chao'
diccionario1[4] = 'no se'
diccionario1[2] = 'que mas'
print(diccionario1)
