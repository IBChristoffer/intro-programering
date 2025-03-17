
max_tal = 100
primtal_markering = [True] * (max_tal + 1)
primtal_markering[0] = primtal_markering[1] = False


for i in range(2, int(max_tal**0.5) + 1):
    if primtal_markering[i]:
        for j in range(i * i, max_tal + 1, i):
            primtal_markering[j] = False


print(primtal_markering)