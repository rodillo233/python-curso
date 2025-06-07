texto = 'Este es el texto de Rodolfo'

resultado = texto.upper()
resultado2 = texto.lower()
resultado3 =  texto.split() # devuelve una lista con el texto separado por palabras


print(resultado)
print(resultado2)
print(resultado3)

a = 'Aprender'
b = 'Python'
c = 'es'
d = 'genial'
e = ' '.join([a,b,c,d])
print(e)

resultado4 = texto.find('e')
print(resultado4)

resultado5 = texto.replace('Rodolfo', 'Todos')
print(resultado5)

#EJERCICIOS

#Imprime el siguiente texto en mayusculas, empleando el metodo especifico de strings
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

#Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza
#el metodo apropiado de listas/strings, y muestra en pantalla el resultado
lista_palabras = ['La', 'legibilidad', 'cuenta']
res = ' '.join(lista_palabras)
print(res)

#Reemplaza en la siguiente frase:
#"Si la implementación es difícil de explicar, puede que sea una mala idea."
#los siguientes pares de palabras: dificil -> facil, mala -> buena
#muestra en pantalla el cambio
frase2 = "Si la implementación es difícil de explicar, puede que sea una mala idea."
res = frase2.replace('difícil', 'facil').replace('mala', 'buena')
print(res)