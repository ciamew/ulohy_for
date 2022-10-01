n = input("Zadaj N:")
n = int(n)
sucet = 0

for cislo in range(1, n+1):
     sucet = sucet + cislo
print("Sucet cisel od 1 do", n, "je:", sucet)