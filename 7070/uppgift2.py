import random

print("Välkommen att kasta tärning")
print("Ett spel kostar 1 krona")
print("Vinstplan:")
print("två lika - 5 kr")
print("en sexa - 3 kr")
print("stege - 3 kr\n")

pengar = 0

while True:
    val = input("Välj spela (s), sätt in pengar (i), eller avsluta (a): ").lower()

    if val == 'i':
        belopp = int(input("Ange belopp att sätta in: "))
        pengar += belopp
        print(f"Att spela för: {pengar}\n")

    elif val == 's':
        if pengar < 1:
            print("Du har inte tillräckligt med pengar. Sätt in mer för att spela.\n")
            continue
        
        pengar -= 1
        tärning1 = random.randint(1, 6)
        tärning2 = random.randint(1, 6)
        print(f"Tärningarna visar: {tärning1} {tärning2}")

        if tärning1 == tärning2 and tärning1 == 6:
            print("Sex-vinst + 3kr\n")
            pengar += 3
        elif tärning1 == tärning2:
            print("Två lika - vinst + 5kr\n")
            pengar += 5
        elif abs(tärning1 - tärning2) == 1:
            print("Stege - vinst + 3kr\n")
            pengar += 3
        else:
            print("Förlust\n")

        print(f"Att spela för: {pengar}\n")

    elif val == 'a':
        print("Vad roligt att du spelade en stund!")
        break
    else:
        print("Ogiltigt val, försök igen.\n")

