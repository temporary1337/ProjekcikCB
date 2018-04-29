f = open("C:\\Users\\Uczeń\\Downloads\\wyniki-lotto-sortowane.csv", 'r+')
moja_lista = f.readlines()
#moja_lista[0] = moja_lista[0].replace('\n','')
#print (moja_lista[0])
moja_lista.pop(0)
rozmiar_po_popnieciu = len(moja_lista)
n = 0
while n < rozmiar_po_popnieciu:
    moja_lista[n] = moja_lista[n].replace('\n','')
    moja_lista[n] = moja_lista[n].split(';')
    n += 1
print(moja_lista)
f.close()

#chce liste w ktorej kazdy element (1-6026) to slownik, ktorego nazwa jest numer wiersza w excelu

n = 0
#while n < rozmiar_po_popnieciu
#    slownik = {moja_lista[n][0]}

#print("\n", moja_lista[0][3])