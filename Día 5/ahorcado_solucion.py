from random import choice

palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']

letras_correctas = []
letras_incorrectas = []

intentos = 6
aciertos = 0

juego_terminado = False

#Elige una palabra al azar de la lista de palabras
def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida)) # -> contiene cuantas letras distintas tiene la palabra y comparar con los aciertos
    return palabra_elegida, letras_unicas

#Pedir al usuario que ingrese una letra
def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input('Elige una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('No haz elegido una letra correcta')

    return letra_elegida

#Mostrar en pantalla el tablero, la palabra oculta en guiones, se muestra cada que el usuario elija letra
def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []

    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))

#Revisar si la letra que puso el usuario se encuentra o no, alimenta letras correctas e incorrectas
def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print('Ya has encontrado esa letra, intenta con otra diferente')
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias

def perder():
    print('Te has quedado sin vidas!')
    print(f'La palabra oculta era: {palabra}')
    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print(f'Felicitaciones, has encontrado la palabra!!')
    return True

palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')

    letra = pedir_letra()
    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)
    juego_terminado = terminado


