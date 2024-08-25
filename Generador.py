# GENERADOR DE CONTRASEÑAS SEGURAS

import string
import random

#Establece la longitud de la ccontraeña
longitud = int (input("Ingrese el tamaño de la contraseña : "))

#Genera los caracteres para usar en la contraseña 
caracteres = string.ascii_letters + string.digits + string.punctuation

#Genera aleatoriamente la contraseña con la longitud especifica
contraseña = "".join( random.choice(caracteres) for i in range(longitud) )

#Imprime la contraseña
print("La contraseña segura es: " +contraseña)

