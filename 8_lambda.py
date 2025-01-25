# Napisz funkcję która przyjmuje trzy listy i powie w której z nich znajduje się największa średnia.


def zad1(lst1, lst2, les3):
    sr = lambda lst: sum(lst) / len(lst)
    all_lst = [lst1, lst2, les3]
    w = []
    for lst in all_lst:
        w.append(sr(lst))
    return w.index(max(w))


print(zad1([1, 2, 3, 4, 5], [-2, -3, -6], [20]))


# Napisz funkcję która generuje losową listę o wielkości k i zakresie n i m.


from random import randint

zad2 = lambda k, n, m: [randint(n, m) for i in range(k)]
print(zad2(10, 10, 20))


# Napisz funkcję która przyjmuje listę i podniesie wszystkie elementy do kwadratu


zad3 = lambda lst: list(map(lambda el: el**2, lst))
print(zad3([2, 3, 4, 5, 6, 7, 8]))

# Napisz funkcję która przyjmuje listę i podniesie wszystkie elementy do 1/2


zad4 = lambda lst: list(map(lambda el: el**1 / 2, lst))
print(zad4([4, 8, 16]))


# Napisz funkcję która przyjmuje listę jako argument w zwróci ile występuje liczb parzystych


zad5 = lambda lst: len(list(filter(lambda x: x % 2 == 0, lst)))
print(zad5([2, 4, 6]))


# Napisz funkcję korzystając z labda i map co
# przyjmuje listę pensji, % podwyżki i liczbę
# lat i zwróci ile będą wynosić pensje po m lat.


def xxx(lst, k, m):
    new_list = lst
    for i in range(m):
        new_list = list(map(lambda x: x * (1 + k / 100), new_list))
    return new_list


print(xxx([100, 100, 100], 10, 2))
