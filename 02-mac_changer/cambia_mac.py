import subprocess
import random

def generar_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0x00, 0xff) for _ in range(5))

interfaz = input("Nombre de la interfaz (Ej: Ethernet): ")
nueva_mac = generar_mac()
print(f"Estableciendo nueva MAC: {nueva_mac}")

subprocess.call(f'netsh interface set interface "{interfaz}" admin=disable', shell=True)
subprocess.call(f'reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{{4d36e972-e325-11ce-bfc1-08002be10318}}\0001 /v NetworkAddress /d {nueva_mac.replace(":", "")} /f', shell=True)
subprocess.call(f'netsh interface set interface "{interfaz}" admin=enable', shell=True)
