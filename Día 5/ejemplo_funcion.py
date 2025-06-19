precios_cafe = [('capuchino', 3.5), ('expresso', 1.2), ('moka', 1.9), ('americano', 2.5)]

for cafe, precio in precios_cafe:
    print(precio * 0.50)

#Extraer el cafe mas caro
def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (cafe_mas_caro, precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)
print(f'El cafe mas caro es {cafe}, cuyo precio es: {precio}')