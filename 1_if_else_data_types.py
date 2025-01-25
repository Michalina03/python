import math

print("Pola figur płaskich:")

print("Pole trójkąta")
a = float(input("bok a = "))
b = float(input("bok b = "))
c = float(input("bok c = "))
p = 0.5 * (a + b + c)
P = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(f"Pole = {P}")

print("Pole kwadratu")
a = float(input("bok a = "))
P = a * a
print(f"Pole = {P}")

print("Pole prostokąta")
a = float(input("bok a = "))
b = float(input("bok b = "))
P = a * b
print(f"Pole = {P}")

print("Pole równoległoboku")
a = float(input("bok a = "))
h = float(input("wysokość h = "))
P = a * h
print(f"Pole = {P}")

print("Pole koła")
r = float(input("promień r = "))
P = math.pi * (r * r)
print(f"Pole = {P}")

print("Pole rombu - sposób 1")
a = float(input("bok a = "))
h = float(input("wysokość h = "))
P = a * h
print(f"Pole = {P}")

print("Pole rombu - sposób 2")
e = float(input("krótsza przekątna e = "))
f = float(input("dłuzsza przekątna f = "))
P = (e * f) / 2
print(f"Pole = {P}")


print("Pola brył:")

print("Pole sześcianu")
d = float(input("krawędź sześcianu = "))


p = 6 * d * d
print(f"Pole = {p}")

print(" ")

print("Pole prostopadłościanu")
e = float(input("krawedź ściany bocznej a = "))
f = float(input("krawedź ściany bocznej b = "))
g = float(input("krawedź podstawy = "))

p = 2 * e * f + 2 * e * g + 2 * f * g
print(f"Pole = {p}")

print(" ")

print("Pole walca")
h = float(input("promień podstawy = "))
i = float(input("wysokość = "))
j = math.pi

p = 2 * j * h * h + 2 * j * i
print(f"Pole = {p}")

print(" ")

print("Pole stożka")
k = float(input("promień podstawy = "))
l = float(input("przeciwprostokątna = "))
m = math.pi

p = m * (k + l)
print(f"Pole = {p}")

print(" ")

print("Pole kuli")
n = float(input("promień podstawy = "))
o = math.pi

p = 4 * o * n * n
print(f"Pole = {p}")

# ------------------------------------------
# 1. Napisz program, który poprosi użytkownika o wprowadzenie swojego imienia i przechowa je w zmiennej. Następnie wyświetl komunikat "Witaj, [imię]!".


imie = input()
print(f"Witaj {imie} !")
print("Witaj " + imie + " !")


# 2. Stwórz dwie zmienne liczbowe i przypisz im wartości. Następnie wykonaj operację dodawania tych zmiennych i wyświetl wynik.


a = 10
b = 20
wynik = a + b
print(a + b)
print(wynik)


# 3. Poproś użytkownika o podanie swojego wieku. Zapisz wartość w zmiennej, a następnie sprawdź, czy osoba jest pełnoletnia (czy jej wiek jest większy lub równy 18). Wyświetla odpowiedni komunikat.


wiek = int(input("Podaj wiek = "))
if wiek >= 18:
    print("Jest pelnoletni")
else:
    print("Nie jest")


# 4. Zadeklaruj zmienną tekstową, która będzie przechowywać dowolny ciąg znaków. Następnie wyświetl długość tego ciągu.


text = input()
print(len(text))


# 5. Zadeklaruj dwie zmienne tekstowe przechowujące imię i nazwisko. Połącz te zmienne w jeden ciąg znaków i wyświetl wynik.


imie = input("imie")
nazwisko = input("nazwisko")
print(f"{imie} {nazwisko}")


# 6. Stwórz zmienną przechowującą liczbę. Zmniejsz wartość tej zmiennej o 5, a następnie pomnóż przez 2. Wyświetl ostateczny wynik.


a = 10
# a = a - 5
a -= 5
a *= 2
print(a)


# 7. Zadeklaruj zmienną przechowującą wartość logiczną (True lub False). Następnie wykonaj negację tej wartości i wyświetla wynik.


czy_baotaty = True
print(f"{not(czy_baotaty)}")


# 8. Stwórz zmienną przechowującą wartość liczbową i zmiennoprzecinkową. Przekonwertuj wartość liczbową na zmiennoprzecinkową i wykonaj dodawanie obu zmiennych. Wyświetl wynik.


a = float(input())
b = int(input())
print(float(a) + b)


# 9. Poproś użytkownika o podanie temperatury w stopniach Celsiusza. Przekonwertuj tę wartość na stopnie Fahrenheita, używając odpowiedniego wzoru. Wyświetl wynik.


t = float()
f = 9 / 5 * t + 32
print(t)


# 10. Zadeklaruj zmienną przechowującą dowolny ciąg znaków. Następnie wyświetl pierwszą i ostatnią literę tego ciągu.


inp = input()
print(inp[0])
print(inp[-1])
print(inp[len(inp) - 1])
