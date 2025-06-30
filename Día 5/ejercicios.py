#Ejercicio1
#Crea una funcion llamada devolver_distintos() que reciba 3 integers como parametros.
#Si la suma de los 3 numeros es mayor a 15, va a devolver el numero mayor
#Si la suma de los 3 numeros es menor a 10, va a devolver el numero menor
#Si la suma de los tres numeros es un valor entre 10 y 15 incluidos va a devolver el numero de valor intermedio
from itertools import count


def devolver_distintos(*args):
    suma_total = sum(args)
    if suma_total > 15:
        print(max(args))
    elif suma_total < 10:
        print(min(args))
    elif suma_total in range(10, 16):
        ordenada = sorted(list(args))
        print(ordenada[1])

devolver_distintos(1,4,3)

#Ejercicio2
#Escibe una funcion que reciba cualquier palabra como parametro, y que devuelva todas sus letras unicas, sin repetir pero en
#orden alfabetico. Por ejemplo si al invocar esta funcion pasamos la palabra "entretenido" debe devolver
# ['d','e','i','n','o','r','t']

def letras_unicas(palabra):
    return sorted(set(palabra))

resultado = letras_unicas('cascarrabias')
print(resultado)

#Ejercicio3
#Escribe una funcion que requiera una cantidad indefinida de argumentos. Lo que hara esta funcion es devolver True si en
#algun momento se ha ingrsado al numero cero repetido dos veces consecutivas. Por ejemplo:
#(5,6,1,0,0,9,3,5) -> True
#(6,0,5,1,0,3,0,1) -> False

def cero_consecutivo(*args):
    lista = []
    indice = 0

    for numero in args:
        lista.append(numero)

        if indice == 0:
            indice += 1
            continue

        if indice > 0:
            if lista[indice-1] == 0 and numero == 0:
                return True
            else:
                indice += 1

    return False

res = cero_consecutivo(8,9,4,3,0,4,7,0)
print(res)


#Solucion udemy
def ceros_vecinos(*args):
    contador = 0

    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador+1] == 0:
            return True
        else:
            contador += 1
    return False

#Ejercicio4
#Escribe una funcion llamada contar_primos() que requiera un solo argumento numerico. Esta funcion va a mostrar en pantalla
#todos los numeros primos existentes en el rango de cero hasta ese numero incluido, y va a devolver la cantidad de numeros
#primos que encontro. Por convencion el 0 y el 1 no se consideran primos.


def contar_primos(numero):
    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:

        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                iteracion += 2
                break

        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)

print(contar_primos(50))



