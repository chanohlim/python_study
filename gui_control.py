import pyautogui, os, time

os.chdir('/Users/chanlim/Desktop')

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

time.sleep(3)
pyautogui.click()

#x,y = pyautogui.locateOnScreen('name.png')

