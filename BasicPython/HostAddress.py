
import socket

hostname = socket.gethostname()
IPAddress = socket.gethostbyname(hostname)

print(" Computer Name :" + hostname)
print(" Computer IP Address :" + IPAddress)
