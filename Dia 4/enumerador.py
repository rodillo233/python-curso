#enumerate nos sirve para acceder a los indices de una lista

lista = ['a', 'b', 'c']

for item in enumerate(lista): # -> devuelve una tupla
    print(item)

print('\n')

for index, item in enumerate(lista):
    print(index, item)

print('\n')

for indice, item in enumerate(range(1,11)):
    print(indice, item)

#convertir a tupla con indice una lista de string
mi_tupla = list(enumerate(lista))
print(mi_tupla)
print(mi_tupla[0][1])

# EJERCICIOS

#Imprime en pantalla frases como la siguiente: '{nombre} se encuentra en el indice {indice}'. Donde nombre debe ser cada
#uno de los nombres de la lista a continuacion, y el indice, obtenido mediante enumerate().

lista_nombres = list(enumerate(["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]))
for indice, nombre in lista_nombres:
    print(f'{nombre} se encuentra en el índice {indice}')

#Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices
#de cada caracter del string 'Python'. Llama a la lista obtenida con el nombre de variable lista_indices.

lista_indices = list(enumerate('Python'))
print(lista_indices)

#Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M.

lista_nombres = list(enumerate(["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]))
for index, name in lista_nombres:
    if name.startswith('M'):
        print(index)