
if 5 == 2:
    print('Es correcto')
else:
    print('No es correcto')

#######################

mascota = 'conejo'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No se que animal tienes')

########################

edad1 = 16
calificacion = 9

if edad1 < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('Reprobado')
else:
    print('Eres Adulto')

# EJERCICIOS

#Utilizando las variables num1 y num2, que se alimentan con el input del usuario:
#Crea una estructura de control de flujo que compare los valores de las variables, y arroje un resultado de acuerdo al caso:
#num1 es mayor que num2
#num2 es mayor que num1
#num1 y num2 son iguales
#Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1 y num2

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

if num1 > num2:
    print(f'{num1} es mayor que {num2}')
elif num2 > num1:
    print(f'{num2} es mayor que {num1}')
else:
    print(f'{num1} y {num2} son iguales')

#Las leyes de un pais establecen que un adulto puede conducir si tiene licencia para hacerlo, y para optar por una licencia para conducir
#debe tener 18 años o mas. Crea una estructura condicional pára verificar si una persona de 16 años sin licencia puede conducir,
#y muestra el resultado que corresponda en pantalla:
#Puedes conducir
#No puedes conducir aun, debes tener 18 años y contar con licencia
#No puedes conducir, Necesitas contar con una licencia.

edad = 89
tiene_licencia = False

if edad >= 18 and tiene_licencia:
    print('Puedes conducir')
elif edad < 18 and not(tiene_licencia):
    print('No puedes conducir aún. Debes tener 18 años y contar con una licencia')
elif edad >= 18 and not(tiene_licencia):
    print('No puedes conducir. Necesitas contar con una licencia')

#Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de ingles
#Crea una estructura condicional para evaluar a un candidato dada estas condiciones, y muestra el mensaje correspondiente en pantalla:
#Cumples con los requisitos para postularte
#Para postularte, necesitas saber programar en python y tener conocimiento de ingles
#Para postularte, necesitas tener conocimiento de ingles
#Para postularte, necesitas saber programar en Python

habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print('Cumples con los requisitos para postularte')
elif sabe_python and not(habla_ingles):
    print('Para postularte, necesitas tener conocimiento de inglés')
elif habla_ingles and not(sabe_python):
    print('Para postularte, necesitas saber programar en Python')
else:
    print('Para postularte, necesitas saber programar en Python y tener conocimiento de inglés')