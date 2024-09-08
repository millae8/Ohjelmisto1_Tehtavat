#Tehtävä 1
import random

def noppa():
    return random.randint(1, 6)

tulos = noppa()

while tulos != 6:
    print(tulos)
    tulos = noppa()

print(f"Numero on {tulos}.")