count = 0

while count < 5: # Tambien se puede usar un for aca
    number = float(input('Ingrese numero decimal: '))
    while number % 1 == 0:
        number = float(input('No es decimal! Ingrese numero decimal: '))
    count += 1