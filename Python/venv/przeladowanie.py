class klasa_liczby:
    def __init__(self, L1, L2):
        self.liczba1 = L1
        self.liczba2 = L2
    def __add__(self, Inna):
        suma = self.liczba1 + Inna.liczba1
        suma2 = self.liczba2 + Inna.liczba2
        return klasa_liczby(suma, suma2)

class klasa_stringi:
    def __init__(self, S1, S2):
        self.string1 = S1
        self.string2 = S2
    def __add__(self, Other):
        a = self.string1 + Other.string1
        b = self.string2 + Other.string1
        c = ('odpad: ', Other.string2)
        return klasa_stringi(a, c)

class klasa_mieszana:
    def __init__(self, L, S):
        self.liczba = L
        self.string = S
    def __add__(self, other):
        return

print('ble')

Liczby = klasa_liczby(5, 17)
Stringi = klasa_stringi('Kappa', 'Poggers')
Mieszana = klasa_mieszana(18, 'WutFace')

x = (Stringi + Stringi)
print(x.string1)
print(x.string2)