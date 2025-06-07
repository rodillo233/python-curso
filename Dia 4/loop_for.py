letras = ['a', 'b', 'c', 'd', 'e']

for letra in letras:
    indice = letras.index(letra) + 1
    print(f'Letra {indice}: {letra}')

print('\n')
#########################

nombres = ['Rodolfo', 'Samantha', 'Sarah', 'Cristhian', 'Regina']

for nombre in nombres:
    if nombre.lower().startswith('s'):
        print(nombre)
    else:
        print(f'El nombre {nombre}, no comienza con s')

print('\n')
#########################

numeros = [1,2,3,4,5]
mi_numero = 0

for numero in numeros:
    mi_numero = mi_numero + numero

print(mi_numero)

print('\n')
#########################

for letra in 'Python':
    print(letra)

for objeto in [[1,2], [3,4], [5,6]]:
    print(objeto)

for a,b in [[1,2], [3,4], [5,6]]:
    print(a, b)

dic = {
    'clave1': 'a',
    'clave2': 'b',
    'clave3': 'c'
}

for a,b in dic.items(): #keys(), values()
    print(a,b)

print('\n')

#EJERCICIOS

#Utilizando loops for, saluda a todos los miembros de una clase, imprimiendo "Hola" + su_nombre
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for alumno in alumnos_clase:
    print(f'Hola {alumno}')

print('\n')

#Dada la siguiente lista de numeros, realiza la suma de todos los numeros utilizando loop for y almacena el resultado
#de la suma en una variable llamada suma_numeros

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros += numero

print(suma_numeros)
print('\n')

#Dada la siguiente lista de numeros, realiza la suma de todos los numeros pares e impares por separado en las variables
#suma_pares y suma_impares respectivamente
lista_numeros2 = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros2:
    if numero % 2 == 0:
        suma_pares += numero

    else:
        suma_impares += numero

print(suma_pares)
print(suma_impares)
