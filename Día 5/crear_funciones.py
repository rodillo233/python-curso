def saludar_persona(nombre):
    print(f'Hola {nombre}!')

saludar_persona('Rodolfo')

#EJERCICIOS

#Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla ¡Hola mundo!

def saludar():
    print('¡Hola mundo!')

#Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, y cada vez que sea llamada imprima
#en pantalla ¡Bienvenido {nombre_persona}!. Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras

def bienvenida(nombre_persona):
    print(f'¡Bienvenido {nombre_persona}!')

nombre_persona = 'Rodolfo'

#Declara una funcion llamada cuadrado, que tome como argumento un número cualquiera, y cada vez que sea llamada, imprima en
#pantalla el cuadrado de dicho número. El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable
#y asígnale el número que quieras.

def cuadrado(numero):
    print(f'{numero ** 2}')

numero = 15