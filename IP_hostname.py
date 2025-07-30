#Encontraremos el nombre e IP del ordenador mediante sockets
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("El nombre de tu ordendor es : " +hostname)
print("Tu direccion IP es " +ip)
