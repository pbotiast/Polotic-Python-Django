class Rectangulo():
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def area(self):
        return self.longitud * self.ancho

rect = Rectangulo(2, 4)
print(f'Longitud {rect.longitud} y Ancho {rect.ancho}')
print(f'Area: {rect.area()}')