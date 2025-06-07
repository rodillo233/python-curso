
diccionario = {
    'c1': 'valor1',
    'c2': 'valor2'
}

print(type(diccionario)) # class dict
print(diccionario)

resultado = diccionario['c2']
print(resultado)

#---------------------------------------

cliente = {
    'nombre': 'Juan',
    'apellido': 'Fuentes',
    'peso': 80,
    'talla': 1.76
}

consulta = cliente['nombre']
print(consulta)

#--------------------------------------

dic = {
    'c1': 55,
    'c2': [10,20,30],
    'c3': {'s1': 100, 's2':200}
}

print(dic['c2'][1]) #20
print(dic['c3']['s2']) #200

#--------------------------------------
#imprimir la letra E

dic2 = {
    'c1': ['a', 'b', 'c'],
    'c2': ['d', 'e', 'f']
}
print(dic2['c2'][1].upper())

#--------------------------------------
#agregar una clave al diccionario
dic3 = {
    1: 'a',
    2: 'b'
}

dic3[3] = 'c'
dic3[4] = 'd'
dic3[2] = 'B' # modifica un valor existente
print(dic3)

#--------------------------------------
#devolver las claves del diccionario
print(dic3.keys())
#devolver los valores del diccionario
print(dic3.values())
#devolver todo lo que hay en el diccionario
print(dic3.items())

# EJERCICIOS

#Crea un diccionario llamado mi_dic que almacena la siguiente informacion de una persona:
#nombre: Karen, apellido: Jurgens, edad: 35, ocupacion: Periodista
#Los nombres de las claves y valores deben ser iguales a la consigna

mi_dic = {
    'nombre': 'Karen',
    'apellido': 'Jurgens',
    'edad': 35,
    'ocupacion': 'Periodista'
}


#Crea una funcion print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario
#Si el valor 300 cambiara en el futuro, el codigo deberia funcionar igual para devolver el valor que se encuentre
#en esa misma posicion. Para ello, deberas hacer referencia a los nombres de las claves y/o indices segun corresponda

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])


#Actualiza la informacion de nuestro diccionario llamado mi_dic2 (reasignando nuevos valores a las claves segun corresponda)
#y agrega una nueva clave llamada 'pais'. Los nuevos datos son: nombre: Karen, apellido: Jurgens, edad: 30, ocupacion: Editora, pais: Colombia
# para ello, no debes cambiar la linea de codigo ya escrita, sino actualizar los valores mediante metodos de diccionarios

mi_dic2 = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic2['edad'] = 36
mi_dic2['ocupacion'] = 'Editora'
mi_dic2['pais'] = 'Colombia'
print(mi_dic2)

del mi_dic2['nombre']
print(mi_dic2)