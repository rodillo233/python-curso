def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor

    return total

print(suma(x=3, y=5, z=2))

###################################

def suma2(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

args = [400,45,100,236,985]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}
suma2(15,59, *args, **kwargs)


# EJERCICIOS

#Crea una funcion llamada cantidad_atributos que cuente la cantidad de parametros que se entregan y devuelva esa cantidad
#como resultado.

def cantidad_atributos(**kwargs):
    total_parametros = len(kwargs)
    return total_parametros

total = cantidad_atributos(a=3, b=4, c=1, d=6, e=8)
print(total)

#Crea una funcion llamada lista_atributos que devuelva en forma de lista los valores de los atributos entrtegados en forma
#de palabras clave. La funcion debe preever recibir cualquier cantidad de argumentos de ese tipo.

def lista_atributos(**kwargs):
    lista = []
    for clave,valor in kwargs.items():
        lista.append(valor)
    print(lista)


lista_atributos(a=3, b=4, c=1, d=6, e=8)

#Crea una funcion llamada describir_persona, que tome como parametros su nombre y luego una cantidad indeterminada de
#argumentos. Esta funcion debera mostrar en pantalla por ejemplo:
#describir_persona("Maria", color_ojos='azules', color_pelo="rubio")
#Se muestra:
# Caracteristicas de Maria:
# color_ojos: azules
# color_pelo: rubio

def describir_persona(name, **kwargs):
    print(f'Caracteristicas de {name}:')
    for clave,valor in kwargs.items():
        print(f'{clave}: {valor}')

describir_persona("Maria", color_ojos='azules', color_pelo="rubio")

