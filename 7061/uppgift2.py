svar = int(input("Ange ett tal ")) 
gissningar = 0

while gissningar < 5:
    if svar < 42:
        svar = int(input("För lågt, gissa igen! "))
        gissningar += 1
    elif svar > 42:
        svar = int(input("Talet är för högt, skriv ett annat "))
        gissningar += 1
    else:
        print("Rätt!")
        break





