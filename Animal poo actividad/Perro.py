from Mascota import Mascota

class Perro(Mascota): #la clase a heredar es mascota

    def __init__(self, nombre, edad, especie, comida_favorita, juguete_favorito):
        super().__init__(nombre, edad, especie, comida_favorita)
        self.juguete_favorito = juguete_favorito

    def tengo_hambre(self):
        print("Humana quiero mi comida!")