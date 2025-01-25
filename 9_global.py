# def xxx():
#     x = 10
# print(x)


# Czemu nie mamy dostępu do x?


x = 10


def xxx():
    print(x)


xxx()


# A teraz paczajcie mamy dostęp do x…


x = 10


def xxx():
    x = 999999
    print(x)


print(x)
xxx()


# To jak to jest z tym x ?


MANA = 10


def zaklęcie():
    MANA = MANA - 10


zaklęcie()


# Nie działa


MANA = 10


def zaklęcie():
    global MANA
    MANA = MANA - 10


zaklęcie()
