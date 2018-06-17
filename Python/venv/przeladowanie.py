import giereczka

class klasa_liczby:
    def __init__(self, L1, L2):
        self.liczba1 = L1
        self.liczba2 = L2
    def __add__(self, Inna):
        suma = self.liczba1 + Inna.liczba1
        suma2 = self.liczba2 + Inna.liczba2
        return (suma, suma2)

class klasa_stringi:
    def __init__(self, S1, S2):
        self.string1 = S1
        self.string2 = S2
    def __add__(self, Other):
        a = self.string1 + Other.string1
        b = self.string2 + Other.string1
        c = ('odpad: ', Other.string2)
        return (a, b, c)

class klasa_mieszana:
    def __init__(self, L, S):
        self.liczba = L
        self.string = S
    def __add__(self, other):
        giereczka
        return

print('ble')

Liczby = klasa_liczby(5, 17)
Stringi = klasa_stringi('Kappa', 'Poggers')
Mieszana = klasa_mieszana(18, 'WutFace')

x = (Liczby + Liczby)
print(x)
print(Liczby)
print(Stringi + Stringi)
Mieszana + Mieszana