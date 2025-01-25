with open("xxx.txt", "w") as text_file:
    text = "Ala ma kota"
    text_file.write(text)


with open("xxx.txt", "r") as xxx:
    print(xxx)
    xxx_contents = xxx.readline()
    print(xxx_contents)

with open("xxx.txt", "a") as text_file:
    text = "\n" + "Nie, Ula ma kota"
    text_file.write(text)

# -------------------------------------

# Napisz funkcję generującą plik tekstowy zawierający liczby “od kiedy do kiedy co ile -range”


def genrate_text(file_name: str, content: str):
    file_name = file_name + ".txt"
    with open(file_name, "w") as text_file:
        text_file.write(content)


def numbers_range(n: int, m: int, k: int):
    text = ""
    for i in range(n, m, k):
        text += f" {i}"
    return text


text = numbers_range(-10, 100, 2)
genrate_text("numbers", text)


# Napisz funkcję generującą plik tekstowy zawierający liczby ciągu arytmetycznego..


def genrate_text(file_name: str, content: str):
    file_name = file_name + ".txt"
    with open(file_name, "w") as text_file:
        text_file.write(content)


def cig_arytmetyczny(p_el, dr_el, n):
    el = p_el
    co_ile = dr_el - p_el
    text = f"{p_el} "
    for _ in range(n):
        text += f"{el+co_ile} "
        el += co_ile
    return text


text = cig_arytmetyczny(5, 10, 20)
genrate_text("ary", text)


# Napisz funkcję generującą plik tekstowy zawierający liczby ciągu geometrycznego.


def genrate_text(file_name: str, content: str):
    file_name = file_name + ".txt"
    with open(file_name, "w") as text_file:
        text_file.write(content)


def cig_gem(p_el, dr_el, n):
    el = p_el
    co_ile = dr_el / p_el
    text = f"{p_el} "
    for _ in range(n):
        text += f"{el*co_ile} "
        el *= co_ile
    return text


text = cig_gem(3, 9, 10)
genrate_text("geom", text)


# Napisz funkcję generującą plik tekstowy zawierający liczby ciągu fibonacciego.


def genrate_text(file_name: str, content: str):
    file_name = file_name + ".txt"
    with open(file_name, "w") as text_file:
        text_file.write(content)


def fibonacci_sequence(n):
    el_1 = 1
    el_2 = 1
    nex_el = 0
    text = f"{el_1} {el_2}"
    for _ in range(n):
        nex_el = el_1 + el_2
        text += f" {nex_el}"
        el_1 = el_2
        el_2 = nex_el
    return text


text = fibonacci_sequence(10)
genrate_text("fibo", text)


# Napisz funkcję generującą pliki tekstowy zwierjacy tabliczke mnożenia 10 na x10.


def multiplication_tables(n):
    s = ""
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            s += f"{i*k}\t"
        s += "\n"
    return s


def genrate_text(file_name: str, content: str):
    file_name = file_name + ".txt"
    with open(file_name, "w") as text_file:
        text_file.write(content)


multiplication_data = multiplication_tables(10)


genrate_text("multiplication_tables", multiplication_data)


# ---- CZYTANIE PLIKÓW ----------- pamiętaj aby najpierw wygenerować plik,
# ten kod linijka po linijce przeczyta Ci tekst  wygenerowanego pliku tekstowego


def linijka_po_linijce(sciezka_do_pliku):
    try:
        with open(sciezka_do_pliku, "r") as plik:
            for linijka in plik:
                inf = linijka.strip()
                print(inf)
                inf = inf.split("-")
                print(inf)
    except FileNotFoundError:
        print("Ups! Nie mogę znaleźć pliku. Sprawdź ścieżkę.")


linijka_po_linijce("xxx.txt")

# ====== ZADANIE KARTKÓWKOWE ====================
# np. kto zarabia więcej, ile mężczyzn do kobiet proporcje, ile średnio zarabiają kobiety
# -- (ten kod chyba nie działa, aby wyciagną osoby z pliku lepiej użyć tego wyżej) --


def linijka_po_linijce(sciezka_do_pliku):
    k = 0
    zarobki = 0
    try:
        with open(sciezka_do_pliku, "r") as plik:
            for linijka in plik:
                inf = linijka.strip()
                inf = inf.split("-")
                if inf[4] == "Kobieta":
                    k += 1
                    zarobki += float(inf[3])

    except FileNotFoundError:
        print("Ups! Nie mogę znaleźć pliku. Sprawdź ścieżkę.")

    print(zarobki / k)


linijka_po_linijce("xxx.txt")


# -----------KOD GENERUJĄCY TABELKE MNOŻENIA ---------------------
def generate_multiplication_table(n):
    table = ""

    table += "   "
    for i in range(1, n + 1):
        table += f"{i:4}"
    table += "\n"

    for i in range(1, n + 1):
        table += f"{i:2}"
        for j in range(1, n + 1):
            result = i * j
            table += f"{result:4}"
        table += "\n"
    return table


table_size = 10

multiplication_table = generate_multiplication_table(table_size)

file_name = "tabliczka_mnozenia.txt"

try:
    with open(file_name, "w") as file:
        file.write(multiplication_table)
    print("Plik został pomyślnie wygenerowany.")
except Exception as e:
    print("Wystąpił błąd podczas generowania pliku:", str(e))


# =================== HOMWORK ========================
# ======= KWADRAT =======
def generate(ilosc):
    tekst = ""
    for i in range(ilosc):
        if i == 0 or i == ilosc - 1:
            tekst += "* " * ilosc + "\n"
        else:
            tekst += "* " + "  " * (ilosc - 2) + "*\n"
    return tekst


ilość_gwiazdek = 10

kwadrat = generate(ilość_gwiazdek)

file_name = "kwadrat.txt"

with open(file_name, "w") as file:
    file.write(kwadrat)

# ======= TRÓJKĄT PTOSTOKĄTNY ========


def generate2(ilosc):
    tekst = ""
    for i in range(1, ilosc + 1):
        tekst += "* " * i + "\n"
    return tekst


ilość_gwiazdek2 = 7

trojkat = generate2(ilość_gwiazdek2)

file_name = "trojkat.txt"

with open(file_name, "w") as file:
    file.write(trojkat)

# ======= TRÓJKĄT RÓWNORAMIENNY========


def generate3(ilosc):
    tekst = ""
    for i in range(ilosc):
        stars = 2 * i + 1
        spaces = ilosc - i - 1
        tekst += " " * spaces + "*" * stars + "\n"
    return tekst


ilość_gwiazdek3 = 4

trojkat2 = generate3(ilość_gwiazdek3)

file_name = "trojkat.txt"

with open(file_name, "w") as file:
    file.write(trojkat2)

# =======================================================
# Napisz skrypt co wygeneruje 20 liczb pierwszych w pliku tekstowym ppp.txt.
def generator_lp(n):
    lst = []
    liczba = 2
    while len(lst) < n:
        if all(liczba % i != 0 for i in range(2, int(liczba**0.5) + 1)):
            lst.append(liczba)
        liczba += 1
    return lst


lista = generator_lp(20)

with open("ppp.txt", "w") as file:
    file.write("\n".join(map(str, lista)))


# Napisz skrypt co wygeneruje 20 liczb ciągu fibonacciego w pliku tekstowym fff.txt
def generator_f(n):
    f = [0, 1]
    while len(f) < n:
        f.append(f[-1] + f[-2])
    return f


list = generator_f(20)

with open("fff.txt", "w") as file:
    file.write("\n".join(map(str, list)))


# 1 Napisz skrypt co przepisze liczby pierwsze do zzz.txt jeśli znajdują się one w obu plikach  ppp.txt / fff.txt
def read(filename):
    with open(filename, "r") as file:
        numbers = set(int(line.strip()) for line in file)
    return numbers


def write(numbers, filename):
    with open(filename, "w") as file:
        for number in sorted(numbers):
            file.write(f"{number}\n")


ppp_numbers = read("ppp.txt")
fff_numbers = read("fff.txt")

numbers = ppp_numbers.intersection(fff_numbers)

write(numbers, "zzz.txt")


# 1 Napisz skrypt co zmieni wszystkie z pliku zzz.txt na liczby binarne
def na_binary(input_file, output_file):
    with open(input_file, "r") as file:
        binary_numbers = [bin(int(line.strip()))[2:] for line in file]

    with open(output_file, "w") as file:
        file.write("\n".join(binary_numbers))


na_binary("zzz.txt", "zzz_bin.txt")


# 2Napisz skrypt co  przepisze  liczby z pliku fff.txt + rozłoży liczby na czynniki pierwsze i zapisze je z pliku ccc.txt.
def czynniki_pierwsze(n):
    factors = []
    d = 2  # dzielnik
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    return factors


def zapis_do_pliku(input_file, output_file):
    with open(input_file, "r") as file:
        numbers = [int(line.strip()) for line in file]

    result = []  # Lista do przechowywania krotek (liczba, czynniki_pierwsze)
    for number in numbers:
        factors = czynniki_pierwsze(number)  # Poprawiono wywołanie funkcji
        result.append((number, factors))

    with open(output_file, "w") as file:
        for number, factors in result:  # Poprawiono zmienną zapis_do_pliku na result
            file.write(f"{number} {' '.join(map(str, factors))}\n")


zapis_do_pliku("fff.txt", "ccc.txt")


# 2Napisz skrypt co powie ile występuje liczb pierwszych (wszystkie liczby pierwsze) w pliku zzz.txt.
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def count_prime_numbers(filename):
    with open(filename, "r") as file:
        return sum(1 for line in file if is_prime(int(line.split()[0])))


ccc_prime_count = count_prime_numbers("ccc.txt")
print(f"Liczba liczb pierwszych w pliku 'ccc.txt': {ccc_prime_count}")

#===========================================

def binarne_na_naturalne(liczba):
    liczba = list(liczba)
    int_num = []
    for index, value in enumerate(reversed(liczba)):
        if value == "1":
            int_num.append(2**index)
    return sum(int_num)


def naturalne_na_binarne(liczba):
    my_list_bin = []
    while liczba > 0:
        remainder = liczba % 2
        my_list_bin.append(remainder)
        liczba = liczba // 2
    my_list_bin.reverse()
    b = ""
    for el in my_list_bin:
        b += str(el)
    return b


from random import randint


def numbers(n):
    with open("numbers.txt", "w") as text_file:
        for i in range(n + 1):
            liczba = randint(1, 100000)
            if i == n:
                text_file.write(f"{liczba}")
            else:
                text_file.write(f"{liczba}-")


numbers(10000)


def zamiana_na_liste_pliku_textowego(sciezka_do_pliku):
    lst = []
    with open(sciezka_do_pliku, "r") as plik:
        for linijka in plik:
            inf = linijka.strip()
            inf = inf.split("-")
            for el in inf:
                lst.append(int(el))
    return lst


lst = zamiana_na_liste_pliku_textowego("numbers.txt")

# Tworzenie pliku my_bin z reprezentacją binarną liczb z pliku numbers.txt
with open("my_bin.txt", "w") as my_bin_file:
    for i, number in enumerate(lst):
        if i == len(lst) - 1:
            my_bin_file.write(naturalne_na_binarne(number))
        else:
            my_bin_file.write(f"{naturalne_na_binarne(number)}-")

# Tworzenie pliku my_int z liczbami całkowitymi z pliku my_bin.txt
with open("my_bin.txt", "r") as my_bin_file:
    with open("my_int.txt", "w") as my_int_file:
        for line in my_bin_file:
            numbers_str = line.strip().split("-")
            for i, num_str in enumerate(numbers_str):
                num_int = binarne_na_naturalne(num_str)
                my_int_file.write(f"{num_int}")
                if i != len(numbers_str) - 1:
                    my_int_file.write("-")