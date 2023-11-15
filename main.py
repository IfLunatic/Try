import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


s = Service(executable_path='chromedriver-win64/chromedriver.exe')

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\Dima (IfLunatic)\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
chrome_options.add_argument("--disable-web-security")
driver = webdriver.Chrome(service=s, options=chrome_options)


try:
    driver.maximize_window()
    driver.get('https://getpass.civic.com/status?chain=polygon')
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="headlessui-listbox-button-:r0:"]'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='CAPTCHA Verification']"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/button'))
    ).click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/button'))
    ).click()
    time.sleep(2)

    active_window = driver.window_handles[-1]
    driver.switch_to.window(active_window)

    driver.execute_script("document.getElementById('password').value = 'password';")
    time.sleep(2)
    driver.execute_script("document.getElementById('password').dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter' }));")


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()