def multiplicar(num1, num2):
    total = num1 * num2
    return total

resultado = multiplicar(5,10)
print(resultado)

#EJERCICIOS

#Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número que resulte
#de resolver una potencia, utilizando el primer número como base, y el segundo como exponente.

def potencia(num1, num2):
    resultado = num1 ** num2
    return resultado

resultado = potencia(9, 2)
print(resultado)

#Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses)
#y devuleva como resultado el monto equivalente en euros. A fines de este ejemplo tomaremos la conversion 1USD = 0.90 EUR
#Crea una variable llamada dólares y almacena en ella un monto cualquiera para entregarselo a tu dunción y evaluar el resultado.

def usd_a_eur(usd):
    conversion = usd * .90
    return conversion

dolares = 50

total = usd_a_eur(dolares)
print(total)

#Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de
# sus caracteres y los devuelva de ese modo y en mayúsculas. Por ejemplo si proporcionas "Python" devolvera "NOHTYP".
#Tambien deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para suministrarle como argumento
#a la función creada.

def invertir_palabra(palabra):
    lista = palabra[::-1].upper()
    return lista
palabra = 'Python'

res = invertir_palabra(palabra)
print(res)