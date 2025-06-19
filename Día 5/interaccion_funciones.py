from random import *
#lista inicial
palitos = ['-', '--', '---', '----']

#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un numero del 1 al 4: ')

    return int(intento)

#comprobar intento
def chequear_intento(lista, intento):
    if lista[intento-1] == '-':
        print('Te toca lavar los trastes!')
    else:
        print('Te salvaste!')

    print(f'Te ha tocado {lista[intento-1]}')

#palitos_mezclados = mezclar(palitos)
#seleccion = probar_suerte()
#chequear_intento(palitos_mezclados, seleccion)

# EJERCICIOS

#Crea una funcion lanzar dados que arroje dos dados al azar y devuelva sus resultados:

#La funcion debe retornar dos valores resultado que se encuentren entre 1 y 6.
#Dicha funcion no debe requerir argumentos para funcionar, si no que debe generar internamente los valores aleatorios.

#Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función
#debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

#Si la suma es menor o igual a 6:
#"La suma de tus dados es {suma_dados}. Lamentable"

#Si la suma es mayor a 6 y menor a 10:
#"La suma de tus dados es {suma_dados}. Tienes buenas chances"

#Si la suma es mayor o igual a 10:
#"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

#Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.

def lanzar_dado():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return (dado1, dado2)

def evaluar_jugada(resultado_dado1, resultado_dado2):
    suma_dados = resultado_dado1 + resultado_dado2
    if suma_dados <= 6:
        return f'La suma de tus dados es {suma_dados}. Lamentable'
    elif 6 < suma_dados < 10:
        return f'La suma de tus dados es {suma_dados}. Tienes buenas chances'
    elif suma_dados >= 10:
        return f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora'

dado1, dado2 = lanzar_dado()
print(f'Dado1: {dado1}, Dado2: {dado2}')

mensaje = evaluar_jugada(dado1, dado2)
print(mensaje)


#Crea una funcion llamada reducir_lista() que tome una lista como argumento, crea tambien la variable lista_numeros
#y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los numeros si hay repetidos) y eliminando
#el valor mas alto. El orden de los elementos puede modificarse.

#Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

#Crea una funcion llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior funcion, y que
#calcule el promedio de los valores de la misma. debe devolver el resultado sin imprimirlo.

lista_numeros = [5,8,9,5,10,13,8,20,45,13,15]

def reducir_lista(lista):
    lista_sin_duplicados = set(lista)
    lista_sin_duplicados.remove(max(lista_sin_duplicados))
    return list(lista_sin_duplicados)

def promedio(lista):
    prom = sum(lista) / len(lista)
    return prom

lista = reducir_lista(lista_numeros)
print(lista)
resultado =  promedio((lista))
print(resultado)

#Crea una funcion llamada lanzar_moneda que devuelva el resultado de lanzar una moneda al azar. Dicha funcion debe poder devolver
#los resultados 'cara' o 'cruz' y no debe recibir argumentos para funcionar.

def lanzar_moneda():
    cara_cruz = ['Cara', 'Cruz']
    return choice(cara_cruz)

def probar_suerte(resultado, lista):
    if resultado == 'Cara':
        print('La lista se autodestruira')
        lista.clear()
        return lista
    else:
        print('La lista fue salvada')
        return lista

volado = lanzar_moneda()
lista_devuelta = probar_suerte(volado, lista_numeros)
print(lista_devuelta)