from Cotxe import Cotxe
from Colibri import Colibri

#3 instàncies de Cotxe

Mercedes = Cotxe("Mercedes", "Negro", "Gasolina","5", "2010")
Jaguar = Cotxe("Jaguar", "Verde metalizado", "Gasoil","3", "2000")
Tesla = Cotxe("Tesla", "Blanco", "Eléctrico","5", "2022")

#3 instàncies de Colibrí.

Colibri1 = Colibri("Verde/negro", "5", "Largo","20", "300")
Colibri2 = Colibri("Blanco", "15", "Corto","10", "500")
Colibri3 = Colibri("Negro/dorado", "12", "Largo","5", "100")

#Mostrar 3 getters de Cotxe

print(f'El model del cotxe és {Mercedes.getModelo()}, el color és { Mercedes.getColor()} y el anyo de fabricació és {Mercedes.getAnyo()}')

#Mostrar 4 getters de Colibrí 

print(f'El color del colibrí és {Colibri1.getColor()}, el tamany és { Colibri1.getTamanyo()} cm, el plumatje és {Colibri1.getPlumaje()} y el seu tipus de pic és {Colibri1.getTipo_pico()} cm de llarg')

#Modificar 2 atributs de Cotxe a través dels setters
#Mostrar els 2 atributs modificats a través dels getters
#Modificar 2 atributs de Colibrí a través dels setters
#Mostrar els 2 atributs modificats a través dels get
