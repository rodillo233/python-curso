palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

lista2 = [letra for letra in 'python']
print(lista2)

lista3 = [numero for numero in range(0,21,2)]
print(lista3)

lista4 = [numero / 2 for numero in range(0,21,2)]
print(lista4)

lista5 = [numero for numero in range(0,21,2) if numero * 2 > 10 ]
print(lista5)

lista6 = [numero if numero * 2 > 10 else 'no' for numero in range(0,41,2)]
print(lista6)

pies = [10,20,30,40,50]
metros = [round(n / 3.281, 2) for n in pies]
print(metros)

# EJERCICIOS

#Crea una lista valores_cuadrado formada por los numeros de la lista valores, elevados al cuadrado.
valores = [1,2,3,4,5,6,9.5]
valores_cuadrado = [v ** 2 for v in valores]
print(valores_cuadrado)

#Crea una lista valores_pares formada por los numeros de la lista valores que sean pares.
valores = [1,2,3,4,5,6,9.5]
valores_pares = [numero for numero in valores if numero % 2 == 0]
print(valores_pares)

#Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores
#de temperatura en grados Celsius. La conversion entre tipo de unidades es la sig. °C = (°F-32) * (5/9).
#almacenala en grados_celsius

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(f-32) * (5/9) for f in temperatura_fahrenheit]
print(grados_celsius)