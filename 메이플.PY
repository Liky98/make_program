import pyautogui
import time
import os

a1= pyautogui.locateCenterOnScreen('white.PNG') 
pyautogui.moveTo(a1) #화면 캡쳐한 곳 가운데로 이동

pyautogui.click() #한번 클릭
time.sleep(1) #1초 대기

for i in range(0,20) :
    pyautogui.write(str(i+1) + 'BoomBoomBoomBoomBoom')
    pyautogui.write(['enter'])


os.system('pause')
