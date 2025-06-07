#conversiones implicitas
num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))

#conversiones explicitas
num3 = 5.8
print(num3)
print(type(num3))

num4 = int(num3)
print(num4)
print(type(num4))

edad = input('Ingresa tu edad: ')
print(type(edad))

edad = int(edad)
print(type(edad))

nueva_edad = 1 + edad
#No se puede concatenar str con int
print("Tu nueva edad será: " + nueva_edad)

