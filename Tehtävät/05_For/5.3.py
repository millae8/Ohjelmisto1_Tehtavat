#Tehtävä 3

def is_prime_number(num):
    if num < 1:
        return False
    for i in range(2, num):
        #print(i)
        if num % i == 0:
            # jos jaollinen jollain i:n arvolla, palautetaan false
            # ja funktion suoritus loppuu siihen
            return False
    return True

# pääohjelma lukee syötteen ja tulostaa vastauksen
user_input = int(input("Anna testattava luku (>0): "))

if is_prime_number(user_input):
    print(f"Luku {user_input} on alkuluku.")
else:
    print(f"Luku {user_input} ei ole alkuluku.")