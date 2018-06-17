import random
wynik = 0
koniec = 'a'

while koniec != '0':
    lista = ['PAPIER', 'KAMIEŃ', 'NOŻYCE']
    x = random.choice(lista)

    print('\nPAPIER - a, KAMIEŃ - b, czy NOŻYCE - c ???')
    y = input('wybierz mądrze\n')
    print('OPPONENT CHOSE <<', x, '>>')
    if x == 'PAPIER':
        x = 'a'
    if x == 'KAMIEŃ':
        x = 'b'
    if x == 'NOŻYCE':
        x = 'c'
    if y == x:
        print('REMIS')
    if y == 'a' and x == 'b':
        print('WYGRAŁEŚ!!!')
        wynik += 1
    if y == 'a' and x == 'c':
        print('PRZEGRAŁEŚ :C')
        wynik -= 1
    if y == 'b' and x == 'a':
        print('PRZEGRAŁEŚ :C')
        wynik -= 1
    if y == 'b' and x == 'c':
        print('WYGRAŁEŚ!!!')
        wynik += 1
    if y == 'c' and x == 'a':
        print('WYGRAŁEŚ!!!')
        wynik += 1
    if y == 'c' and x == 'b':
        print('PRZEGRAŁEŚ :C')
        wynik -= 1
    print('\nTWÓJ WYNIK TO:', wynik, 'By zakończyć, wpisz 0')
    koniec = input
