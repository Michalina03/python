# append( element ): Dodaje element na końcu listy.


lista = [1, 2, 3]
lista.append(4)
print(lista)  # [1, 2, 3, 4]


# Rozszerza listę dodając na końcu wszystkie elementy z danego iterowanego obiektu.


lista1 = [1, 2, 3]
lista2 = [4, 5]
lista1.extend(lista2)
print(lista1)  # [1, 2, 3, 4, 5]


# insert( index, element ): Wstawia element w określonej pozycji.


lista = [1, 2, 4]
lista.insert(2, 3)
print(lista)  # [1, 2, 3, 4]


# remove( element ): Usuwa pierwsze wystąpienie danego elementu.


lista = [1, 2, 3, 2]
lista.remove(2)
print(lista)  # [1, 3, 2]


# Usuwa element z określonej pozycji i zwraca go. Jeśli nie podano indeksu, usuwa i zwraca ostatni element.


lista = [1, 2, 3, 4]
x = lista.pop(2)
print(lista)  # [1, 2, 4]
print(x)  # 3


# Zwraca indeks pierwszego wystąpienia danego elementu.


lista = [1, 2, 3, 4, 2]
idx = lista.index(2)
print(idx)  # 1


# count( element ): Zwraca liczbę wystąpień danego elementu w liście.


lista = [1, 2, 3, 4, 2]
liczba = lista.count(2)
print(liczba)  # 2


# sort(): Sortuje listę in-place.


lista = [3, 1, 4, 2]
lista.sort()
print(lista)  # [1, 2, 3, 4]


# reverse(): Odwraca kolejność elementów w liście in-place.


lista = [1, 2, 3, 4]
lista.reverse()
print(lista)  # [4, 3, 2, 1]


# clear(): Czyści listę, usuwając wszystkie elementy.


lista = [1, 2, 3, 4]
lista.clear()
print(lista)  # []
