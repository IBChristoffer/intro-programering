

import random
spela = str(input("Vill du spela?"))
tärning1 = (random.randint(1, 6))
tärning2 = (random.randint(1, 6))


while spela == "":
    
    print("Vad roligt att du spelade en stund!")

    if tärning1 == 6 and tärning2 == 6:
        print(tärning1, tärning2, "sex-vinst!")
    
    elif tärning1 == tärning2:
        print(tärning1, tärning2, "vinst")

    elif abs(tärning1 - tärning2) == 1:
        print(tärning1, tärning2, "steg-vinst!")

    else:
        print(tärning1, tärning2, "förlust")
    spela = str(input("Vill du spela?"))
    tärning1 = (random.randint(1, 6))
    tärning2 = (random.randint(1, 6))
        
print("tack förspelet!")




"""
import random
spela = str(input("Vill du spela?"))
tärning1 = (random.randint(1, 6))
tärning2 = (random.randint(1, 6))


while spela == "ja":
    
    print("Vad roligt att du spelade en stund!")


    
    if tärning1 == tärning2:
        print(tärning1, tärning2, "vinst")
        spela = str(input("Vill du spela?"))
        tärning1 = (random.randint(1, 6))
        tärning2 = (random.randint(1, 6))
    else:
        print(tärning1, tärning2, "förlust")
        spela = str(input("Vill du spela?"))
        tärning1 = (random.randint(1, 6))
        tärning2 = (random.randint(1, 6))
        
print("tack förspelet!")

"""