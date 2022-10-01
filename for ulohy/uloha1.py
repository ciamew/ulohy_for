n = input("Zadaj N:")
n = int(n)

for cislo in range(1, n+1):
    vysledok = cislo % 3
    if vysledok == 0:
        print("Cislo delitelne 3:", cislo)
