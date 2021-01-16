import pyautogui
import time

pyautogui.position()
pyautogui.moveTo(2180,168,2)
pyautogui.doubleClick()
time.sleep(1)
pyautogui.typewrite('HelloWorld!')
pyautogui.moveTo(2735,852,1)
pyautogui.doubleClick()