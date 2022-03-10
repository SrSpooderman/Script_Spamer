import pyautogui
import time
time.sleep(5)
f = open("si.txt", 'r')
for word in f:
    time.sleep(2)
    pyautogui.typewrite(word)
    pyautogui.press("enter")
