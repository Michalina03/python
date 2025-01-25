import Fabryka_Czolgow


class Magazyn:
    def __init__(self, cena) -> None:
        self.magazyn = []
        self.na_sprzedarz = []
        self.cena = cena

    def doaj_czolg_do_magazynu(self):
        self.magazyn.append(Fabryka_Czolgow.Czolg(self.cena))

    def dodaj_czolg_na_sprzedarz(self):
        self.magazyn.append(Fabryka_Czolgow.Czolg(self.cena))

    def usun_czolg_z_magazynu(self, a):
        self.magazyn.remove(self.magazyn[a])

    def usun_czolg_sprzedarz(self, a):
        self.magazyn.remove(self.cena[a])

    def przenies_czolg_z_magazynu_na_sprzedarz(self, a):
        self.na_sprzedarz.append(self.magazyn[a])
        self.magazyn.remove(self.magazyn[a])

    def inf(self):
        print(self.cena)


o1 = Magazyn(123865039239067509)
