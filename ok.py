import uuid
import json

SYSTEM_MEMBER = []
class Employee:
    def __init__(self, name, position):
        self.id = str(uuid.uuid4())
        self.name = name
        self.position = position
        self.add_employe()

    def add_employe(self):
        SYSTEM_MEMBER.append({
            'id':self.id,
            'name' : self.name,
            'position' : self.position

        })

    def inf(self):
        print(self.id)
        print(self.name)
        print(self.position)

class ManageEmploye:
    @staticmethod
    def data_json(data):
        return Employee(
            name = data['name'],
            position = data['position']
        )
    
    @staticmethod
    def file_json(file_path):
        with open(file_path, 'r') as file_json:
            data = json.load(file_json)
            employees =[]
            for item in data:
                empolyee = ManageEmploye.data_json(item)
                employees.append(empolyee)
        return employees
    

emp1 = Employee("marek", "koko")
emp2 = Employee("ffdfmarek", "kssssoko")
emp3 = Employee("macccrek", "ccckoko")

with open ('raport.json' , 'w') as raport:
    json.dump(SYSTEM_MEMBER,raport , indent=4)

empolyess = ManageEmploye.file_json('raport.json')

for obj in empolyess:
    print(20*"-")
    obj.inf()



#======================================================

import math


def nwd(a, b):
    lst = [a, b]
    wieksza = max(lst)
    mniejsza = min(lst)
    reszta = 1
    while reszta != 0:
        reszta = wieksza % mniejsza
        wieksza = mniejsza
        mniejsza = reszta
    return wieksza

print(nwd(78, 66))


def nww(a, b):
    return int((a * b) / nwd(a, b))

print(nww(78, 66))


liczby = [nww(78, 66), nwd(78, 66)]


def czy_to_liczba_pierwsza(liczba):
    if liczba <= 1:
        return False
    if liczba == 2:
        return True  # 2 jest liczbą pierwszą
    if liczba % 2 == 0:
        return False  # odrzuć parzyste liczby
    i = 3
    while math.sqrt(liczba) >= i:
        if liczba % i == 0:
            return False
        i += 2
    return True

for liczba in liczby:
    print(f"Czy {liczba} jest liczbą pierwszą? {czy_to_liczba_pierwsza(liczba)}")

#======================================================

uczen = {
    'imie': 'Adrian',
    'nazwisko': 'Poniatowski',
    'wiek':26,
    'matematyka':[1,1,2,3,4,5],
    'angielski':[2,3,4,5,6,1],
    'polski':[5,3,2,10]
}
# ---------------------------------------------------------
def inf(dc):
    for k,v in dc.items():
        print(f"{k}:  {v}")


def srednie(dc):
    srednia_m = sum(dc['matematyka'])/len(dc['matematyka'])
    print(f"Matematyka srednia {srednia_m}")
    srednia_m = sum(dc['angielski'])/len(dc['angielski'])
    print(f"Angielski srednia {srednia_m}")
    srednia_m = sum(dc['polski'])/len(dc['polski'])
    print(f"Polski srednia {srednia_m}")


# ----------------------------------------------------------
def edycja(dc):
    print("wprowadz klucz jaki chcesz edytować")
    print("==="*25)
    inf(dc)
    print("==="*25)
    inp = input()
    dc[inp] = input("Podaj nowe dane")


def edycja_listy(lst):
    while True:
        print(lst)
        print('a - dodaj element')
        print('u - usun element')
        print('e - wyjdz z edycji list')
        inp = input()
        if 'a' == inp:
            ocena = float(input())
            lst.append(ocena)
            print('ocena dodana')
        elif 'u' == inp:
            ocena = float(input())
            lst.remove(ocena)
            print('ocena usunieta')
        elif 'e' == inp:
            break
        else:
            print("Nie ma takiej komendy")


def dodaj_nowe_oceny(dc):
    print("Edytuj oceny")
    print("Matematyka - a")
    print("Angielski - b")
    print("Polski - c")
    inp = input()
    if inp == 'a':
        edycja_listy(dc['matematyka'])
    elif inp == 'b':
        edycja_listy(dc['angielski'])
    elif inp == 'c':
        edycja_listy(dc['polski'])
    print("dodaj_nowe_oceny - zakonczylo dzialnie")
   
# ----------------------------------------------------------
while True:
    print("==="*25)
    print("e - wyjdź z programu")
    print("i - informacje o uczniu")
    print("s - średnia ocen")
    print("ed - edytuj dane")
    print("oc - edytuj oceny")
    print("==="*25)
    inp = input().lower()
    if 'e' == inp:
        break
    elif 's' == inp:
        srednie(uczen)
    elif 'i' == inp:
        inf(uczen)
    elif 'ed' == inp:
        edycja(uczen)
    elif 'oc' == inp:
        dodaj_nowe_oceny(uczen)
    else:
        print("Program zkonczyl dziłanie")
        break


#==============================================

def genrate_text(file_name:str,content:str):
   file_name = file_name + ".txt"
   with open(file_name, "w") as text_file:
       text_file.write(content)


def cig_arytmetyczny(p_el,dr_el,n):
    el = p_el
    co_ile = dr_el - p_el
    text = f"{p_el} "
    for _ in range(n):
        text += f"{el+co_ile} "
        el += co_ile
    return text


text = cig_arytmetyczny(5,10,20)
genrate_text("ary", text) 



#===========================================

inp = input()
k_ile = 0
for el in inp:
    if el == 'k':
        k_ile += 1
print(f"W tym zdaniu jest {k_ile}k")
