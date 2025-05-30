import platform
import socket

print("Información del sistema:")
print(f"Sistema operativo: {platform.system()} {platform.release()}")
print(f"Nombre del equipo: {platform.node()}")
print(f"Dirección IP local: {socket.gethostbyname(socket.gethostname())}")
