import subprocess

ip = input("Ingresa la IP a escanear: ")
print("Escaneando con Nmap...")
subprocess.call(f"nmap -sS -T4 {ip}", shell=True)
