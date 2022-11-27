#Importaciones
import pyautogui
import time
from tkinter.filedialog import askopenfilename
#Variables
texto_enviar = askopenfilename(filetypes=[('Archivos de texto', '*.txt')])
tiempo_antes_iniciar = int(input("Inserte tiempo antes de iniciar: "))
tiempo_entre__envios = int(input("Inserte tiempo entre mensaje y mensaje: "))
archivo = open(texto_enviar, 'r')
#main
time.sleep(tiempo_antes_iniciar)
for frase in archivo:
    time.sleep(tiempo_entre__envios)
    pyautogui.typewrite(frase)
    pyautogui.press("enter")
print("Completado")