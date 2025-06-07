monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1
else:
    print('No tengo mas monedas..')

#################

respuesta = 's'
while respuesta == 's':
    respuesta = input('Deseas continuar? (s/n): ')
    print('Seguimos..')
else:
    print('Gracias!')

#################
#pass
respuesta1 = 's'

#while respuesta1 == 's':
    #pass #-> no hace nada, simplemente continua con la ejecucion aun siendo un ciclo while
#print('Hola')

#break
nombre = input('Ingresa tu nombre: ')
for letra in nombre:
    if letra == 'o':
        #break #interrumpe el ciclo cuando se cumple la condicion
        continue #vuelve al inicio de la iteracion del ciclo
    print(letra)

#EJERCICIOS

#Crea un loop while que se imprima en pantalla los numeros del 10 al 0, uno a la vez
numero = 10

while numero >= 0:
    print(numero)
    numero -= 1

#Crea un loop while que reste de uno en uno los numeros desde el 50 al 0 (ambos numeros incluidos) con las sig. condiciones:
#Si el numero es divisible por 5, mostrar dicho numero en pantalla
#Si el numero no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla

numero2 = 50

while numero2 >= 1:
    if numero2 % 5 == 0:
        print(numero2)
    numero2 -= 1