mi_tupla = (1,2,3,4)
t = (5, 6.9, 'hola', {'name':'rodolfo'})

print(type(mi_tupla)) # class tuple
print(t[0])
print(t[-2])

#Las tuplas son inmutables
#mi_tupla[0] = 5
#print(mi_tupla)

tupla = (1,2,(10,20),3,4)
print(tupla[2][0]) # -> 10

#convertir a lista
tuple_to_list = list(tupla)
print(type(tuple_to_list))
#devolver la lista a tupla
list_to_tuple = tuple(tuple_to_list)
print(type(list_to_tuple))

#Almacenar los valores de una tupla en dicferentes variables

a = (1,2,3,4,5)
v,w,x,y,z = a
print(v)
print(w)
print(x)
print(y)
print(z)

#largo de una tupla
b = (1,2,3,1)
print(len(b))

#contar la cantidad de apariciones de un elemento en la tupla
print(b.count(1)) # -> 2

#devuelve el indice de un valor de una tupla
print(b.index(2))

# EJERCICIOS

#Utiliza un metodo de tuplas para contar la cantidads de veces que aparece el valor 2 en la siguiente
#tupla, y muestra el resultado en pantalla.
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))


#Convierte a lista la siguiente tupla, y almacenala en una variable llamada mi_lista
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)
print(mi_lista)


#Extrae los elemento de la siguiente tupla en cuatro variables.
mi_tupla = (1,2,3,4)
a,b,c,d = mi_tupla
print(a)
print(b)
print(c)
print(d)