import random
index=0
tärning = []


while index < 10:
    tärning.append(random.randint(1,6))
    index=index+1

tärning.sort()

print(tärning)

print("summa:", sum(tärning))

print("medelvärde:", sum(tärning)/len(tärning))

print("störst:", max(tärning))

print("minst:", min(tärning))

antal6=0

for antal6or in tärning:
    if antal6or == 1:
        antal6=antal6+1

print("antal6or:", antal6)


most_freq = max(set(tärning) ,key = tärning.count)

print("vanligast valör:", most_freq)