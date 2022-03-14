# Quests
import time
from lands import gl_land, sn_land, mn_land
from AutoClicker import auto_click
from Authorization import driver


# Global quest
def gl_quests():
    # First island
    driver.get(url=gl_land[0][0])
    time.sleep(1)
    auto_click()
    # Second island
    driver.get(url=sn_land[1][0])
    time.sleep(1)
    auto_click()


# Sun quest
def sn_quests():
    # First island
    driver.get(url=sn_land[0][0])
    time.sleep(1)
    auto_click()
    # Second island
    driver.get(url=sn_land[1][0])
    time.sleep(1)
    auto_click()
    # Third island
    driver.get(url=sn_land[2][0])
    time.sleep(1)
    auto_click()


# Moon quest
def mn_quests():
    # First island
    driver.get(url=mn_land[0][0])
    time.sleep(1)
    auto_click()
    # Second island
    driver.get(url=mn_land[1][0])
    time.sleep(1)
    auto_click()
    # Third island
    driver.get(url=mn_land[2][0])
    time.sleep(1)
    auto_click()
    # Fourth island
    driver.get(url=mn_land[3][0])
    time.sleep(1)
    auto_click()
    # Fifth island
    driver.get(url=mn_land[4][0])
    time.sleep(1)
    auto_click()
