import pyautogui
import time

pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("notepad")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("Automação com pyautogui", interval=0.1)
pyautogui.hotkey("Ctrl" ,"s")
time.sleep(2)
pyautogui.write("teste.txt")
pyautogui.press("enter")
time.sleep(1)
print("Arquivo salvo")
