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
print ("Mostrar 3 getters de Cotxe")
print(f'El model del cotxe és {Mercedes.getModelo()}, el color és { Mercedes.getColor()} y el anyo de fabricació és {Mercedes.getAnyo()}')
print("")

#Mostrar 4 getters de Colibrí 
print("Mostrar 4 getters de Colibrí")
print(f'El color del colibrí és {Colibri1.getColor()}, el tamany és { Colibri1.getTamanyo()} cm, el plumatje és {Colibri1.getPlumaje()} y el seu tipus de pic és {Colibri1.getTipo_pico()} cm de llarg')
print("")

#Modificar 2 atributs de Cotxe a través dels setters
print("Modificar 2 atributs de Cotxe a través dels setters")
print("Modifiquem el color i el any de fabricació")
print("Abans:")
print(f'El model del cotxe és {Mercedes.getModelo()}, el color és { Mercedes.getColor()} y el anyo de fabricació és {Mercedes.getAnyo()}')
Mercedes.setColor("Verde")
#print(Mercedes.getColor())
Mercedes.setAnyo("2012")
#print(Mercedes.getAnyo())
print("Despres:")
print(f'El model del cotxe és {Mercedes.getModelo()}, el color és { Mercedes.getColor()} y el anyo de fabricació és {Mercedes.getAnyo()}')
print("")

#Mostrar els 2 atributs modificats a través dels getters
print("Mostrar els 2 atributs modificats a través dels getters")
Mercedes.setColor("Verde")
print(f"Este es el nuevo atributo de color: {Mercedes.getColor()}, modificado en Cotxe a través del getters")
Mercedes.setAnyo("2012")
print(f"Este es el nuevo atributo de anyo: {Mercedes.getAnyo()}, modificat en Cotxe a través del getters")
print("")

#Modificar 2 atributs de Colibrí a través dels setters
print("Modificar 2 atributs de Colibrí a través dels setters")
print("Modifiquem el plumaje i el tipo de pico del Colibrí")
print("Abans:")
print(f'El color del colibrí és {Colibri1.getColor()}, el tamany és { Colibri1.getTamanyo()} cm, el plumatje és {Colibri1.getPlumaje()} y el seu tipus de pic és {Colibri1.getTipo_pico()} cm de llarg')
print("Despres:")
Colibri1.setPlumaje("Rojo/Dorado")
Colibri1.setTipo_pico("30")
print(f'El color del colibrí és {Colibri1.getColor()}, el tamany és { Colibri1.getTamanyo()} cm, el plumatje és {Colibri1.getPlumaje()} y el seu tipus de pic és {Colibri1.getTipo_pico()} cm de llarg')
print("")

#Mostrar els 2 atributs modificats a través dels getters
print("Mostrar els 2 atributs modificats a través dels getters")
Colibri1.setPlumaje("Rojo/Dorado")
print(f"Este es el nuevo atributo de plumaje: {Colibri1.getPlumaje()}, modificado en Colibrí a través del getters")
Colibri1.setTipo_pico("30")
print(f"Este es el nuevo atributo de tipo de pico: {Colibri1.getTipo_pico()}, modificado en Colibrí a través del getters")