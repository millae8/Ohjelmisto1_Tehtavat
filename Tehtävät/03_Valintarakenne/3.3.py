#Tehtävä 3

gender = input("Onko biologinen sukupuolesi mies vai nainen? ")
hemoglobiini = int(input("Mikä on hemoglobiiniarvosi? "))

if gender == "nainen" and hemoglobiini<=116:
    print("Hemoglobiiniarvosi on alhainen.")
elif gender == "nainen" and 117<=hemoglobiini<=175:
    print("Hemoglobiiniarvosi on normaali.")
elif gender == "nainen" and hemoglobiini>=176:
    print("Hemoglobiiniarvosi on korkea.")

if gender == "mies" and hemoglobiini<=133:
    print("Hemoglobiiniarvosi on alhainen.")
elif gender == "mies" and 134<=hemoglobiini<=195:
    print("Hemoglobiiniarvosi on normaali.")
elif gender == "mies" and hemoglobiini>=196:
    print("Hemoglobiiniarvosi on korkea.")

else:
    print("Error.")