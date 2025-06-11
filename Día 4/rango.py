#range(inicio, fin, saltos) solo enteros

for numero in range(20, 31, 2):
    print(numero)

#crear una lista con un rango del 1 al 100
lista = list(range(1,101))

print(lista)

#EJERCICIOS

#Crea una lista formada por todos los numeros desde el 2500 al 2585(inclusive).
#Almacena dicha lista en la variable mi_lista

mi_lista = list(range(2500, 2586))
print(mi_lista)

#Utilizando la funcion range(), crea en una unica linea de codigo una lista formada por todos los numeros multiplos de 3
# desde el 3 al 300(inclusive). Almacena dicha lista en la variable mi_lista

mi_lista2 = list(range(3,301,3))
print(mi_lista2)

#Utiliza la funcion range() y un loop para sumar los cuadrados de todos los numero del 1 al 15(inclusive). Almacena el resultado en una variable llamada
#suma_cuadrados, para ello: Crea un rango de valores que puedas recorrer en un loop. Para cada uno de estos valores,
#calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional)
#Suma todos los valores al cuadrado obtenidos. acumula la suma en la variable suma_cuadrados.

valores = list(range(1,16))
suma_cuadrados = 0

for valor in valores:
    suma_cuadrados += valor**2

print(suma_cuadrados)