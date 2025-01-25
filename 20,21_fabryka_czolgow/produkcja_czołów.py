class Dzialo:
    def __init__(self,kaliber) -> None:
        self.kaliber = kaliber
    
    def zmien(self, nowy_kaliber):
        self.kaliber = nowy_kaliber

    def inf(self):
        print(self.kaliber)

class Silnik:
    def __init__(self,moc) -> None:
        self.moc = moc
    
    def zmien(self,nowy_silnik):
        self.moc = nowy_silnik

    def inf(self):
        print(self.moc)

class Zawieszenie:
    def __init__(self,wysokosc_zawieszenia) -> None:
        self.wysokosc_zawieszenia = wysokosc_zawieszenia
    
    def zmien(self, nowe_zawieszenie):
        self.wysokosc_zawieszenia = nowe_zawieszenie

    def inf(self):
        print(self.wysokosc_zawieszenia)

class Wieza:
    def __init__(self,predkosc_obrotu) -> None:
        self.predkosc_obrotu = predkosc_obrotu
    
    def zmien(self,nowa_predkosc):
        self.nowa_predkosc = nowa_predkosc

    def inf(self):
        print(self.wieza)

class Pancerz:
    def __init__(self,grubosc) -> None:
        self.grubosc = grubosc
    
    def zmien(self,nowa_grubosc):
        self.nowa_grubosc = nowa_grubosc

    def inf(self):
        print(self.pancerz)

class Czolg():
    ilosc = 0
    def __init__(self,cena):
        self.dzialo = Dzialo(1)
        self.silnik = Silnik(1)
        self.zawieszenie = Zawieszenie(1)
        self.wieza = Wieza(1)
        self.pancerz = Pancerz(1)
        self.cena = cena
        Czolg.ilosc += 1
        self.numer_seryjny = Czolg.ilosc

    def inf(self):
        self.dzialo.inf()
        self.silnik.inf()
        self.zawieszenie.inf()
        self.wieza.inf()
        self.pancerz.inf()
        print(self.cena)
        print(self.numer_seryjny)
    
    def zmien_dzialo(self,a):
        self.dzialo.zmien(a)

    def zmien_silnik(self,a):
        self.silnik.zmien(a)

    def zmien_zawieszenie(self,a):
        self.zawieszenie.zmien(a)

    def zmien_wieza(self,a):
        self.wieza.zmien(a)

    def zmien_pancerz(self,a):
        self.pancerz.zmien(a)

    def zmien_cena(self,a):
        self.cena=a

    def zmien_wszystko(self,a,b,c,d,e,f):
        self.dzialo.zmien(a)
        self.silnik.zmien(b)
        self.zawieszenie.zmien(c)
        self.wieza.zmien(d)
        self.pancerz.zmien(e)
        self.cena=f