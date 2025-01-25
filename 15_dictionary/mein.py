from lesson.dictionary.meinD import (
    slownik1,
    słownik2,
    słownik3,
    edycja,
    inf_biblioteka,
    usuwanie,
)

ksiązka1 = {"tytuł": "Dzieci z Bulerbyn", "ilość_stron": 324}
ksiązka2 = {"tytuł": "Pies który jeżdził koleją", "ilość_stron": 94}
ksiązka3 = {"tytuł": "Ania z zielonego wzgórza", "ilość_stron": 309}

biblioteka = [ksiązka1, ksiązka2, ksiązka3]


while True:
    print("b - biblioteka ksiązek")
    print("e - edycja słownika")
    print("u - usuwanie słowników")
    inp = input().lower()
    if inp == "b":
        inf_biblioteka(ksiązka1, ksiązka2, ksiązka3)
    elif inp == "e":
        edycja(ksiązka1, ksiązka2, ksiązka3)
    elif inp == "u":
        usuwanie(ksiązka1, ksiązka2, ksiązka3)
    else:
        break
