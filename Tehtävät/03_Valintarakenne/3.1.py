#Tehtävä 1

kuha_pituus = float(input("Kuhan pituus senttimetreinä: "))
puuttuu = 37-kuha_pituus

if kuha_pituus<37:
    print(f"Kuha on {puuttuu}cm liian pieni. Laske kuha takaisin järveen.")
else:
    print("Kuha on tarpeeksi pitkä.")