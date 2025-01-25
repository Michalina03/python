def slownik1(ksiązka1):
    for k, v in ksiązka1.items():
        print(f"klucz - {k} ")
        print(f"wartość - {v}")


def słownik2(ksiązka2):
    for k, v in ksiązka2.items():
        print(f"klucz - {k} ")
        print(f"wartość - {v}")


def słownik3(ksiązka3):
    for k, v in ksiązka3.items():
        print(f"klucz - {k} ")
        print(f"wartość - {v}")


def edycja(ksiązka1, ksiązka2, ksiązka3):
    print("Wybierz słownik który chcesz edytować(1,2,3)")
    inp = input().lower()
    if inp == "1":
        print("--" * 25)
        print("wprowadz klucz jaki chcesz edytować")
        print("--" * 25)
        slownik1(ksiązka1)
        print("--" * 25)
        inp = input()
        ksiązka1[inp] = input("Podaj nowe dane")
    elif inp == "2":
        print("--" * 25)
        print("wprowadz klucz jaki chcesz edytować")
        print("--" * 25)
        słownik2(ksiązka2)
        print("--" * 25)
        inp = input()
        ksiązka2[inp] = input("Podaj nowe dane")
    elif inp == "3":
        print("--" * 25)
        print("wprowadz klucz jaki chcesz edytować")
        print("--" * 25)
        słownik3(ksiązka3)
        print("--" * 25)
        inp = input()
        ksiązka3[inp] = input("Podaj nowe dane")


def inf_biblioteka(ksiązka1, ksiązka2, ksiązka3):
    while True:
        print("1 - ksiązka1")
        print("2 - ksiażka2")
        print("3 - ksiązka3")
        inp = input().lower()
        if inp == "1":
            slownik1(ksiązka1)
        elif inp == "2":
            słownik2(ksiązka2)
        elif inp == "3":
            słownik3(ksiązka3)
        else:
            break


def usuwanie(ksiązka1, ksiązka2, ksiązka3):
    print("Wybierz słownik który chcesz edytować(1,2,3)")
    inp = input().lower()
    if inp == "1":
        print("--" * 25)
        del ksiązka1["tytuł", "ilość stron"]
    elif inp == "2":
        print("--" * 25)
        del ksiązka2["tytuł", "ilość stron"]
    elif inp == "3":
        print("--" * 25)
        del ksiązka3["tytuł", "ilość stron"]
