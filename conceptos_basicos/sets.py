empty_set = set()
print("set vacio => ")
print(empty_set)

my_set = {1, "Hola", 2.25, True, (1, 2, 3)}
print("\nset => ")
print(my_set)
my_set = {1, "Hola", 1, True, (1, 2, 3)}
print("\nset con valor repetido (1) => " )
print(my_set)

my_list = [1, 2, 2, 3, 4, 5, 6, 7, 6, 9]
my_set = set(my_list)
print("\npasar de lista a set => " )
print(my_set)

my_set.add("Hola mundo")
print("\nAdd set => " )
print(my_set)
my_set.update([10, 1, 3, 8])
print("\nUpdate set => " )
print(my_set)
my_set.update([11, 13, 31, 8], {6, 80})
print(my_set)

my_set.discard(2)
print("\nDiscard set => " )
print(my_set)
my_set.remove(80)
print("\nRemove set => " )
print(my_set)
my_set.pop()
print("\nPop set=> " )
print(my_set)
my_set.clear()
print("\nClear set=> " )
print(my_set)

# OPERACIONES CON SETS
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}

my_set3 = my_set1 | my_set2
print("\n union: ")
print(my_set3)
my_set3 = my_set1 & my_set2
print("\n Interseccion: ")
print(my_set3)
my_set3 = my_set1 - my_set2
print("\n Diferencia 1: ")
print(my_set3)
my_set3 = my_set2 - my_set1
print("\n Diferencia 2: ")
print(my_set3)
my_set3 = my_set1 ^ my_set2
print("\n Diferencia simetrica: ")
print(my_set3)