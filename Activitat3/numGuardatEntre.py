'''
Amb while indicar si el número guardat a una variable està entre 100 i 400
'''

num = int(input("Introdueix un número: "))

while num < 100 or num > 400:
    print(f'El número {num} no està entre 100 i 400.')
    num = int(input("Introdueix un altre número: "))

print(f'El número {num} està entre 100 i 400.')