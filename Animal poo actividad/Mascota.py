#EJERCICIO HERENCIA CON ANULACION DE FUNCION (Mascota -> perro) misma funcion, diferente print (anulacion)
class Mascota:

    def __init__(self, nombre, edad, especie, comida_favorita):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.comida_favorita = comida_favorita

    def tengo_hambre(self):
        print("Tengo hambre, alimentame!")