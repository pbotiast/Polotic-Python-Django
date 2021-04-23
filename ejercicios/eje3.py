# Un plus seria que valide que sea entero

numbers = []

while len(numbers) < 5:
    n = int(input('Ingrese numero entero: '))
    numbers.append(n)

for number in numbers:
    print(number, end=' ')