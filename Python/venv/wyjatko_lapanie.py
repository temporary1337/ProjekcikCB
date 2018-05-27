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