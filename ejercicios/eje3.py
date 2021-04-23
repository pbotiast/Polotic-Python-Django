# Hay dos formas, la que describo en el codigo y la otra usando es len y count (opcionalmente, tambien lower)

word = input('Ingrese algo: ')
cont_w = 0
cont_a = 0

for w in word:
    cont_w += 1
    if w in ['a', 'A']:
        cont_a += 1

print (f'En la entrada "{word}", hay {cont_w} caracteres y {cont_a} "a" y/o "A"')