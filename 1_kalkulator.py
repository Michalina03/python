print("Hej !")
a = float(input("a:"))
b = float(input("b:"))
c = input("Wybierz opcje: a- dodawanie, b- odejmowanie, c- mnożenie, d- dzielenie")

if c == "a":
    print(f"{a}+{b}={a+b}")
elif c == "b":
    print(f"{a}-{b}={a-b}")
elif c == "c":
    print(f"{a}*{b}={a*b}")
elif c == "d":
    print(f"{a}/{b}={a/b}")
else:
    print("Nie ma takiej opcji")


print("=================================")

import math

a = float(input())
b = float(input())
c = float(input())
if a + b > c and b + c > a and a + c > b:
    p = 1 / 2 * (a + b + c)
    w = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(w)
else:
    print("nie")

print("=================================")

import math

a = float(input())
b = float(input())
c = float(input())
delta = b**2 - 4 * a * c
if delta > 0:
    x1 = -b - math.sqrt(delta) / (2 * a)
    x2 = -b + math.sqrt(delta) / (2 * a)
    print(f"mam 2 pierwiatki x1={x1}x2={x2}")
elif delta == 0:
    x = -b / 2 * a
    print(f"x{x}")
else:
    print("nie ma pierwiastków")

print("=================================")

import math

while True:
    print("li8cz a / zamknij b ")
    inp = input().upper()
    if inp == "A":
        a = float(input())
        b = float(input())
        c = float(input())
        delta = b**2 - 4 * a * c
        if delta > 0:
            x1 = -b - math.sqrt(delta) / (2 * a)
            x2 = -b + math.sqrt(delta) / (2 * a)
            print(f"mam 2 pierwiatki x1={x1}x2={x2}")
        elif delta == 0:
            x = -b / 2 * a
            print(f"x{x}")
        else:
            print("nie ma pierwiastków")
    elif inp == "B":
        break
    else:
        print("nie ma takiej komendy")


print("======================================")

import math

a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    print("to jest trójkt")
    p = 1 / 2 * (a + b + c)
    pp = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(pp)
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("prostoktny")
else:
    print("to nie jest trójkt")
