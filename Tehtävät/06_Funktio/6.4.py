#Tehtävä 4

lista = []

def summa(lista):
    sum = 0
    for each in lista:
        sum = sum + each
    return sum

numero = input("Anna numero: ")
while numero != "":
    numero = int(numero)
    lista.append(numero)
    numero = input("Anna numero: ")
summa(lista)
print(summa(lista))