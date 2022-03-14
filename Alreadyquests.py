import pyautogui
from Quests import gl_quests, sn_quests, mn_quests


def already_quest():
    already_gl = pyautogui.locateOnScreen("image/alreadygl.PNG", confidence=0.95)
    already_sn = pyautogui.locateOnScreen("image/alreadysn.PNG", confidence=0.95)
    already_mn = pyautogui.locateOnScreen("image/alreadymn.PNG", confidence=0.95)
    # Global quest already
    for gl in already_gl is None:
        try:
            gl
        except pyautogui.ImageNotFoundException:
            gl_quests()
            break
    # Sun quest already
    for sn in already_sn is None:
        if sn is None:
            sn_quests()
        elif sn:
            break
    # Moon quest already
    for mn in already_mn is None:
        if mn is None:
            mn_quests()
        elif mn:
            break
