#El metodo open recibe como 2° parametro tres opciones: r= Read, w= write (reemplaza el texto anterior por el nuevo),
# a= posiciona el cursor al final del texto del archivo

archivo = open('prueba.txt', 'a')

archivo.write('''Hola
mundo
''')
archivo.write('Soy el nuevo texto!')
archivo.writelines(['\nHola', 'Soy', 'un', 'texto', 'creado', 'con', 'writelines'])

archivo.close()

#EJERCICIOS

# Abre el archivo mi_archivo.txt y cambia su contenido por el texto: Nuevo texto
mi_archivo = open('mi_archivo.txt', 'w')
mi_archivo.write('Nuevo texto')
mi_archivo.close()

mi_archivo2 = open('mi_archivo.txt', 'r')
print(mi_archivo2.readline())
mi_archivo2.close()

#Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".
# Imprime el contenido completo de "mi_archivo.txt" al finalizar.
my_archivo = open('mi_archivo.txt', 'a')
my_archivo.write('Nuevo inicio de sesión')
my_archivo.close()

my_archivo = open('mi_archivo.txt', 'r')
print(my_archivo.read())
my_archivo.close()

#Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt".
# Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
last_file = open('registro.txt', 'a')
for palabra in registro_ultima_sesion:
    last_file.writelines(palabra + '\t')
last_file.close()

last_file = open('registro.txt', 'r')
print(last_file.read())
last_file.close()