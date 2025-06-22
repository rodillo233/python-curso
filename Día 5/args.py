#Argumentos indefinidos en las funciones
def suma(*args):
    #total = 0
    #for arg in args:
        #total += arg
    #return total
    return sum(args)

print(suma(5,6,9,10,2,8))

# EJERCICIOS

#Crea una funcion llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numericos y que retorne la
#suma de sus valores al cuadrado.
#Por ejemplo para los argumentos suma_cuadrados(1,2,3) debera retornar 14. (1 + 4 + 9)

def suma_cuadrados(*args):
    total = 0
    for numero in args:
        total += numero**2
    return total

cuadrados = suma_cuadrados(5,9,7,6)
print(f'Suma cuadrados: {cuadrados}')

#Crea una funcion llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extension, y retorne la suma de
#sus valores absolutos es decir que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos
#negativos y positivos como positivos.

def suma_absolutos(*args):
    suma = 0
    for numero in args:
        if numero < 0:
            suma += numero * -1
        else:
            suma += numero
    return suma


total = suma_absolutos(5,9,-8,6,-3,1,7, -10)
print(f'Suma absolutos: {total}')

#Crea una funcion llamada numeros_persona que reciba, como primer argumento, un nombre, y acontinuacion una cantidad
# indefinida de numeros. La funcion debe devolver:
#"{nombre}, la suma de tus numeros es {suma_numeros}"

def numeros_persona(nombre, *args):
    suma_numeros = 0
    for numero in args:
        suma_numeros += numero
    return f'{nombre}, la suma de tus numeros es {suma_numeros}'

print(numeros_persona('Rodolfo', 4,6,9,8,2,3,47))