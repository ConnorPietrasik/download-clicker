import pyautogui
from time import sleep

count = 0
while True:
    try:
        x, y = pyautogui.locateCenterOnScreen("slow.png", confidence=0.7)
        count += 1
        old_x, old_y = pyautogui.position()
        pyautogui.click(x, y)
        pyautogui.moveTo(old_x, old_y)
        #with pyautogui.hold("alt"):
        #    pyautogui.press("tab")
        print(f"Clicked: {count}")
    except pyautogui.ImageNotFoundException:
        print("Missed!")

    sleep(8)