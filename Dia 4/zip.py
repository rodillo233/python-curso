#zip combina dos o mas listas entrelazando sus elementos en tuplas

nombres = ['Rodo', 'Samantha', 'Sarah']
edades = [30, 11, 7, 29] # toma en cuenta el tamaño de la lista mas corta
ciudades = ['Guzman', 'Guadalajara', 'Colima']

combinados = list(zip(nombres, edades, ciudades))

for nombre, edad, ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')

#EJERCICIOS

#Muestra en pantalla frases como la del siguiente ejemplo: La capital de Alemania es Berlín. Utiliza la fuinción zip,
#loops y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

for pais, capital in list(zip(paises, capitales)):
    print(f'La capital de {pais} es {capital}')

#Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tu prefieras, dentro de la variable mi_zip.
marcas = ['NIke', 'Adidas', 'Puma', 'Under Armour']
productos = ['Tenis', 'Pants', 'Gorras', 'Shorts']
mi_zip = zip(productos, marcas)

#Crea el zip con las traducciones de los numeros del 1 al 5 en español, portugues e ingles en el mismo orden, y convierte
#el objeto generado en una lista almacenada en la variable numeros.

espanol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(espanol, portugues, ingles))
