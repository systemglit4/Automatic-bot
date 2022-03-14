# Authorization
import pickle
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By

# Enter your data
# login = "systemglit4@gmail.com"
# password = "567Block234Farm89!"

# Options
useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.Chrome}")
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

# Variables
url = "https://blockfarm.club/farm/mylands"
driver = webdriver.Chrome(
    executable_path=r"Driver\chromedriver.exe",
    options=options,
)


def auth():
    try:
        # WITH COOKIES
        driver.get(url=url)
        for cookie in pickle.load(open(f"Cookies/cookie", "rb")):
            driver.add_cookie(cookie)
            driver.refresh()
            driver.get(url=url)
    except FileNotFoundError:
        # Enter your login and password:
        print("Hi,Enter your login and password: ")
        login = input("Enter login: ")
        password = input("Enter password: ")
        # MADE COOKIES
        driver.get(url=url)
        # Email
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys(login)
        # Password
        pass_input = driver.find_element(By.ID, "password")
        pass_input.send_keys(password)
        # Button Login
        log_in = driver.find_element(By.TAG_NAME, "BUTTON")
        log_in.click()
        # Cookies
        pickle.dump(driver.get_cookies(), open(f"Cookies/cookie", "wb"))
