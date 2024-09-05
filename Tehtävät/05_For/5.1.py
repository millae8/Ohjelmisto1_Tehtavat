#Tehtävä 1
import random

total = 0
dice_count = int(input("Kuinka monta noppaa heität? "))

for i in range(dice_count):
    total = total + random.randint(1, 6)
print(f"Noppien silmälukujen summa on {total}.")