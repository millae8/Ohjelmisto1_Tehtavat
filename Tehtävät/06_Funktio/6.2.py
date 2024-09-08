#Tehtävä 2
import random

tahko = int(input("Anna nopan tahkojen määrä: "))

def noppa(tahko):
    return random.randint(1, tahko)
# print(noppa(tahko))

tulos = noppa(tahko)

while tulos != tahko:
    print(tulos)
    tulos = noppa(tahko)

print(f"Numero on {tulos}.")