n = input("Zadaj N:")
n = int(n)
pocet = 0

for cislo in range(1, n+1):
    vysledok = cislo % 2
    if vysledok == 0:
        pocet = pocet + 1
    print(pocet)
print("Pocet parnych cisel od 1 do", n, "je:", pocet)
