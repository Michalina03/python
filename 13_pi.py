# Napisz funkcję która wyznaczy nam wartość pi:
import random


def oblicz_pi(liczba_prob):
    liczba_trafien_w_kolo = 0

    for i in range(liczba_prob):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            liczba_trafien_w_kolo += 1

    pi = 4 * liczba_trafien_w_kolo / liczba_prob
    return pi


probki = 1000000  # Im większa liczba próbek, tym dokładniejszy wynik.
PI = oblicz_pi(probki)
print(PI)


# Porównaj tą wartość do wbudowanej metody w pythonie.
import math

print(math.pi == PI)
print(f"{math.pi} == {PI}")
