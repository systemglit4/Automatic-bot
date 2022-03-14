# Library
from Authorization import auth, driver
from Alreadyquests import already_quest

# !!!! ПОИСК ПО ONCLICK !!!!
# driver.find_element(By.XPATH, "//button[@onclick=\"claimedDailyQuest('water')\"]").click()

# All_code
try:
    auth()
    already_quest()

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
