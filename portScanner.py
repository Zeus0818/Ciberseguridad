import socket

# Solicitar la IP a escanear
ip = input("Ingrese la dirección IP a escanear: ")

# Recorrer el rango de puertos
for puerto in range(1, 65535):
    # Crear un socket 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Se puede ajustar el timeout según necesidades

        # Intentar conectar al puerto
        result = sock.connect_ex((ip, puerto))

        # Si la conexión es exitosa, el puerto está abierto
        if result == 0:
            print(f"Puerto Abierto: {puerto}")
            sock.close()
        # Se omite la impresión de puertos cerrados para no generar salida innecesaria
        else:
               print(f"Puerto Cerrado: {puerto}")



    # ip de Prueba de NMAP : 45.33.32.156
