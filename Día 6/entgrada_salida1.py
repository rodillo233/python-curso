mi_archivo = open('prueba.txt')

#metodo readline()
#una_linea = mi_archivo.readline()
#print(una_linea.upper())

#una_linea = mi_archivo.readline()
#print(una_linea.rstrip()) # -> Elimina el salto de línea

#una_linea = mi_archivo.readline() # con readline guarda el punto donde leyo la última vez y cuando es llamado de nuevo lo hace desde donde se quedo.
#print(una_linea)



#Podemos iterar cada linea del archivo
#for linea in mi_archivo:
    #print(f'Aqui dice: {linea}')



#metodo readlines() genera una lista con las lineas que contiene el documento
todas = mi_archivo.readlines()
todas = todas.pop()
print(todas)


mi_archivo.close()

#EJERCICIOS
#Abre el archivo texto.txt e imprime su contenido
archivo = open('texto.txt')
#print(archivo.read())

#Imprime la primera línea del archivo
linea_uno = archivo.readline()
print(linea_uno)

#Abre el archivo texto.txt e imprime únicamente la segunda línea
linea_uno = archivo.readline()
print(linea_uno)

archivo.close()
