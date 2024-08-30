#Tehtävä 5

tunnus = "python"
salasana = "rules"
yritys = 1
max_yritys = 5

while yritys <= max_yritys:
    anna_tunnus = input("Kirjoita tunnus: ")
    anna_salasana = input("Kirjoita salasana: ")
    if anna_tunnus != tunnus or anna_salasana != salasana:
        print("Väärä tunnus tai salasana.")
        yritys += 1
    elif anna_tunnus == tunnus and anna_salasana == salasana:
        print("Tervetuloa!")
        break
    if yritys > max_yritys:
        print("Pääsy evätty.")