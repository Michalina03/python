# Definiowanie zbiorów
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}


# Operacje na zbiorach
union = a | b
intersection = a & b
difference = a - b
symmetric_difference = a ^ b


# Wyświetlanie wyników
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
print("Symmetric Difference:", symmetric_difference)


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {5, 6, 9, 10}


# Suma zbiorów A, B i C zad.1
def zad1(a, b, c):
    return a | b | c


print(zad1(A, B, C))  # Wypisze sumę zbiorów zad


# Iloczyn zbiorów A i B zad.2
def zad2(a, b):
    return a & b


print(zad2(A, B))


# Usunięcie wszystkich elementów ze zbioru C zad.3
def zad3(s):
    s.clear()
    return s


C_copy = C.copy()
print(zad3(C_copy))


# Sprawdzenie, czy A jest podzbiorem B zad.4
def zad4(a, b):
    return a.issubset(b)


print(zad4(A, B))  # Wypisze False, ponieważ A nie jest podzbiorem B


# Z5 Utwórz zbiór D zawierający elementy od 1 do 10 za pomocą funkcji range/set i porównaj go ze zbiorem A. Napisz funkcję, która zwróci elementy, które są w D, ale nie ma ich w A.


def zad5(a):
    D = set(range(1, 11))
    return D - a


print(zad5(A))


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {5, 6, 9, 10}


# Z6 Napisz funkcję, która zwróci symetryczną różnicę zbiorów B i C.


def zad6(a: set, b: set):
    return a.symmetric_difference(b)


print(zad6(A, B))

# Z7 Utwórz skrypt, który doda element 11 do wszystkich trzech zbiorów A, B i C.
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {5, 6, 9, 10}


def zad7(a: set, b: set, c: set, n: int):
    a.add(n)
    b.add(n)
    c.add(n)


print(A)
print(B)
print(C)


# Z8 Napisz funkcję, która zwróci różnicę między zbiorem B a zbiorem A.


def zad8(b: set, a: set):
    return b - a


# Z9 Napisz funkcję, który utworzy zbiór E zawierający wszystkie parzyste liczby zawarte w zbiorach A, B i C.


def zad9(a: set, b: set, c: set):
    E = set()
    for el in a:
        if el not in E and el % 2 == 0:
            E.add(el)
    for el in b:
        if el not in E and el % 2 == 0:
            E.add(el)
    for el in c:
        if el not in E and el % 2 == 0:
            E.add(el)
    return E


print(zad9(A, B, C))
