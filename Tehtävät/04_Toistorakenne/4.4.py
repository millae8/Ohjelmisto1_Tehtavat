#Tehtävä 4
import random

vastaus = random.randint(1, 10)

arvaus = int(input("Arvaa numero: "))
while arvaus != vastaus:
    if arvaus > vastaus:
        print("Liian suuri arvaus.")
        arvaus = int(input("Arvaa numero: "))
    elif arvaus < vastaus:
        print("Liian pieni arvaus.")
        arvaus = int(input("Arvaa numero: "))
if arvaus == vastaus:
    print("Oikein!")