class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Jestem {self.imie}, mam {self.wiek} lat."


class Uczen(Osoba):
    def __init__(self, imie, wiek, klasa):
        super().__init__(imie, wiek)
        self.klasa = klasa

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" Uczę się w klasie {self.klasa}."


class Nauczyciel(Osoba):
    def __init__(self, imie, wiek, przedmiot):
        super().__init__(imie, wiek)
        self.przedmiot = przedmiot

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" Uczę przedmiotu {self.przedmiot}."


# -------------------------------------------------------


class Dzwieki:

    @staticmethod
    def wfo():
        print("Wfo !!! Woff!!!")

    @staticmethod
    def miaw():
        print("Miał !!")


class Kot(Dzwieki):
    def __init__(self, _imie, wiek) -> None:
        self.imie = _imie
        self.wiek = wiek


kicia = Kot("Ala", 22)
kicia.wfo()

# ---------------------------------------------------------


class Pojazd:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def opis(self):
        return f"Pojazd marki {self.marka}, model {self.model}."


class Samochod(Pojazd):
    def __init__(self, marka, model, rok_produkcji):
        super().__init__(marka, model)
        self.rok_produkcji = rok_produkcji

    def opis(self):
        bazowy_opis = super().opis()
        return f"{bazowy_opis} Rok produkcji: {self.rok_produkcji}."


a = Samochod("Toyota", "Corolla", 2020)
print(a.opis())

# ---------------------------------------------------


class Pojazd:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def opis(self):
        print(f"Pojazd marki {self.marka}, model {self.model}.")


class Samochod(Pojazd):
    def __init__(self, marka, model, rok_produkcji):
        super().__init__(marka, model)
        self.rok_produkcji = rok_produkcji

    def opis(self):
        # Całkowite nadpisanie metody
        print(f"Sam {self.marka} {self.model}, rok pr: {self.rok_produkcji}.")
