
texto = input('Ingresa el texto que requieras: ').lower()
letras = input('Ingresa tres letras a tu elección separadas por un espacio: ').lower().split(' ')

aparece_primera = texto.count(letras[0])
aparece_segunda = texto.count(letras[1])
aparece_tercera = texto.count(letras[2])

texto_lista = texto.split(' ')
contador_palabras = len(texto_lista)


texto_lista_invertido = texto_lista
texto_lista_invertido.reverse()
texto_invertido = ' '.join(texto_lista_invertido)

esta_python = texto.find('python')
#'python' in texto
respuesta = esta_python > 0
respuesta_python = {
    True : 'Si se encuentra',
    False : 'No se encuentra'
}

print('\n*********** Resultado del analizador de texto ***********')
print(f'1.- La letra {letras[0]} aparece: {aparece_primera} veces, la letra {letras[1]} aparece: {aparece_segunda} veces y la letra {letras[2]} aparece {aparece_tercera} veces.')
print(f'2.- El texto ingresado tiene {contador_palabras} palabras.')
print(f'3.- La primera letra del texto ingresado es: "{texto[0]}" y la última "{texto[-1]}"')
print(f'4.- El texto invertido es: {texto_invertido}')
print(f'5.- Se encuentra la palabra python? {respuesta_python[respuesta]}')