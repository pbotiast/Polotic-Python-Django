from datetime import datetime as dt

now = dt.now()

print(f'Hora actual: {now.hour}:{now.minute}:{now.second}')

print(f'En dos horas: {now.hour + 2}:{now.minute}:{now.second}')