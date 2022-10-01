n = input("Zadaj N:")
n = int(n)
sucet = 0

for cislo in range(1, n+1):
    vysledok = cislo % 2
    if vysledok == 0:
        print("Parne cislo:", cislo)
        sucet = sucet + cislo
print("Sucet vsetkych parnych cisel je:", sucet)
