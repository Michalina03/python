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
    return (a * b) / nwd(a, b)


print(nww(78, 66))
