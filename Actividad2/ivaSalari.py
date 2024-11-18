'''
    4. Aplicar IVA segons el salari
En aquest exercici, s’aplicarà un IVA (0, 10, 21) segons el salari que s’indiqui.
Crear una variable de nom salari. Si el salari és menor de 15.000, s’aplica un 0% d’IVA. 
Si el salari és menor de 30.000 s’aplica un 10% de l’iva. Si el salari és menor a 60.000 s’aplica un IVA del 21%.

Exemple càlcul si el salari son 5000 => 5.000 * 0/100
'''

salari = float(input("Introdueix el teu salari: "))

if salari < 15000:
    iva = 0
    salari_final = salari * (1 + iva / 100)
    print("IVA aplicat: 0%. El salari final és:", salari_final)
elif salari < 30000:
    iva = 10
    salari_final = salari * (1 + iva / 100)
    print("IVA aplicat: 10%. El salari final és:", salari_final)
elif salari < 60000:
    iva = 21
    salari_final = salari * (1 + iva / 100)
    print("IVA aplicat: 21%. El salari final és:", salari_final)
else:
    print("No és un salari vàlíd.")

