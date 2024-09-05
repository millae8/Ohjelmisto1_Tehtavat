#Tehtävä 4

kaupungit = []
i = 0

for i in range(5):
    kaupunki = input("Anna kaupungin nimi: ")
    kaupungit.append(kaupunki)
for n in kaupungit:
    print(f"{n}!")