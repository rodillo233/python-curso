def chequear_3_cifras(lista):
    lista_3_cifras = []
    for numero in lista:
        if numero in range(100, 1000):
            lista_3_cifras.append(numero)
        else:
            pass
    return lista_3_cifras

lista = [99, 593, 482, 23, 54]
resultado = chequear_3_cifras(lista)
print(resultado)

#EJERCICIOS

#Crea una función todos_positivos que reciba una lista de números como parámetro y devuelva True si todos los valores de la
#lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores
#positivos y negativos.

def todos_positivos(lista):
    for n in lista:
        if n < 0:
            return False
        else:
            pass
    return True

lista_numeros = [5, 8000, 15, 4253, 9, 23]

res = todos_positivos(lista_numeros)
print(res)

#Crea una función suma_menores que sume los números de una lista almacenada en la variable lista_numeros, siempre y cuando
#sean mayores a 0 y menores a 1000 y devuelva el resultado de dicha suma

def suma_menores(lista):
    nueva_lista = []
    for numero in lista:
        if 0 < numero < 1000:
            nueva_lista.append(numero)
        else:
            pass
    return sum(nueva_lista)

respuesta = suma_menores(lista_numeros)
print(respuesta)

#Crea una función cantidad_pares que cuente la cantidad de números pares que existen en una lista lista_numeros, y
#devuelva el resultado de dicha cuenta

def cantidad_pares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
        else:
            pass
    return contador

lista_numeros = [5, 8, 7, 10, 24, 19, 48, 200, 115, 128]

resp = cantidad_pares(lista_numeros)
print(resp)