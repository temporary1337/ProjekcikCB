import threading
import time

bramka = True
while bramka == True:
    try:
        z = input('Podaj wartosc Z do obliczen\n')
        z = int(z)
        temp = 1/z
    except ValueError:
        print('Program przyjmuje tylko wartosci liczbowe, sprobuj ponownie')
    except ZeroDivisionError:
        print('Podana wartosc musi byc rozna od zera')
    else:
        bramka = False

def dodawanie(x, y):
    wynik = x + y
    print('Suma', x, 'i', y, 'wynosi', wynik)

def dzielenie_czasu(x, y):
    wynik = round(x / y)
    print('Zaokraglony iloraz', x, 'i', y, 'wynosi', wynik)

def trzy_minutowy_mlyn():
    czas = 0
    a = 0
    b = 0
    while czas != 180:
        time.sleep(1)
        czas += 1
        a += 1
        print('Mieli ziarno (', czas, '/ 180 )')
        while a < 10:
            print('\U0001F35A' * a)
            print('\U0001F4B0' * b)
            if a == 9:
                b += 1
                a -= 10
            break

    print('Zmielil')

t1 = threading.Thread(target=dodawanie, args=(5, 10))
t2 = threading.Thread(target=dzielenie_czasu, args=(round((time.time())/1000), z))
t3 = threading.Thread(target=trzy_minutowy_mlyn)

t1.start()
t2.start()
t3.start()