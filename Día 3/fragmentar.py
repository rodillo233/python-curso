texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento = texto[2:10:2]

print(fragmento)

#EJERCICIOS

#Extrae la primera palabra de la siguiente frase utilizando slicing,
#y muestrala en pantalla
frase = "Controlar la complejidad es la esencia de la programación"
fragmento_frase = frase[:9]
print(fragmento_frase)

#Toma cada tercer caracter empezando desde el noveno hasta el final
#de la frase, e imprime el resultado
phrase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento_phrase = phrase[8::3]
print(fragmento_phrase)

#Invierte la posición de todos los caracteres de la siguiente frase y muestra
#el resultado en pantalla
frase1 = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
fragmento1 = frase1[::-1]
print(fragmento1)

