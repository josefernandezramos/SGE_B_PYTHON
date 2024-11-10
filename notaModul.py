'''
    3. Nota Mòdul
En aquest exercici caldrà modificar la nota en número i mostrar-la en text. 
Es crearà una variable on es guardarà la nota numèrica i amb condicionals es 
mirarà la nota i segons la nota numèrica sortirà per pantalla la nota (S - suspès, A - aprovat, N - notable, E - excel·lent)

Exemple: nota = 6,25
Sortida: L’alumne ha aprovat.

Suspès => 0 a 4,99
Aprovat => 5 a 6,5
Notable => 6,6 a 8
Excel·lent => més de 8
'''
nota = ""

nota = float(input("Ingresa una nota: "))

if nota >= 0 and nota <= 4.99:
    print("L'alumne ha suspès.")
elif nota >= 5 and nota <= 6.5:
    print("L'alumne ha aprovat.")
elif nota >= 6.6 and nota <= 8:
    print("L'alumne ha obtingut un notable.")
elif nota >= 8:
    print("L'alumne ha obtingut un excelent.")
else:
    print("Nota no vàlida.") 