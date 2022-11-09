class Mascota:

    def __init__(self, tipo, nombre, raza, color, edad):
        self.tipo = tipo
        self.nombre = nombre
        self.raza = raza
        self.color = color
        self.edad = edad

    def cumple(self):
        self.edad += 1
        print("Tu mascota tiene 1 año más")
