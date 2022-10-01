z = input("Zadaj zaciatok intervalu:")
z = int(z)
k = input("Zadaj koniec intervalu:")
k = int(k)

if z > k:
    z, k = k, z
pocet = 0

for cislo in range(z, k+1):
    vysledok = cislo % 8
    if vysledok == 0:
        pocet = pocet + 1
    print(pocet)
print("Pocet cisel delitelnych 8 od", z, "do", k, "je:", pocet)
