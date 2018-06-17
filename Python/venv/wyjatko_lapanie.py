b = input('dej liczbe\n')
try:
    b = int(b)
    a = 100/b
except Exception:
    print("Nie dziel przez 0 i nie pisz glupot!")
else:
    print("Dobra liczba :ok_hand:!")

b = {'1':'bka', '2':'13', '3':3}
print(b)
try:
    b = int(input("podaj dowolna cyfre, oprocz ZAKAZANEJ\n"))
    c = 5 - b
    c = c/c
except ZeroDivisionError:
    print('TYLKO NIE PIATKA!!!\n')
else:
    print(b,'\n')

#try:
#   b = int(input('Podaj dowolna cyfre, oprocz ZAKAZANEJ(znowu)'))

''' 1.Plik do odczytu
    -otworzyc do zapisu
    
    2.Tablica 10 elementow
    -odwolac sie do 12 indeksu
    
    3.Zaimportowac nieistniejacy modul'''

#1.
try:
    file = open("C:\\Users\\Uczeń\\Desktop\\lorem_ipsum.txt", 'r+')
    file.write("Zakazany tekst")
except PermissionError:
    print("Nie przeczytasz zakazanego...")
#2.
zakazana_tablica = [0] * 10
print(zakazana_tablica[11])

#3.
import zakazany_modul

#4.
print(zakazana_zmienna)