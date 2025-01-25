class Xxxx:
    zmienna_klasowa_1 = 0
    zmienna_klasowa_2 = 0
    ile = 0

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c
        Xxxx.zmienna_klasowa_2 += 1
        Xxxx.licznik()

    def zmien_a(self, a):
        self.a = a

    @classmethod
    def zmein_zmien_klasowa_1(cls, zmienna):
        cls.zmienna_klasowa_1 = zmienna

    @classmethod
    def licznik(cls):
        cls.ile += 1

    @classmethod
    def inf_zmienne_klasowe(cls):
        print(cls.zmienna_klasowa_1)
        print(cls.zmienna_klasowa_2)


x1 = Xxxx(1, 1, 1)
x2 = Xxxx(2, 2, 2)
x3 = Xxxx(3, 3, 3)
x3.inf_zmienne_klasowe()
Xxxx.inf_zmienne_klasowe()

# -------------------------------------------


class Ksiazka:
    def __init__(self, tytul: str = None, autor: str = None, liczba_stron: int = 0):
        self.tytul = tytul
        self.autor = autor
        self.liczba_stron = liczba_stron

    def informacje(self):
        print(f"Tytuł: {self.tytul}")
        print(f"Autor: {self.autor}")
        print(f"Liczba stron: {self.liczba_stron}")


class Biblioteka:
    liczba_ksiazek = 0
    lista_ksiazek = []

    @classmethod
    def informacje(cls):
        print(f"Liczba książek: {cls.liczba_ksiazek}")
        for ksiazka in cls.lista_ksiazek:
            ksiazka.informacje()
            print("---")

    @classmethod
    def dodaj_ksiazke(cls, tytul, autor, liczba_stron):
        k = Ksiazka(tytul, autor, liczba_stron)
        cls.lista_ksiazek.append(k)
        cls.liczba_ksiazek += 1


Biblioteka.dodaj_ksiazke("AAA", "AAAAAA", 100)
Biblioteka.dodaj_ksiazke("BBB", "BBBBBB", 200)
Biblioteka.informacje()

# -----------------------------------------------------------

# Zadanie 1: Licznik instancji klasy
# Polecenie: Stwórz klasę LicznikInstancji, która będzie śledzić, ile razy została zainicjalizowana. Użyj @classmethod do przechowywania i aktualizacji licznika każdej utworzonej instancji.


class LicznikInstancji:
    i = 0

    def __init__(self) -> None:
        LicznikInstancji.licznik()

    @classmethod
    def licznik(cls):
        cls.i += 1

    @classmethod
    def inf_licznik(cls):
        print(cls.i)


l1 = LicznikInstancji()
l2 = LicznikInstancji()
l3 = LicznikInstancji()
l1.inf_licznik()
l2.inf_licznik()
l3.inf_licznik()


# Zadanie 2: Alternatywny konstruktor dla użytkowników
# Polecenie: Utwórz klasę Uzytkownik z podstawowym konstruktorem przyjmującym imię i nazwisko.
# Dodaj @classmethod, który pozwoli na tworzenie instancji klasy na podstawie ciągu znaków z
# imieniem i nazwiskiem oddzielonymi spacją.


class Uzytkownik:
    liczba_stworzonych_uzytkownikow = 0

    def __init__(self, imie: str = "", nazwisko: str = "") -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        Uzytkownik.stworzny_urzytkownik()

    @classmethod
    def stworzny_urzytkownik(cls):
        cls.liczba_stworzonych_uzytkownikow += 1

    # Kiedy z_ciagu tworzy nową instancję klasy (poprzez return cls(imie, nazwisko)),
    # w rzeczywistości wywołuje konstruktor Uzytkownik.__init__ z przekazanymi argumentami imie i nazwisko.
    # Dlatego też nie wywołujemy Uzytkownik.stworzny_urzytkownik()
    @classmethod
    def alternatywn_konstruktor(cls, ciag: str = ""):
        imie, nazwisko = ciag.split(" ")
        return cls(imie, nazwisko)

    def inf(self):
        print(f"imie - {self.imie} nazwisko - {self.nazwisko}")
        print(Uzytkownik.liczba_stworzonych_uzytkownikow)


u1 = Uzytkownik("Ala", "Alowata")
u2 = Uzytkownik.alternatywn_konstruktor("Ala Alowata")
u1.inf()
u2.inf()


# -------------------------------------------------------------


class Math:

    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def subtraction(a, b):
        print(a - b)

    @staticmethod
    def multiplication(a, b):
        print(a * b)

    @staticmethod
    def division(a, b):
        print(a / b)


Math.add(5, 6)
Math.subtraction(10, 5)
Math.multiplication(2, 3)
Math.division(10, 2)


# =========================STATIC CLASS============================================


class PrzykladowaKlasa:
    @staticmethod
    def przykladowa_metoda_statyczna(arg1, arg2):
        # Tutaj może być dowolna logika niezależna od instancji klasy
        return arg1 + arg2


# Wywołanie statycznej metody na klasie
wynik = PrzykladowaKlasa.przykladowa_metoda_statyczna(5, 3)
print(wynik)  # Wynik: 8


# Wywołanie statycznej metody na instancji klasy również
# jest możliwe, ale niezalecane
instancja = PrzykladowaKlasa()
wynik_instancji = instancja.przykladowa_metoda_statyczna(10, 2)
print(wynik_instancji)  # Wynik: 12


class Kwadrat:
    liczba_stworzonych_obiektow = 0

    def __init__(self, a) -> None:
        self.a = a
        self.pp = Kwadrat.oblicz_pp(a)
        self.obw = Kwadrat.oblicz_obw(a)
        Kwadrat.licznik_obiektow()

    def inf(self):
        print(f"a - {self.a}")
        print(f"pp - {self.pp}")
        print(f"obw - {self.obw}")
        Kwadrat.ile_obiektow_powstalo()

    def zmien_a(self, a):
        self.a = a
        self.pp = Kwadrat.oblicz_pp(a)
        self.obw = Kwadrat.oblicz_obw(a)

    @classmethod
    def licznik_obiektow(cls):
        cls.liczba_stworzonych_obiektow += 1

    @classmethod
    def ile_obiektow_powstalo(cls):
        print(f"Powstało {cls.liczba_stworzonych_obiektow} obiektów.")

    @staticmethod
    def oblicz_pp(a):
        return a * a

    @staticmethod
    def oblicz_obw(a):
        return 4 * a


k1 = Kwadrat(10)
k2 = Kwadrat(10)
k3 = Kwadrat(10)
k4 = Kwadrat(10)
k4.inf()
