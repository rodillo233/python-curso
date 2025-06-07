
mi_lista = ['a', 'b', 'c']
otra_lista = ['hola', 55, 6.1]


resultado = len(mi_lista)
resultado1 = mi_lista[0]
resultado2 = mi_lista[0:2]
resultado3 = mi_lista + otra_lista

print(type(mi_lista)) #class list
print(resultado)
print(resultado1)
print(resultado2)
print(f'\n{resultado3}')

resultado3[0] = 'alpha' #modifica el indice 0 de la lista
print(resultado3)

resultado3.append('z') #agrega elemento al final de la lista
print(resultado3)

resultado3.pop() #elimina el ultimo elemento
print(resultado3)

eliminado = resultado3.pop(0) #elimina el indice 0 y lo almacena en la variable eliminado
print(resultado3)
print(eliminado)

#ordenar lista (el metodo sort no devuelve ningun valor, solo reordena en tiempo de ejecución)
lista = ['g', 'o', 'b', 'm', 'c']
lista2 = [5, 9, 1, 6, 10, 0, 8]
lista.sort()
lista2.sort()
print(lista)
print(lista2)

#invertir el orden de una lista
lista3 = ['z', 'y', 'x', 'w', 'v', 'u']
lista3.reverse()
print(lista3)

#EJERCICIOS

#Crea una lista con 5 elementos, dentro de la variable mi_lista, Puedes incluir strings, booleanos, numeros
mi_lista1 = ['hola', 2, False, 6.5, 'adios']

#Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
#medios_transporte = ["avión", "auto", "barco", "bicicleta"]
#No debes modificar la línea de código ya suministrada, sino que debes emplear el metodo apropiado de listas para
#añadir un nuevo elemento.

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append('motocicleta')

#Utiliza el metodo pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo
# en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(frutas)
print(eliminado)