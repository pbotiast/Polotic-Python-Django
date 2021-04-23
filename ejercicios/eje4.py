lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for e in lista1:
    if e > 150:
        break
    elif e % 5 == 0:
        print(e, end=' ')