# Auto clicker v1.0
import time
import pyautogui
from datetime import datetime, timedelta
from Authorization import driver


# Time
# timeStart = datetime.now()
# timeFinish = timeStart + timedelta(seconds=5)


def auto_click():
    time.sleep(5)
    i = 2
    button = pyautogui.locateOnScreen("image/interact.PNG", confidence=0.8)
    reward = pyautogui.locateOnScreen("image/reward.PNG", confidence=0.9)
    loading1 = pyautogui.locateOnScreen("image/loading.PNG", confidence=0.9)
    loading2 = pyautogui.locateOnScreen("image/loading2.PNG", confidence=0.9)
    # for loading in loading1 or loading2:
    #     if loading:
    while i < 3:
        # Buttons
        if button:
            # Click Buttons
            for buttons in button:
                if buttons:
                    pyautogui.click(button)
                elif buttons is None:
                    break
        if loading1:
            # Loop Loading
            for loop_loading in loading1:
                # Time
                timeStart = datetime.now()
                timeFinish = timeStart + timedelta(seconds=4)
                if loop_loading > timeFinish:
                    driver.refresh()
                elif loop_loading < timeFinish:
                    break
        # Rewards
        if reward:
            for rewards in reward:
                if rewards:
                    pyautogui.click(rewards)
                elif rewards is None:
                    break
        if loading1 or loading2:
            for loading in loading1 or loading2:
                if loading:
                    try:
                        loading1 and loading2
                    except pyautogui.ImageNotFoundException:
                        break
                elif loading is None:
                    break
        time.sleep(3)

    # Старый автокликер
    # while timeStart < timeFinish:
    #     button = pyautogui.locateOnScreen("image/interact.PNG", confidence=0.8)
    #     rewards = pyautogui.locateOnScreen("image/reward.PNG", confidence=0.9)
    #     # loading = pyautogui.locateOnScreen("image/loading.PNG", confidence=0.9)
    #     # loading2 = pyautogui.locateOnScreen("image/loading2.PNG", confidence=0.9)
    #     if button:
    #         pyautogui.click(button)
    #         pyautogui.sleep(9)
    #     elif rewards:
    #         pyautogui.click(rewards)
    #         pyautogui.sleep(9)
    #     elif button is None:
    #         break
