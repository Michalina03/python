##1. Napisz funkcję, która oblicza sumę dwóch liczb.


def zad1(x, y):
    print(x + y)


zad1(10, 10)


## 2. Utwórz listę liczb całkowitych i wypisz tylko te liczby, które są większe od 10.


lista = [1, 2, 3, 11, 20, 30]


def zad2(lista):
    for el in lista:
        if el > 10:
            print(f"{el}", end=" ")


zad2(lista)


## 3. Napisz funkcję, która zwraca odwróconą wersję łańcucha znakowego.


def zad3(text):
    for i in range(-1, -len(text) - 1, -1):
        print(f"{text[i]}", end="")
    print("\n")


text = "Ala ma kota"


## zad3(text)


def rev(text):
    return text[::-1]


text = "Ala ma kota"
reversed_text = rev(text)
print(reversed_text)


print(text[0])
print(text[2])
print(text[0:5])
print(text[0:10:3])


## 4. Utwórz listę imion i wypisz wszystkie imiona rozpoczynające się na literę "A".


Iminona = ["Ala", "Olek", "Antek"]


def zad4(lista, litera):
    for el in lista:
        if el[0] == litera:
            print(el)


zad4(Iminona, "A")


## 5. Napisz funkcję, która sprawdza, czy dana liczba jest liczbą pierwszą.


def zad5(inp):
    for i in range(2, inp - 1):
        if inp < 2:
            return False
        if inp % i == 0:
            return False
    return True


inp = int(input("Podaj liczbe "))
print(zad5(inp))


## 6. Utwórz listę liczb i oblicz ich średnią arytmetyczną.


def zad6(oceny):
    print(sum(oceny) / len(oceny))


lista = [4, 2]


## 7. Napisz funkcję, która przyjmuje dwie listy i zwraca listę elementów wspólnych obu list.


def zad7(list1, list2):
    wsp_elementy = []
    for el in list1:
        if el in list2 and el not in wsp_elementy:
            wsp_elementy.append(el)
    return wsp_elementy


a = ["a", "a", "b", "c"]
b = ["a", "b"]


print(zad7(a, b))


## 8. Utwórz listę liczb całkowitych i wypisz tylko liczby parzyste.


def zad8(lista):
    r = []
    for el in lista:
        if el % 2 == 0:
            r.append(el)
    return r


l = [1, 2, 3, 4, 5, 6, 7, 8]
print(zad8(l))


## 9. Napisz funkcję, która znajduje najmniejszą i największą wartość w danej liście liczb.


def zad9(lista):
    print(max(lista))
    print(min(lista))


l = [10, 11, 20, 4]
zad9(l)


# 10. Utwórz listę słów i wypisz tylko te słowa, które mają więcej niż 5 znaków.


def zad10(lista, ile):
    for el in lista:
        if len(el) > ile:
            print(f" {el}", end=" ")
    print("\n")


l = ["aaaaaaaa", "aaaa", "bbbbb", "vvvvvvvvvvvv", "c"]
zad10(l, 5)


# 11. Napisz funkcję, która zamienia wszystkie litery w danym łańcuchu znaków na duże litery.


def zad11(string):
    print(string.upper())


zad11("Ala ma kota")


# 12. Utwórz listę liczb i znajdź drugą najmniejszą wartość w tej liście.


def zad12(lista):
    list.sort(lista)
    return lista[1]


l = [1, 2, 3, 4, 5, 2, 1, -1, 10]
print(zad12(l))


# 13. Napisz funkcję, która liczy wystąpienia danego znaku w danym łańcuchu znaków.


def zad13(slowo, znak):
    ile = 0
    for el in slowo:
        if el == znak:
            ile += 1
    return ile


print(zad13("Ala ma kota", "a"))


# 14. Utwórz listę liczb i oblicz sumę wszystkich liczb podzielnych przez 3.


def zad14(lista):
    my_sum = 0
    for el in lista:
        if el % 3 == 0:
            my_sum += el
    return my_sum


l = [5, 6, 9]
print(zad14(l))


# 15. Napisz funkcję, która usuwa duplikaty z danej listy.


def zad15(lista):
    r = []
    for el in lista:
        if el not in r:
            r.append(el)
    return r


print(zad15([1, 1, 2, 2, 3]))
# 16. Utwórz listę liczb i znajdź najczęściej występujący element w tej liście.


def zad16(lista):
    ile = 0
    naj = lista[0]
    for el in lista:
        if ile < lista.count(el):
            ile = lista.count(el)
            naj = el
    return naj


print(zad16([5, 5, 5, 3, 3, 3, 1, 1, 6, 6, 6, 6, 4]))

# 17. Napisz funkcję, która odwraca kolejność elementów w danej liście.


def zad17(inp):
    return inp[::-1]


print(zad17("Ala ma kota"))


# 18. Utwórz dwie listy i połącz je w jedną, tak aby elementy były posortowane rosnąco.


def zad18(list_1, list_2):
    list_1.extend(list_2)
    return sorted(list_1)


print(zad18([1, 2, 3, 4], [5, 4, 6, 7, -100]))


# 19. Utwórz listę liczb i znajdź drugą największą wartość w tej liście.


l = [12, 3, 321, 312, 32, 3, 123, 123, 12, 3, 123, 2, 3, 232, 23]


def zad19(list):
    list = sorted(list)
    return list[-2]


print(zad19(l))
