#En un set los elementos no se repiten, no se ordenan en indices, no admite listas ni diccionarios.
# set([1,2,3,4,5,6])
# {1,2,3,4,5,6}

mi_set = set([1,2,3,4,5,1,2,1,(10,20,30)]) #podemos agregar set ya que son inmutables, listas y diccionarios no
print(type(mi_set))
print(mi_set)

#print(mi_set[0]) -> no se indexan
#mi_set[2] = 20 -> son inmutables

otro_set = {1,2,3,4,5}
print(type(otro_set))
print(otro_set)
print(len(otro_set))
print(2 in otro_set)

#union de sets
s1 = {10,20,30}
s2 = {30,40,50}
s3 = s1.union(s2)
print(s3)

s1.add(100)
print(s1)

s1.remove(10)
print(s1)

s1.discard(1000)
print(s1) # similar a remove con la diferencia que si no encuentra el elemento no marca error

s1.pop() # elimina un elemento aleatorio
print(s1)

s1.clear() #limpia el set
print(s1)

# EJERCIOCIOS

#Une los siguientes sets en uno solo, llamado mi_set_3
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)

#Elimina un elemento al azar del siguiente set, utilizando metodos de sets
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
print(sorteo)

#Agrega el nombre Damian al siguiente set, utilizando metodos de set
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add('Damián')