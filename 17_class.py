# Klasa Prostokąt: Napisz klasę Prostokat z atrybutami szerokosc i wysokosc.
# Dodaj metody do obliczenia pola i obwodu prostokąta.


class Istota:
    def __init__(self, zyje) -> None:
        self.zyje = zyje


class Prostokat:
    def __init__(self, szerokosc: float = 0, wysokosc: float = 0) -> None:
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

    def pole_p(self) -> float:
        return self.szerokosc * self.wysokosc

    def obwod_p(self) -> float:
        return 2 * self.szerokosc + 2 * self.wysokosc


pr1 = Prostokat()
print(pr1.obwod_p())
print(pr1.pole_p())


pr2 = Prostokat(5, 10)
print(pr2.obwod_p())
print(pr2.pole_p())


# Klasa BankAccount: Stwórz klasę BankAccount,
# która będzie przechowywać atrybuty balance (saldo) i owner (właściciel).
# Zaimplementuj metody do wpłacania i wypłacania pieniędzy oraz do wyświetlania aktualnego salda.


class BankAccount:
    def __init__(self, balance: float = 0, owner: str = None) -> None:
        self.balance = balance
        self.owner = owner

    def withdrawing_money(self, mony: float = 0) -> None:
        if self.balance < mony:
            print("not enough money in the account")
        self.balance -= mony

    def payment_of_money(self, mony: float = 0) -> None:
        self.balance += mony

    def information(self) -> None:
        print(self.owner)
        print(self.balance)


custome_1 = BankAccount(500, "Alex")
custome_1.payment_of_money(500)
custome_1.withdrawing_money(1000)
custome_1.information()


# Klasa Zegar: Utwórz klasę Zegar,
# która będzie reprezentować czas. Klasa powinna mieć atrybuty godzina,
# minuta i sekunda. Dodaj metodę do ustawiania czasu oraz inną do wyświetlania aktualnego czasu.


class Zegar:
    def __init__(self, godzina: int = 0, minuta: int = 0, sekunda: int = 0) -> None:
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda

    def ustaw_czas(self, godzina: int, minuta: int, sekunda: int) -> None:
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda

    def wyswietl_czas(self) -> None:
        return f"{self.godzina:02d}:{self.minuta:02d}:{self.sekunda:02d}"


zegar = Zegar()
zegar.ustaw_czas(10, 25, 30)
print(zegar.wyswietl_czas())


# Klasa Punkt: Zdefiniuj klasę Punkt reprezentującą punkt w przestrzeni 2D.
# Klasa powinna mieć atrybuty x i y. Dodaj metodę do obliczania odległości od innego punktu.


from math import sqrt


class Punkt:

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def odleglosc_od_punktu(self, inny_x: float, inny_y: float) -> float:
        return sqrt((inny_x - self.x) ** 2 + (inny_y - self.y) ** 2)


# Przykład użycia
p1 = Punkt()
print(p1.odleglosc_od_punktu(4, 4))


# Klasa Książka: Stwórz klasę Ksiazka z atrybutami jak tytul,
# autor i liczba_stron. Dodaj metodę do wyświetlania podstawowych informacji o książce.


class Ksiazka:
    def __init__(
        self, tytul: str = None, autor: str = None, liczba_stron: int = 0
    ) -> None:
        self.tytul = autor
        self.autor = autor
        self.liczba = liczba_stron

    def informacje(self) -> None:
        print(f"tytul {self.tytul}")
        print(f"autor {self.autor}")
        print(f"liczba {self.liczba}")


k1 = Ksiazka()
k1.informacje()


# --------------------------------------
class Zegar:
    def __init__(self, godzina: int = 0, minuta: int = 0, sekunda: int = 0) -> None:
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda

    def ustaw_czas(self, godzina: int, minuta: int, sekunda: int) -> None:
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda

    def wyswietl_czas(self) -> None:
        return f"{self.godzina:02d}:{self.minuta:02d}:{self.sekunda:02d}"


zegar = Zegar()
zegar.ustaw_czas(10, 25, 30)
print(zegar.wyswietl_czas())


# ------------------------------------------------------
class Pierwiastek:
    def __init__(self, nazwa, masa_atomowa, liczba_atomowa):
        self.masa_atomowa = masa_atomowa
        self.liczba_atomowa = liczba_atomowa
        self.nazwa = nazwa

    def wyswietl_info(self):
        print(
            f"Pierwiastek {self.nazwa}, masa atomowa {self.masa_atomowa},liczba atomowa  {self.liczba_atomowa}"
        )


Tytan = Pierwiastek("tytan", 48, 22)
Cyrkon = Pierwiastek("cyrkon", 91, 40)
German = Pierwiastek("german", 73, 32)
Azot = Pierwiastek("azot", 14, 7)
Tlen = Pierwiastek("tlen", 16, 8)
Wodor = Pierwiastek("wodor", 1, 1)
Tytan.wyswietl_info()
Cyrkon.wyswietl_info()
German.wyswietl_info()
Azot.wyswietl_info()
Tlen.wyswietl_info()
Wodor.wyswietl_info()


print("====================================================")


class Człowiek:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def wyswietl_info(self):
        print(
            f"Człowiek o imieniu {self.imie}, nazwisku {self.nazwisko} i wieku {self.wiek}"
        )


czlowiek = Człowiek("Basia", "Kociszewska", 19)
czlowiek.wyswietl_info()


class Czołg:
    def __init__(self, moc, model, marka):
        self.moc = moc
        self.model = model
        self.marka = marka

    def wyswietl_info(self):
        print(f"Czołg o mocy {self.moc}, model {self.model} i marce {self.marka}")


czołg = Czołg("1500 KM", "2A4", "leopard")
czołg.wyswietl_info()


class Laptop:
    def __init__(self, pamięć_RAM, model, marka):
        self.pamięć_RAM = pamięć_RAM
        self.model = model
        self.marka = marka

    def wyswietl_info(self):
        print(
            f"Laptop o pamięci {self.pamięć_RAM}, model {self.model} i marce {self.marka}"
        )


laptop = Laptop("32 GB", "Inspiron 3520-9997 15.6", "Dell")
laptop.wyswietl_info()


print("====================================================")
