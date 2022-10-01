n = input("Zadaj N:")
n = int(n)
pocet = 0

for cislo in range(1, n+1):
    vysledok1 = cislo % 7
    vysledok2 = cislo % 4
    if vysledok1 == 0 and vysledok2 == 0:
        pocet = pocet + 1
    print(pocet)
print("Pocet vsetkych cisel je:", pocet)
