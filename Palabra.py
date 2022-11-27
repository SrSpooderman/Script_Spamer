#importaciones
import pyautogui
import time
#variables
array_repetir = str(input("inserte palabra para repetir: "))
tiempo_antes_iniciar = int(input("Inserte tiempo antes de iniciar: "))
tiempo_entre__envios = int(input("Inserte tiempo entre mensaje y mensaje: "))
#main
time.sleep(tiempo_antes_iniciar)
while True:
    pyautogui.typewrite(array_repetir)
    time.sleep(tiempo_entre__envios)
    pyautogui.press("enter")