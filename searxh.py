from datetime import datetime, timedelta
import pyautogui

# Time
timeStart = datetime.now()
timeFinish = timeStart + timedelta(seconds=300)


# Auto clicker
def auto_click():
    while timeStart < timeFinish:
        button = pyautogui.locateOnScreen("image/alreadysn.PNG", confidence=0.95)
        if button:
            print("ЕСТЬ")
            pyautogui.click(button)
            pyautogui.sleep(1)
        elif button is None:
            print("НЕТУ")
            pyautogui.sleep(1)


auto_click()
