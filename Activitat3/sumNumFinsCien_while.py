'''
Sumar números fins a arribar a 100 amb while. Caldrà sumar els números que estan inclosos entre 0 i 100. 
El programa deixarà d’executar-se quan s’arribi al número 100.
'''

suma = 0
i = 0

while suma < 100:
    suma += i
    i += 1
print(f'La suma total de números fins arribar a 100 és: {suma}')

#la suma manual sería 1+2+3+4+5+6+7+8+9+10+11+12+13+14=105