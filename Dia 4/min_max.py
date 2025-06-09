menor = min(58, 96, 72, 64, 35)
mayor = max(58, 96, 72, 64, 35)

print(menor)
print(mayor)


lista = [100, 45, 69, 12, 43, 1]
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')

nombres = ['juan', 'pablo', 'alicia', 'carlos']
print(max(nombres))

nombre = 'rodolfo' # -> primero revisa letras mayusculas y posteriormente las minusculas
print(min(nombre))

dic = {'c1':45, 'c2':11}# -> por default devuelve el minimo de las claves
print(min(dic.values()))

# EJERCICIOS

#Obten el valor maximo entre los valores de la siguiente lista, y almacenalo en una variable llamada valor_maximo.
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(valor_maximo)

#Calcula la diferencia entre el valor maximo y el minimo en la siguiente lista de numeros, y guardalo en una variable llamada rango.
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros) - min(lista_numeros)
print(rango)

#Utilizando max(), min() y metodos de diccionarios, obten el minimo valor a partir del siguiente diccionario, almacena dicho
#valor en una variable llamada edad_minima. Tambien obten el nombre que se ubica ultimo en orden alfabetico y guardalo en ultimo_nombre.
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades).lower()
print(ultimo_nombre)