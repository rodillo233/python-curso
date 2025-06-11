from random import randint
print('ADIVINA EL NÚMERO!!')

name = input('Cual es tu nombre? : ').strip()
print(f'{name} Tienes 8 oportunidades para adivinar el número entre 1 y 100, comenzamos!\n')
intentos = 1
number = randint(1, 100)

while intentos <= 8:
    input_number = int(input(f'Intento {intentos} Ingresa un Número entre 1 y 100: '))

    if input_number not in range(1,101):
        print(f'{input_number}, no es un Número válido!\n')
    elif input_number < number:
        print(f'Incorrecto!, {input_number} es menor al número incognito.\n')
    elif input_number > number:
        print(f'Incorrecto!, {input_number} es mayor al número incognito.\n')
    else:
        print(f'Excelente {name}!! haz adivinado el número a los {intentos} intentos.\n')
        break
    intentos += 1

    if intentos > 8:
        resp = input(f'{name} agotaste tus intentos, quieres volver a jugar? (s/n): ').strip()
        match resp:
            case 's':
                intentos = 1
            case 'n':
                break



