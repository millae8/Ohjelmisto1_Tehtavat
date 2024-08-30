#Tehtävä 4

vuosi = int(input("Anna vuosiluku: "))

if vuosi % 4 == 0 and vuosi % 100 != 0:
    print("On karkausvuosi.")
elif vuosi % 4 != 0:
    print ("Ei ole karkausvuosi.")

if vuosi % 100 == 0 and vuosi % 400 == 0:
    print("On karkausvuosi.")
elif vuosi % 100 == 0 and vuosi % 400 != 0:
    print("Ei ole karkausvuosi.")