# Random
from random import *

aleatorio = randint(1, 50) #genera valor aleatorio en base al rango definido
print(aleatorio)

aleatorio2 = round(uniform(1, 5), 1) #genera un valor flotante aleatorio
print(aleatorio2)

aleatorio3 = random() #genera un numero flotante aleatorio entre 0 y 1
print(aleatorio3)

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio4 = choice(colores) #devuelve un elemento aleatorio de la lista
print(aleatorio4)

numeros = list(range(5,51,5))
shuffle(numeros) # no devuelve una lista, modifica la lista original, mezclo los valores para dar una salida diferente a la original
print(numeros)

# EJERCICIOS

#Implementa la funcion randint() de la libreria random que te permita obtener un numero entero del 1 al 10 y almacenalo en aleatorio.

aleatorio5 = randint(1, 10)
print(aleatorio5)

#Implementa la funcion random() de la libreria random que te permita obtener un numero decimal entre 0 y 1 y almacenalo en aleatorio
aleatorio6 = random()
print(aleatorio6)

#Utiliza el metodo choice() de la libreria random para obtener un elemento al azar de la sig. lista de nombres y almacenalo en sorteo.
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(sorteo)