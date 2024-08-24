# 2. Muuttujat ja vuorovaikutteiset ohjelmat
import math
import random

#Tehtävä 1
name = input("Mikä on nimesi: ")
print("Moi " + name)

#Tehtävä 2
circle_str = input("Mikä on ympyrän säde: ")
circle = float(circle_str)
carea = (circle**2)*math.pi
print("Ympyrän pinta-ala on: " + str(carea))

#Tehtävä 3
rectanglew_str = input("Suorakulmion kanta: ")
rectangleh_str = input("Suorakulmion korkeus: ")
rw = float(rectanglew_str)
rh = float(rectangleh_str)
piiri = 2*rw + 2*rh
pa = rw * rh
print("Suorakulmion piiri on " + str(piiri) + " ja sen pinta-ala on: " + str(pa))

#Tehtävä 4
eka_str = input("Syötä ensimmäinen kokonaisluku: ")
toka_str = input("Syötä toinen kokonaisluku: ")
kolmas_str = input("Syötä kolmas kokonaisluku: ")
eka = int(eka_str)
toka = int(toka_str)
kolmas = int(kolmas_str)
summa = eka + toka + kolmas
tulo = eka * toka * kolmas
keskiarvo = summa / 3
print("Numeroiden summa on " + str(summa) + ", tulo on " + str(tulo) + " ja keskiarvo on " + str(keskiarvo))

#Tehtävä 5
loaves_str = input("Massa leivisköinä: ")
nails_str = input("Massa nauloina: ")
bullets_str = input("Massa luoteina: ")
loaves = float(loaves_str)
nails = float(nails_str)
bullets = float(bullets_str)
ltn = loaves * 20
nailoaves = nails + ltn
lona = nailoaves * 32
lonabu = bullets + lona
grams = lonabu * 13.3
kgrams = grams // 1000
grams = grams % 1000
print("Massa nykymittojen mukaan: \n" + str(kgrams) + " kilogrammaa ja " + str(grams) + " grammaa.")

#Tehtävä 6
codea = ""
for _ in range(3):
    x = str(random.randint(0, 9))
    codea = codea + x

codeb = ""
for _ in range(4):
    y = str(random.randint(1, 6))
    codeb = codeb + y

print("Ensimmäinen koodi: " + codea + "\nToinen koodi: " + codeb)

#Loppu