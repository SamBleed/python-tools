import subprocess

print("Reiniciando adaptador WiFi...")
subprocess.call('netsh interface set interface "Wi-Fi" admin=disable', shell=True)
subprocess.call('netsh interface set interface "Wi-Fi" admin=enable', shell=True)
print("WiFi reiniciado.")
