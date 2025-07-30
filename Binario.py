# Definimos una función llamada 'binario' que recibe un número decimal como parámetro
def binario(decimal):
    binario = ""  # Inicializamos una cadena vacía donde construiremos el número binario
    while decimal > 1:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    # Finalmente, agregamos el último dígito (el que hace que decimal <= 1)
    return str(decimal) + binario

# Solicitamos al usuario un número entero
numero = int(input("Ingrese un número que quieras convertir a binario: "))
# Llamamos a la función y mostramos el resultado
print("El número en binario es:", binario(numero))
