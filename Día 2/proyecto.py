# Calcular la ganancia de los trabajadores, que sera del 13% del total de la venta
# Preguntar Nombre y total de la venta
# Devolver Ok {nombre}. este mes ganaste ${ganancia}
print('*** Vamos a calcular tu ganancia mensual. ***')

nombre = input('Ingresa tu Nombre: ')
venta_mensual = float(input('Ingresa el total de tu venta del mes: '))
comision = round((venta_mensual*13)/100, 2)

print(f'Ok {nombre}. Este mes ganaste ${comision}')