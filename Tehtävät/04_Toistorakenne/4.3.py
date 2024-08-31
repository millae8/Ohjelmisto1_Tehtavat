#Tehtävä 3

numero = "a"
x = None
y = None
while numero!="":
    numero = input("Anna numero: ")
    print(numero)
    if numero != "":
        numero = int(numero)
        if x is None or numero > x:
            x = numero
        if  y is None or numero < y:
            y = numero
print(f"Ohjelma lopetettu. Pienin numero on {y} ja suurin numero on {x}.")