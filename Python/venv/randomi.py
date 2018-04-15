import time
import random

random.seed(time.time())
lista = ['Bartek', 'Tomasz', 'Jacek', 'Jan', 'Milosz', 'Leonardo', 'Bruce', 'Jackie', 'Clint', 'Harrison']

#x = (random.randrange(20))

x = random.choice(lista)
print (x)
random.shuffle(lista)
x = random.sample(lista, 2)
print (x)
