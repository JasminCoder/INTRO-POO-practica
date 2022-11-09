#HERENCIA
from Persona import Persona

class Estudiante(Persona): #estamos diciendo q la clase a heredar es persona

    lista_estudiantes = []

    def __init__(self, nombre, apellido, email, edad, id):
        super().__init__(nombre, apellido, email, edad) #para no volver a escribir todos los atributos self. de la clase 
        #persona, llamamos a la clase superior, usando super().
        self.id = id #para agregar un nuevo atributo
        Estudiante.lista_estudiantes.append(self) #para la lista estudiantes

        #tb se heredan las funciones (linea 64) pedro codificar - pedro cumpleaños, etc



    #SOBREESCRITURA y POLIMORFiSMO
    #reemplazar (sobreescribir) funcion "imprime lista" de la clase persona
    @classmethod #funcion para la clase completa
    def imprime_lista(cls): 
        print("Total de estudiantes:" , len(cls.lista_estudiantes))
        for estudiante in cls.lista_estudiantes:
            print(estudiante.nombre) 


    #reemplaza funcion cumpleaños de clase persona
    def cumpleaños(self):
        self.edad += 2
        print("Sin festejo, a seguir estudiando!")


    #modifica funcion cumpleaños agregandole otra frase
    def cumpleaños(self):
        super().cumpleaños() #referencia a la funcion de mi superior
        print("A seguir estudiando ;)")




    #POLIMORFISMO?
    def que_haces(self):
        print("Estoy estudiando en Coding Dojo")



    #funcion solo para class estudiante
    def estudiar(self):
        print("Hoy estamos estudiando Python")