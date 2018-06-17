Lista_1 = [5,5,5,5,5,1,2,3,4,9]
Lista_2 = [1.11, 2.22, 3.14, 1.11, 0.3, 221.4, 124.2, 1.1]
Lista_3 = [['a', 'b', 'c'], [1,2,3,4,5], [1.17, 'zet', 117], 'lelement1', 'lelement2', 'lelement3', 'lelement4', 'lelement5']
Lista_4 = [7,8,9, ['a', 13, 14], 'blabla', 'z17', 8.99, 'lelement1', 'lelement2', 'lelement3', 'lelement4', 'lelement5']

print(Lista_1[0:10])
print(Lista_2[0:8])
print(Lista_3[0:8])
print(Lista_4[0:12])

Lista_1.sort()
Lista_2.sort()
print ('\n\n',Lista_1,'\n',Lista_2,'\n\n')

print(Lista_1[::-1])
print(Lista_2[::-1])
print(Lista_3[::-1])
print(Lista_4[::-1], '\n', '\n')

del Lista_1[::3]
del Lista_2[::3]
del Lista_3[::3]
del Lista_4[::3]

print(Lista_1[0:9])
print(Lista_2[0:7])
print(Lista_3[0:7])
print(Lista_4[0:11])