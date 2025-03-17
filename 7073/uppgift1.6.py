tal = int(input("Gissa ett tal: "))

gissningar = 1

while tal != 42:
    gissningar = gissningar + 1
    if tal > 42:
        tal = int(input("för stort, gissa igen! "))
    else:
        tal = int(input("för litet, gissa igen! "))

print("Grattis, du vann, du gisssade på", gissningar, "gissningar")