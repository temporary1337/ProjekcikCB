class Zwierze:
    def ilosc_nog(self):
        print("pienc nug")
        return 5

class Ssak(Zwierze):
    def ilosc_nogSsaka(self):
        super.ilosc_nog(self)
        return 4
#   liczba_nog = 1
#   pancerz = False
#   lubiany = False
#   grozny = False

#    def __init__(self, liczba_nog, grozny):
#       self.liczba_nog = 10
#       self.grozny = True

 #   def wyswietl(self):
 #       print("Nóg ma", self.liczba_nog)
 #       return 0

# slimak = Zwierze(10, False)
# slimak.wyswietl()
# slimak.liczba_nog = 7

