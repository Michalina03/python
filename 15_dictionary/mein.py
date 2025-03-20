import uuid
from function import inf, edycja, usuwanie, dodawanie

# Tworzymy książki z unikalnymi ID
ksiazka1 = {"id": str(uuid.uuid4()), "nazwa": "Dzieci z Bulerbyn", "liczbaStron": 324}
ksiazka2 = {"id": str(uuid.uuid4()), "nazwa": "Pies który jezdzil koleja", "liczbaStron": 94}
ksiazka3 = {"id": str(uuid.uuid4()), "nazwa": "Ania z zielonego wzgorza", "liczbaStron": 309}

biblioteka = [ksiazka1, ksiazka2, ksiazka3]

while True:
    print("\ni - wyswietl biblioteke")
    print("d - dodaj ksiazke")
    print("e - edytuj ksiazke")
    print("u - usun ksiazke")
    print("q - wyjscie")

    inp = input("Wybierz opcje: ").lower()

    if inp == "i":
        inf(biblioteka)
    elif inp == "d":
        dodawanie(biblioteka)
    elif inp == "e":
        edycja(biblioteka)
    elif inp == "u":
        usuwanie(biblioteka)
    elif inp == "q":
        break
    else:
        print("Nie ma takiej komendy")
