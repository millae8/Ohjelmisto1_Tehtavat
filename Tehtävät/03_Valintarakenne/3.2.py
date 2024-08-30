#Tehtävä 2

user_input = input("Valitse hyttiluokka LUX, A, B tai C: ")
if user_input == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif user_input == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif user_input == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
elif user_input == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
else:
    print("Virheellinen hyttiluokka.")