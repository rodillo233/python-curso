from random import choice

lista_palabras = ['manzana', 'helado', 'carpinteria', 'escuela', 'mochila', 'escalera', 'serpiente', 'princesa', 'trabajo', 'escuelinista', 'stitch', 'matematicas']

def escoger_palabra(lista):
    return choice(lista)

def pedir_letra():
    letra = input('Introduce una letra: ')
    while(len(letra) != 1 or not letra.isalpha()):
        letra = input('Introduce una letra válida (solo una): ')
    return letra

def buscar_letra(letra, palabra):
    return palabra.count(letra)

def buscar_indices(letra_seleccionada):
    lista_indices = []
    index = 0

    for letra in palabra:
        if letra_seleccionada == letra:
            lista_indices.append(index)

        index += 1

    return lista_indices

def mostrar_letras(indices, palabra_escondida, letra):
    lista_escondida = list(palabra_escondida)
    for indice in indices:
        lista_escondida[indice] = letra

    lista_escondida = ''.join(lista_escondida)
    return lista_escondida


print("########   Bienvenido al Juego del Ahorcado   ########\n")
palabra = escoger_palabra(lista_palabras)
palabra_oculta = palabra.replace(palabra, '_' * len(palabra))
print(palabra_oculta)
letras_erroneas = []
vidas = 6

while vidas > 0:
    letra = pedir_letra()
    letras_encontradas = buscar_letra(letra, palabra)

    if letras_encontradas > 0:
        indices = buscar_indices(letra)
        palabra_oculta = mostrar_letras(indices, palabra_oculta, letra)
        print(palabra_oculta)

        if palabra_oculta == palabra:
            print('Ganaste!')
            break

    else:
        vidas -= 1
        if vidas == 0:
            print(f'Te quedan {vidas} vidas, Perdiste!')
            print(f'La palabra escondida era: {palabra}')
            break
        else:
            print(f'Fallaste, te quedan {vidas} vidas.\n')
            letras_erroneas.append(letra)
            print(f'Letras erroneas: {letras_erroneas}')
            print(palabra_oculta)
