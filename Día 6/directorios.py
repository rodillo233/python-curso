import os
from pathlib import Path #desde ver. 3.4 python

#getcurrentworkingdirectory nos da la ruta actual en la que estamos trabajando
ruta = os.getcwd()
print('Ruta actual: ' + ruta + '\n')

#changedirectory cambiamos de ruta
ruta1 = os.chdir('/Users/rodillo/Desktop/')
archivo = open('otro_archivo.txt')
print(archivo.read() + '\n')

#makedirectories crea carpetas
#ruta3 = os.makedirs('/Users/rodillo/Desktop/otra_carpeta')

#obtener el directorio y el nombre del archivo de una ruta
ruta2 = '/Users/rodillo/Documents/python-curso/python total/Python/Día 6/prueba.txt'

#nombre de archivo
elemento = os.path.basename(ruta2)

#ruta
path = os.path.dirname(ruta2)

#ambos
ambos = os.path.split(ruta2) # -> devuelve una tupla con ambos valores
print(elemento)
print(path)
print(ambos)

#eliminar carpeta
#os.rmdir('/Users/rodillo/Desktop/otra_carpeta')

#abrir archivo sin os
otro_archivo = open('/Users/rodillo/Desktop/otro_archivo.txt')
print(otro_archivo.read())

#Modulo Path
carpeta = Path('/Users/rodillo/Desktop/otra_carpeta')
archivo = carpeta / 'nuevo_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())