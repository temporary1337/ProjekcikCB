Karn = {'nazwa' : 'Karn, Scion of Urza', 'koszt' : '(4)', 'typ' : 'Planeswalker', 'CMC' : 4}
Mox = {'nazwa' : 'Mox Amber', 'koszt' : '(0)' , 'typ' : 'Artifact', 'CMC' : 0}
Mapa = {'nazwa' : 'Treasure Map', 'koszt' : '(2)', 'typ' : 'Artifact', 'CMC' : 2}
Head = {'nazwa' : 'Orzaca Relic', 'koszt' : '(3)', 'typ' : 'Artifact', 'CMC' : 3}
Lannery = {'nazwa' : 'Captain Lannery Storm', 'koszt' : '(2)R', 'typ' : 'Creature', 'CMC' : 3}

print (Karn['typ'])

Deck = {1 : Karn, 2 : Mox, 3 : Mapa, 4 : Head, 5 : Lannery}

print (Deck[1])
print (Karn)
print ('blabla\n')
print (Deck.keys())
x = 1
print ('Podaj jeden z filtrów kart: nazwa, koszt, typ lub CMC')
wybrana = input ('to wybierz\n')
while x < 6:
    y = Deck[x]
    print (y[wybrana])
    x += 1