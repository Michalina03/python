class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        return print(f"Jestem {self.imie}{self.nazwisko} i  mam {self.wiek} lat.")


# Tworznie pracownika========================================================


class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, umowa_o_prace):
        super().__init__(imie, nazwisko, wiek)
        self.umowa_o_prace = umowa_o_prace

    def przedstaw_sie(self):
        return super().przedstaw_sie() + print(
            f" Jestem pracownikiem, posiadam umowe {self.umowa_o_prace}."
        )


class SP(Pracownik):
    def __init__(self, imie, nazwisko, wiek, umowa_o_prace, sprzątam):
        super().__init__(imie, nazwisko, wiek, umowa_o_prace)
        self.sprzątam = sprzątam

    def przedstaw_sie(self):
        return super().przedstaw_sie() + print(
            f" Jestem sprzątaczką, sprzątam {self.sprzątam}."
        )


class Menager(Pracownik):
    def __init__(self, imie, nazwisko, wiek, umowa_o_prace, zarządzam):
        super().__init__(imie, nazwisko, wiek, umowa_o_prace)
        self.zarządzam = zarządzam

    def przedstaw_sie(self):
        return super().przedstaw_sie() + print(
            f" Jestem menagerem, zarządzam {self.zarządzam}."
        )


class IT(Pracownik):
    def __init__(self, imie, nazwisko, wiek, umowa_o_prace, dostep):
        super().__init__(imie, nazwisko, wiek, umowa_o_prace)
        self.dostep = dostep

    def przedstaw_sie(self):
        return super().przedstaw_sie() + print(
            f" Jestem pracownikiem IT, mam dostęp do {self.dostep}."
        )


# ==========================================================================


class Admin(IT):
    def __init__(self, imie, nazwisko, wiek, umowa_o_prace, dostep, serwer):
        super().__init__(imie, nazwisko, wiek, umowa_o_prace, dostep)
        self.serwer = serwer

    def przedstaw_sie(self):
        return super().przedstaw_sie() + print(f" Zarządzam serwerem {self.serwer}.")


o1 = Admin("mkm", "nsdn", "snduns", "sds", "sdsds", "sdss")
o1.przedstaw_sie()


class Developer(IT):
    def __init__(self, imie, nazwisko, wiek, umowa_o_prace, dostep, jezyk):
        super().__init__(imie, nazwisko, wiek, umowa_o_prace, dostep)
        self.jezyk = jezyk

    def przedstaw_sie(self):
        return super().przedstaw_sie() + print(f" programoje w jezyku {self.jezyk}.")


o2 = Developer("Kazik", "Oslo", "snduns", "sds", "sdsds", "sdss")
o2.przedstaw_sie()


class Hardwer(IT):
    def __init__(self, imie, nazwisko, wiek, umowa_o_prace, dostep, naprawiam):
        super().__init__(imie, nazwisko, wiek, umowa_o_prace, dostep)
        self.nprawiam = naprawiam

    def przedstaw_sie(self):
        return super().przedstaw_sie() + print(f" naprawiam {self.nprawiam}.")


o3 = Hardwer("Bartek", "Janik", 29, "umowa o zlecenie", "komputerów", "komputery")
o3.przedstaw_sie()
# ==========================================================================


class BiznesPartner(Osoba):
    def __init__(self, imie, nazwisko, wiek, firma):
        super().__init__(imie, nazwisko, wiek)
        self.firma = firma

    def przedstaw_sie(self):
        return super().przedstaw_sie() + print(
            f" Jestem partnerem biznesowym tej firmy, moja firma to {self.firma}."
        )


o4 = BiznesPartner("Marta", "Kostniak", 35, "Kluski i komputer")
o4.przedstaw_sie()


class Klient(Osoba):
    def __init__(self, imie, nazwisko, wiek, usluga):
        super().__init__(imie, nazwisko, wiek)
        self.usluga = usluga

    def przedstaw_sie(self):
        return super().przedstaw_sie() + print(
            f" Jestem klientem, kupiłam/em {self.usluga}."
        )


o5 = Klient("Ania", "Nowak", 23, "strona internetowa")
o5.przedstaw_sie()
