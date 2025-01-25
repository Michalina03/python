class Pracownik:
    def __init__(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
        self.ocena_pracy = ocena_pracy
        self.doswiadczenie = doswiadczenie
        self.podgrupa = podgrupa

    def zmien_pensje(self, nowa_pensja):
        self.pensja = nowa_pensja

    def zmien_ocene_pracy(self, nowa_ocena):
        self.ocena_pracy = nowa_ocena

    def zmien_doswiadczenie(self, nowe_doswiadczenie):
        self.doswiadczenie = nowe_doswiadczenie

    def zmien_nazwisko(self, nowe_nazwisko):
        self.nazwisko = nowe_nazwisko

    def opis(self):
        print(f"Imię: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"Pensja: {self.pensja}")
        print(f"Ocena pracy: {self.ocena_pracy}")
        print(f"Doświadczenie: {self.doswiadczenie}")
        print(f"Podgrupa: {self.podgrupa}")


class Pracownik_Montazu:
    def __init__(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
        self.pracownik = Pracownik(
            imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa
        )


class Pracownik_IT:
    def __init__(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
        self.pracownik = Pracownik(
            imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa
        )


class Pracownik_Organizacji_Pracy:
    def __init__(self, imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa):
        self.pracownik = Pracownik(
            imie, nazwisko, pensja, ocena_pracy, doswiadczenie, podgrupa
        )


prac_montazu = Pracownik_Montazu("Robert", "Kowalski", 3500, 4, 3, "Monter")
prac_montazu.pracownik.zmien_pensje(5000)
prac_IT = Pracownik_IT("Maciej", "Nowak", 4000, 5, 4, "programista")
prac_IT.pracownik.zmien_ocene_pracy(3)
prac_organizacji_pracy = Pracownik_Organizacji_Pracy(
    "Kuba", "Wójcicki", 6000, 3, 2, "mechanik"
)
prac_organizacji_pracy.pracownik.zmien_nazwisko("Musiał")

print(prac_montazu.pracownik.imie)
print(prac_montazu.pracownik.pensja)
prac_IT.pracownik.opis()
prac_organizacji_pracy.pracownik.opis()
