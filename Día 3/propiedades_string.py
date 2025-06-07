#Propiedades de los strings
#inmutables -> puedo cambiar el contenido de una variable, mas no modificar el caracter de un string
#concatenable
#multiplicable
#multilineales
#verificar si contiene
#calcular longitud

nombre = 'Jackeline'
#nombre[3] = 'q'
print(nombre)

n1 = 'Eliz'
n2 = 'abeth'
print(n1 + n2)
print(n1*10)

poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(poema)

print("agua" in poema)
print("agua" not in poema)

print(len(poema))

#EJERCICIOS

#Concatena 15 veces el texto 'Repetición' y muestra el resultado en pantalla. Por suerte, conoces que los strings
# son multiplicables y puedes realizar esta actividad de forma simple y elegante

print('Repetición' * 15)

#Verifica si la palabra 'agua' no se encuentra en el siguiente haiku. Debes imprimir el booleano.
#Tierra mojada,
#mis recuerdos de viaje
#entre las lluvias
haiku = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""

print("agua" not in haiku)

#Muestra en pantalla el largo (en numero de caracteres) de la palabra electroencefalografista
print(len('electroencefalografista'))