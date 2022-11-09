from Persona import Persona #importar lo q esta en el archivo persona para poder usarlo acá
from Estudiante import Estudiante

#instancia de persona
elena = Persona("Elena", "De Troya", "elena@codingdojo.com", 30)
juana = Persona("Juana", "De Arco", "juana@codingdojo.com", 17)

print(elena.nombre)
print(juana.nombre)

elena.cumpleaños() #no es necesario enviar el self (poner cumpleaños dentro de parentesis) pq ya se esta poniendo el nombre de quien quieres 
#q cumpla años y le sume 1 (elena.cumpleaños)

print(elena.edad)
print(juana.edad)


print(elena.lineas_codigo)
print(juana.lineas_codigo)

elena.codificar(45)
print(elena.lineas_codigo)
elena.codificar(10)
print(elena.lineas_codigo)
print(juana.lineas_codigo)


print(elena.pais)
print(juana.pais)


Persona.pais = "Mexico" #modificar pais de todos
print(elena.pais)


Persona.imprime_lista()

pablo = Persona("Pablo", "Picasso", "pablo@", 40)

Persona.imprime_lista()

juana.cumpleaños()

print(juana.edad)

juana.tomar_cerveza()

pablo.codificar(101)


elena.curso.agrega_calificacion(9)
elena.curso.agrega_calificacion(7)

print(elena.curso.calificaciones)




pedro =  Estudiante("Pedro", "Paramo", "pedro@dojo.com", 30, 1234)

print(pedro.email)
print(pedro.id)

pedro.codificar(100)

print(pedro.lineas_codigo)

pedro.cumpleaños()

Persona.imprime_lista()

print(Estudiante.lista_estudiantes)

Estudiante.imprime_lista()

pedro.que_haces()

pedro.estudiar()








print("-------------")
#importar
from Mascota import Mascota

#instancia mascota
perro = Mascota("perro", "Pupy", "pequines", "cafe", 2)
gato = Mascota("gato", "Fifi", "Persa", "gris", 1)

print(perro.nombre)
print(gato.raza)


perro.cumple()
print(perro.edad)














