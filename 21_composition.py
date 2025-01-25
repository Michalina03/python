class Kolo:
    def __init__(self) -> None:
        pass


class Silnik:
    def __init__(self) -> None:
        pass


class Wlasciciel:
    def __init__(self) -> None:
        pass


class Auto:
    def __init__(self, kolo: Kolo, silnik: Silnik, wlasciciel: Wlasciciel) -> None:
        self.kolo = kolo
        self.silnik = silnik
        self.wlasiciel = wlasciciel


k = Kolo()
s = Silnik()
w = Wlasciciel()
a = Auto(k, s, w)

# --------------------------------------


class Autor:
    def __init__(self, imie):
        self.imie = imie


class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor


class Biblioteka:
    def __init__(self):
        self.ksiazki = []

    def dodaj_ksiazke(self, ksiazka):
        self.ksiazki.append(ksiazka)


autor = Autor("J.K. Rowling")
ksiazka = Ksiazka("Harry Potter", autor)
biblioteka = Biblioteka()


class Kolo:
    def __init__(self, promien):
        self.promien = promien


class Samochod:
    def __init__(self, marka, kola):
        self.marka = marka
        self.kola = kola


kola = [Kolo(15), Kolo(15), Kolo(15), Kolo(15)]
samochod = Samochod("Toyota", kola)

# -------------------------------------


class Oceny:
    def __init__(self) -> None:
        self.matematyka = []
        self.angielski = []

    def dodaj_ocene_matematyka(self, ocena):
        self.matematyka.append(ocena)

    def dodaj_ocene_angielski(self, ocena):
        self.angielski.append(ocena)

    def dodaj_ocene(self, ocena):
        print("a - matematyka")
        print("b - angielski")
        inp = input().lower()
        if inp == "a":
            self.dodaj_ocene_matematyka(ocena)
        elif inp == "b":
            self.dodaj_ocene_angielski(ocena)
        else:
            print("brak takiej komendy")

    def inf(self):
        print(f"\tMatematyka: {self.matematyka}")
        print(f"\tAngielski: {self.angielski}")


class Uczen:
    def __init__(self, imie) -> None:
        self.imie = imie
        self.oceny = Oceny()

    def dodaj_ocene(self, ocena):
        self.oceny.dodaj_ocene(ocena)

    def inf(self):
        print(self.imie)
        self.oceny.inf()


class Uczen:
    def __init__(self) -> None:
        self.hp = 0
        self.mana = 0
        self.oceny = []
        self.edycja_bazowych_statystyk = EdycjaBazowychStatystyk()

    def inf(self):
        print(self.hp)
        print(self.mana)
        print(self.oceny)

    def modyfikacja_hp(self, nowe_hp):
        self.edycja_bazowych_statystyk.modyfikacja_hp(self, nowe_hp)

    def modyfikacja_mana(self, nowe_mana):
        self.edycja_bazowych_statystyk.modyfikacja_mana(self, nowe_mana)

    def dodaj_ocene(self, ocena):
        self.edycja_bazowych_statystyk.dodaj_ocene(self, ocena)


class EdycjaBazowychStatystyk:
    def __init__(self) -> None:
        pass

    def modyfikacja_hp(self, uczen: Uczen, hp):
        uczen.hp = hp

    def modyfikacja_mana(self, uczen: Uczen, mana):
        uczen.mana = mana

    def dodaj_ocene(self, uczen: Uczen, ocena):
        uczen.oceny.append(ocena)


u = Uczen()
u.dodaj_ocene(5)
u.modyfikacja_hp(100)
u.modyfikacja_mana(50)
u.inf()

# -------------------------------------------------


class Postac:
    def __init__(self) -> None:
        self.level = 1
        self.statystic = Statitic()

    def up_level(self):  # <----------------
        self.statystic.level_up(self)  # <----------------

    def inf(self):
        print(self.level)


class Statitic:

    def level_up(self, postac: Postac):
        postac.level += 1


p = Postac()
p.up_level()
p.up_level()
p.up_level()
p.up_level()
p.up_level()
p.inf()
