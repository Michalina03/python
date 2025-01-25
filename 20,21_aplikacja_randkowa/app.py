class Osoba:
    def __init__(self, imie, nazwisko, wiek) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def info(self):
        print(f"Imie - {self.imie}")
        print(f"Nazwisko - {self.nazwisko}")
        print(f"Wiek - {self.wiek}")

    def edytuj_imie(self, nowe_imie):
        self.imie = nowe_imie

    def edytuj_nazwisko(self, nowe_nazwisko):
        self.nazwisko = nowe_nazwisko

    def edytuj_wiek(self, nowe_wiek):
        self.wiek = nowe_wiek


# ------------------------------------------------------------------
class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, obowiazki):
        super().init(imie, nazwisko, wiek)
        self.obowiazki = obowiazki

    def info(self):
        print(f"Imie - {self.imie}")
        print(f"Nazwisko - {self.nazwisko}")
        print(f"Wiek - {self.wiek}")
        print(f"Obowiazki - {self.obowiazki}")

    def edytuj_obowiazki(self, nowe_obowiazki):
        self.obowiazki = nowe_obowiazki


# ------------------------------------------------------------------


class Manager(Pracownik):
    def init(self, imie, nazwisko, wiek, obowiazki, zarzadzane_dzialy):
        super().init(imie, nazwisko, wiek, obowiazki)
        self.zarzadzane_dzialy = zarzadzane_dzialy

    def info(self):
        super().info()
        print(f"Zarzadzane dzialy - {self.zarzadzane_dzialy}")

    def edytuj_zarzadzane_dzialy(self, nowe_zarzadzane_dzialy):
        self.zarzadzane_dzialy = nowe_zarzadzane_dzialy


class IT(Pracownik):
    def __init__(self, imie, nazwisko, wiek, obowiazki, jezyk_programowania):
        super().init(imie, nazwisko, wiek, obowiazki)
        self.jezyk_programowania = jezyk_programowania

    def info(self):
        super().info()
        print(f"Jezyk programowania - {self.jezyk_programowania}")

    def edytuj_jezyk_programowania(self, nowy_jezyk_programowania):
        self.jezyk_programowania = nowy_jezyk_programowania


class Ksiegowosc(Pracownik):
    def init(self, imie, nazwisko, wiek, obowiazki, doswiadczenie):
        super().init(imie, nazwisko, wiek, obowiazki)
        self.doswiadczenie = doswiadczenie

    def info(self):
        super().info()
        print(f"Doswiadczenie - {self.doswiadczenie} lat")

    def edytuj_doswiadczenie(self, nowe_doswiadczenie):
        self.doswiadczenie = nowe_doswiadczenie


class PomocSprzatajaca(Pracownik):
    def init(self, imie, nazwisko, wiek, obowiazki, staz):
        super().init(imie, nazwisko, wiek, obowiazki)
        self.staz = staz

    def info(self):
        super().info()
        print(f"Staz - {self.staz} miesiecy")

    def edytuj_staz(self, nowy_staz):
        self.staz = nowy_staz


# ------------------------------------------------------------------


class Developer(IT):
    def init(self, imie, nazwisko, wiek, obowiazki, jezyk_programowania):
        super().init(imie, nazwisko, wiek, obowiazki, jezyk_programowania)

    def info(self):
        super().info()

    def edytuj_jezyk_programowania(self, nowy_jezyk_programowania):
        self.jezyk_programowania = nowy_jezyk_programowania


class Hardware(IT):
    def __init__(self, imie, nazwisko, wiek, obowiazki, specjalizacja):
        super().init(imie, nazwisko, wiek, obowiazki, "Brak")
        self.specjalizacja = specjalizacja

    def info(self):
        super().info()
        print(f"Specjalizacja - {self.specjalizacja}")

    def edytuj_specjalizacja(self, nowa_specjalizacja):
        self.specjalizacja = nowa_specjalizacja


class Admin(IT):
    def init(self, imie, nazwisko, wiek, obowiazki, narzedzia_administracyjne):
        super().init(imie, nazwisko, wiek, obowiazki, "Brak")
        self.narzedzia_administracyjne = narzedzia_administracyjne

    def info(self):
        super().info()
        print(f"Narzedzia administracyjne - {self.narzedzia_administracyjne}")

    def edytuj_narzedzia_administracyjne(self, nowe_narzedzia_administracyjne):
        self.narzedzia_administracyjne = nowe_narzedzia_administracyjne


# ------------------------------------------------------------------

o1 = Osoba("Jan", "Kowalski", 30)
o1.info()

p1 = Pracownik("Anna", "Nowak", 25, "Ksiegowosc")
p1.info()
p1.edytuj_obowiazki("Administracja")
p1.info()

m1 = Manager("Tomasz", "Nowicki", 40, "Zarzadzanie", "Sprzedaz")
m1.info()
m1.edytuj_zarzadzane_dzialy("Marketing")
m1.info()

it1 = IT("Marcin", "Kowalczyk", 35, "Programowanie", "Python")
it1.info()
it1.edytuj_jezyk_programowania("JavaScript")
it1.info()

k1 = Ksiegowosc("Alicja", "Wisniewska", 28, "Rozliczenia", 5)
k1.info()
k1.edytuj_doswiadczenie(7)
k1.info()

ps1 = PomocSprzatajaca("Katarzyna", "Mazurek", 22, "Sprzatanie", 3)
ps1.info()
ps1.edytuj_staz(6)
ps1.info()

dev1 = Developer("Jan", "Nowak", 30, "Programowanie", "Python")
dev1.info()
dev1.edytuj_jezyk_programowania("JavaScript")
dev1.info()

hw1 = Hardware("Anna", "Kowalczyk", 25, "Obsluga sprzetu", "Serwery")
hw1.info()
hw1.edytuj_specjalizacja("Sieci")
hw1.info()

admin1 = Admin("Tomasz", "Wislowski", 35, "Administracja", "Active Directory")
admin1.info()
admin1.edytuj_narzedzia_administracyjne("Microsoft Exchange")
admin1.info()
