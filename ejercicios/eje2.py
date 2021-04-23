class Vehiculo():
    def __init__(self, asientos = 6):
        self.asientos = asientos

class Minibus(Vehiculo):
    def __init__(self):
        super().__init__(self)
        self.ocupados = []

    def capacidad(self, new_asientos):
        self.asientos = new_asientos

    def pasajeros(self, pasajero):
        if self.disponibilidad():
            if pasajero in self.ocupados:
                print(f'{pasajero} ya esta dentro!')
            else:
                self.ocupados.append(pasajero)
        else:
            print('Se llegó al tope de la capacidad!')
    
    def disponibilidad(self):
        asientos = self.asientos - len(self.ocupados)
        print(f'Hay {asientos} asientos disponibles')
        return asientos

class Pasajero():
    def __init__(self, nombre):
        self.nombre = nombre


auto = Vehiculo()
print(auto.asientos)

bus = Minibus()
bus.capacidad(3) # En realidad es 50, pero es muucho para probar
print(bus.asientos)

while bus.disponibilidad() != 0:
    nombre = input('Como se llama el pasajero?: ')
    pasajero = Pasajero(nombre)
    bus.pasajeros(pasajero.nombre)
    print(bus.ocupados)

print('Se llego al tope de la capacidad, nos vimos! 👋')