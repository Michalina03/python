# 1.Wygeneruj listę 10 liczb losowych z przedziału 1 do 100.


from random import randint


lst = []
n = int(input())
for i in range(n):
    lst.append(randint(1, 100))
print(lst)


# 2.Wygeneruj listę 20 liczb losowych z przedziału 100 do 200. Parzystych niepodzielnych przez 5.


lst = []
while len(lst) != 20:
    rnd = randint(100, 200)
    if rnd % 5 == 0:
        lst.append(rnd)
print(lst)


# 3.Napisz program do którego możemy wprowadzić dowolne zdanie. Niech nasz program wyświetli:
# Ile mamy d,v,b,n,k.


inp = input()
d_ile = 0
for el in inp:
    if el == "d":
        d_ile += 1
print(f"d --- {d_ile}")

from random import randint

lista = [randint(-20, 20) for el in range(100)]
print(lista)
# 5.Napisz program która z przyjmuje jako argument powyższą listę i zwróci mi ile jest liczb mniejszych od 0.


ile_mn = 0
for el in lista:
    if el < 0:
        ile_mn += 1
print(ile_mn)


# 6.Napisz program która z przyjmuje jako argument powyższą listę i zwrócić mi ile jest większych lub równych 0.


print(len(lista) - ile_mn)


# 7.Napisz program która z przyjmuje jako argument powyższą listę i zwrócić mi sumę wszystkich elementów parzystych.


s = 0
for el in lista:
    if el % 2 == 0:
        s += el
print(s)


# 8.Napisz program która z przyjmuje jako argument powyższą listę i zwrócić mi sumę wszystkich elementów nieparzystych .


s = 0
for el in lista:
    if el % 2 != 0:
        s += el
print(s)


# 9.Napisz program która przyjmuje jako argument powyższą listę i zwrócić mi sumę wszystkich elementów podzielnych przez 5 i 7.


s = 0
for el in lista:
    if el % 7 == 0 and el % 5 == 0:
        s += el
print(s)


# 10.Napisz program która z przyjmuje jako argument powyższą listę poprosi o podanie liczby przez użytkownika i powie ile takich liczb występuje na tej liście.


inp = int(input())
ile = 0
for el in lista:
    if el == inp:
        ile += 1
print(ile)


# 11.Zwrócić lise w których będę zawrte idexy pod którymi występują największe wartości i najmniejsze wartości.


lst = []
my_max = max(lista)
for i in range(len(lista)):
    if lista[i] == my_max:
        lst.append(i)
print(lst)


# 12.Napisz program która wygeneruje listę o n wielkości i “zasięgu” podanego przez użytkownika.


lst = []
n = int(input())
maxx = int(input())
minn = int(input())
for i in range(n):
    lst.append(randint(minn, maxx))
print(lst)


# 1. Wyświetl liczby od 1 do 10.


for i in range(10):
    print(i)


# 2. Oblicz sumę liczb od 1 do 100.


my_sum = 0
for i in range(100):
    my_sum += 1
print(my_sum)


# 3. Wyświetl wszystkie parzyste liczby od 1 do 50.


for i in range(1, 51):
    if i % 2 == 0:
        print(i)


for i in range(0, 51, 2):
    print(i)


# 4. Oblicz iloczyn liczb od 1 do 5.


il = 1
for i in range(1, 6, 1):
    il *= i
print(il)
print(1 * 2 * 3 * 4 * 5)


# 5. Wyświetl odwróconą wersję napisu "Hello World!".


s1 = "Hello World!"
s2 = ""
for char in s1:
    s2 = char + s2
print(s2)


# 6. Wyświetl wszystkie litery z podanego słowa.


inp = input()
for el in inp:
    print(el)


# 7. Oblicz sumę elementów listy liczb.


lista = [11, 11, 10]
sum = 0
for el in lista:
    sum += el
print(sum)


# 8. Wyświetl wszystkie liczby od 20 do 30, które są podzielne przez 3.


for number in range(21, 31, 3):
    print(number)


# 9. Znajdź największą liczbę w liście.


lista = [5, 10, 7, 10]
my_max = lista[0]
for number in lista:
    if my_max < number:
        my_max = number
print(number)


# 10. Wyświetl wszystkie liczby od 1 do 100, które są podzielne jednocześnie przez 3 i 5.


for liczby in range(1, 101):
    if liczby % 3 == 0 and liczby % 5 == 0:
        print(liczby)


# # 11. Oblicz średnią arytmetyczną z listy liczb.


lista = [2, 5]
suma = 0
for number in lista:
    suma += number
print(suma / len(lista))


# # 12. Wyświetl wszystkie litery z podanego zdania, pomijając spacje.


inp = input()
my_str = ""
for znak in inp:
    if znak == " ":
        continue
    my_str += znak
print(my_str)


# 13. Oblicz silnię liczby podanej przez użytkownika.


inp = int(input())
silnia = 1
for i in range(1, inp + 1):
    silnia *= i
print(silnia)


# 14. Wyświetl tabliczkę mnożenia (od 1 do 20).


for i in range(1, 21):
    for j in range(1, 21):
        res = i * j
        print(f" {res:3} ", end=" ")
    print("\n")


# 15. Sprawdź, czy podane słowo jest palindromem.


inp = input()
palindromem = True
for i in range(len(inp) // 2):
    if inp[i] != inp[-i - 1]:
        palindromem = False
        break
print(palindromem)


# 16. Zamień wszystkie litery w podanym napisie na wielkie litery.


inp = input()
text = ""
for el in inp:
    text += el.upper()
print(text)


# 18. Wyświetl liczby od 1 do 10 w odwrotnej kolejności.


for i in range(10, 0, -1):
    print(-i)
