dic = {
    'clave1': 100,
    'clave2': 500
}

dic2 = dic.popitem()
print(dic2)

#EJERCICIOS

#Remueve los caracteres a la izquierda de nuestro texto principal. Utiliza el metodo lstrip(). Imprime el
#resultado en pantalla.

texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:%_#')
print(texto)

#Añade el elemento naranja como el cuarto elemento de la siguiente lista "frutas", utilizando el metodo insert().
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, 'naranja')
print(frutas)

#Verifica si los sets a continuacion forman conjuntos aislados (es decir, que no tienen elementos en comun), utilizando
#el metodo isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados.
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)
print(conjuntos_aislados)