#Tehtävä 2

luku = input("Anna numero: ")
luvut = []

while luku != "":
    luku = int(luku)
    luvut.append(luku)
    luku = input("Anna numero: ")

luvut.sort(reverse = True)
print(luvut[0:6])