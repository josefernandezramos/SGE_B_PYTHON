'''
Imprimir els números parells i els imparells continguts en la següent llista. 
Utilitzar for: num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
'''

num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

#nums parells
print("Números parells:")
for n in num:
    if n % 2 == 0:
        print(f'{n}')
    

#nums imparells
print("Números imparells:")
for n in num:
    if n % 2 != 0:
        print(f'{n}')
