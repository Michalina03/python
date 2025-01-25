class Klient:
    def __init__(
        self, ilość_kupionych: int = None, rodzaj_klienta: str = None, kwota: int = None
    ) -> None:
        self.ilość_kupionych = ilość_kupionych
        self.rodzaj_klienta = rodzaj_klienta
        self.kwota = kwota

    def kupione(self):
        self.ilość_kupionych = int(input())

    def klient(self):
        self.rodzaj_klienta = input()

    def zakup(self):
        self.kwota = int(input())

    def informacje(self):
        print(f"Ilość kupionych czołgów: {self.ilosc_kupionych}")
        print(f"Klient: {self.rodzaj_klienta}")
        print(f"Wartość zakupu: {self.kwota}")


class Klienci:
    lista_klientow = []
    liczba_klientow = 0

    @classmethod
    def informacje(cls):
        print(f"Liczba klientow: {cls.liczba_klientow}")
        for klient in cls.lista_klientow:
            klient.informacje()
            print("---")

    @classmethod
    def stwórz_klienta(cls, rodzaj_klienta, ilość_kupionych, kwota):
        cls.liczba_klientow += 1
        cls.lista_klientow.append(Klient(ilość_kupionych, rodzaj_klienta, kwota))


Klienci.stwórz_klienta("państwowy", 100, 1000000)
Klienci.stwórz_klienta("prywatny", 20, 200000)
Klienci.informacje()
