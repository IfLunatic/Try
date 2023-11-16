import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


s = Service(executable_path='chromedriver-win64/chromedriver.exe')

chrome_options = Options()
user_data_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default')
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_extension("Rainbow.crx")
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
            (By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/button'))
    ).click()
    time.sleep(2)

    active_window = driver.window_handles[-1]
    driver.switch_to.window(active_window)

    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="main"]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div[5]/div/div[1]/input'))
    )

    password_input.send_keys("ASDpasswordASD")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="main"]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div[6]/div/button'))
    ).click()
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="main"]/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div[1]/button'))
    ).click()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/div/div[1]/div[3]/div[1]/div/div/div/div/div[2]/button[1]'))
    ).click()
    time.sleep(5)

    checkbox = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="scrollContainer"]/div[2]/div/input'))
    ).click()


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()