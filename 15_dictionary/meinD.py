import uuid

def inf(lst):
    for dic in lst:
        print(f"ID: {dic['id']}")
        print(f"Nazwa: {dic['nazwa']}")
        print(f"Liczba stron: {dic['liczbaStron']}")
        print("---" * 10)


def dodawanie(lst):
    nazwa = input("Podaj nazwe ksiazki: ")
    liczba_stron = input("Podaj liczbe stron: ")

    nowa_ksiazka = {
        "id": str(uuid.uuid4()),  # Generujemy unikalne ID
        "nazwa": nazwa,
        "liczbaStron": liczba_stron
    }

    lst.append(nowa_ksiazka)
    print("Ksiazka zostala dodana!")


def edycja(lst):
    """ Edytuje dane ksiazki na podstawie ID """
    book_id = input("Podaj ID ksiazki do edycji: ")
    
    for ksiazka in lst:
        if ksiazka["id"] == book_id:
            print("Obecne dane ksiazki:")
            print(f"Nazwa: {ksiazka['nazwa']}")
            print(f"Liczba stron: {ksiazka['liczbaStron']}")

            ksiazka["nazwa"] = input("Podaj nowa nazwe: ")
            ksiazka["liczbaStron"] = input("Podaj nowa liczbe stron: ")
            print("Ksiazka zostala zaktualizowana!")
            return

    print("Nie znaleziono ksiazki o podanym ID")


def usuwanie(lst):
    """ Usuwa ksiazke na podstawie ID """
    book_id = input("Podaj ID ksiazki do usuniecia: ")

    for ksiazka in lst:
        if ksiazka["id"] == book_id:
            lst.remove(ksiazka)
            print("Ksiazka zostala usunieta!")
            return

    print("Nie znaleziono ksiazki o podanym ID")

