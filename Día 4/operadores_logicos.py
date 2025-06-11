mi_bool = (4 < 5) and (5 == 2+3)
mi_bool2 = (55 == 55) and ('perro' == 'perro')

mi_bool3 = 1 == 10 or 3 == 3

print(mi_bool)
print(mi_bool2)
print(mi_bool3)

texto = 'esta frase es breve'

mi_bool4 = ('frase' in texto) or ('python' in texto)
print(mi_bool4)

mi_bool5 = not('a' == 'a')
print(mi_bool5)


# EJERCICIOS

#Crea tres variables (num1 ,  num2 y num3):
#Dentro de num1, almacena el valor 36
#Dentro de num2, almacena el resultado de la operación 72/2
#Dentro de num3, almacena el valor 48
#Verifica si num1 es mayor que num2, y menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.

num1 = 36
num2 = 72 / 2
num3 = 48
mi_bool6 = (num1 > num2) and (num1 < num3)
print(mi_bool6)


#Crea tres variables (num1 ,  num2 y num3):
#Dentro de num1, almacena el valor 36
#Dentro de num2, almacena el resultado de la operación 72/2
#Dentro de num3, almacena el valor 48
#Verifica si num1 es mayor que num2, o menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.

mi_bool7 = (num1 > num2) or (num1 < num3)
print(mi_bool7)


#Verifica si las palabras almacenadas en las siguientes variables:
#palabra1 = "éxito", y
#palabra2 = "tecnología"
#no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:

#"Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
#Elon Musk

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool8 = (palabra1 not in frase) and (palabra2 not in frase)
print(mi_bool8)