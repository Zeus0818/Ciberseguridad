def binario(decimal):
    binario = ""
    while decimal > 1:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input("Ingrese un número que quieras convertir a binario: "))
print("El número en binario es:", binario(numero))
