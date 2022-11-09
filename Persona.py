#PROGRAMACION ORIENTADA A OBJETOS (POO)
from Curso import Curso #para poder usar aca la clase curso

class Persona: #persona es el objeto (en singular)

    #atributo para todas las personas de la clase
    pais = "Chile"
    lista_Personas = [] #lista de todas las instancias de persona
    total_lineas_codigo = 0 #total lineas codigo de todos


    def __init__(self, nombre, apellido, email, edad): #INIT: inicializando nuestra instancia (objeto persona). 2 guiones bajos
    #SELF: incluye toda la info sobre el objeto
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad
        self.lineas_codigo = 0
        Persona.lista_Personas.append(self)
        self.curso = Curso("Bootcamp Python") #se le esta poniendo un nombre(valor) x defecto, x eso no se agrega "curso" 
        #en la linea 12.. Si todos tuvieran un curso dif o especifico, ahi se agregaria en la 12 un "nombre curso" en vez 
        #de "Bootcamp Python" y ej en main, despues de la edad "Bootcamp js"


    
    def cumpleaños(self):
        self.edad += 1
        print("Muchas felicidades!")
        if Persona.mayor_edad(self.edad): #staticmethod
            print("Wujuu, eres mayor de edad") 

    
    def codificar(self, cantidad_lineas):
        #self = elena, cantidad_lineas = 45
        self.lineas_codigo += cantidad_lineas #1 persona
        Persona.total_lineas_codigo += cantidad_lineas #toda la clase
        if Persona.experto(self.lineas_codigo):
            print("Eres toda una experta codificando", self.nombre)



    @classmethod #funcion para la clase completa
    def imprime_lista(cls): #CLS = persona (se pone cls en vez de self, ya q es para toda la clase, no individual)
        print("Total de personas:" , len(cls.lista_Personas))
        for personita in cls.lista_Personas:
            print(personita.nombre)


    @staticmethod #no corresponde a la instancia ni a la clase/solo recibe un n° y devuelve verdadero o falso y 
    #este staticmethod lo usamos para cumpleaños y tomar cerveza/ en main se define la persona/si quisiera hacerlo 
    #para todas las instancias, hay q hcerlo 1 x 1
    def mayor_edad(edad):
        if edad >= 18:
            return True
        else:
            return False

    #staticmethod como q se usa para verificar

    @staticmethod #no le importa quien, solo toma el n° y realiza la funcion
    def experto(lineas): #recibo un n°
        if lineas > 100: #si es mayor a 100, entonces es experto
            return True
        else:
            return False #si no, no es experto
    #para usarlo en codificar



    #funcion normal para una persona (instancia especifica)
    def tomar_cerveza(self): #self = juana
        if Persona.mayor_edad(self.edad): #18
            print("Aqui está tu cerveza", self.nombre)
        else:
            print("Lo siento no puedes tomar cerveza")



    #POLIMORFISMO
    def que_haces(self):
        raise NotImplementedError #Cuando a la persona le pregunten que_haces no va a decir NADA (obliga a q en
        #estudiantes exista "que_haces" y si no existe q mande un error). Si esto no se pone, la funcion estudiante igual 
        #funciona