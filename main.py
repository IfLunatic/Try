import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

# Specify the path to the web driver
s = Service(executable_path='chromedriver-win64/chromedriver.exe')

chrome_options = Options()

# Take the cache from the system so that the extension (Rainbow) does not ask to register
user_data_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default')
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# Connecting the Rainbow extension itself
chrome_options.add_extension("Rainbow.crx")

# Connecting the Captcha-Solver-Auto-Recognition-and-Bypass extension
chrome_options.add_extension("Captcha-Solver-Auto-Recognition-and-Bypass.crx")

driver = webdriver.Chrome(service=s, options=chrome_options)


try:

    # Open the page in full screen to avoid nuances with the mobile version
    driver.maximize_window()
    driver.get('https://getpass.civic.com/status?chain=polygon')
    time.sleep(2)

    # Opening the drop-down list
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, '//*[@id="headlessui-listbox-button-:r0:"]'))
    ).click()

    # Select an option from the drop-down list
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//span[text()='CAPTCHA Verification']"))
    ).click()

    # Finding the button at the top right
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, '//button[@class="sc-csKJRI erRRBL" and @type="button"]'))
    ).click()
    time.sleep(2)

    # Choose Rainbow
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, '//button[contains(div, "Rainbow")]'))
    ).click()
    time.sleep(2)

    # Switch to our extension to work with it in the future
    active_window = driver.window_handles[-1]
    driver.switch_to.window(active_window)

    # Enter password
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, '//input[@type="password" and contains(@placeholder, "Password")]'))
    ).send_keys("ASDpasswordASD")  # Enter correct password
    time.sleep(2)

    # Click to button 'unlock' in extension
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="main"]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div[6]/div/button'))
    ).click()
    time.sleep(2)

    # Click to button connect
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="main"]/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/div[1]/button'))
    ).click()
    time.sleep(2)

    # Switch to main window
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

    # Click to button with text GET PASS
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, '/html/body/div/div/div[1]/div[3]/div[1]/div/div/div/div/div[2]/button[1]'))
    ).click()
    time.sleep(2)

    iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]
    # switch to selected iframe
    driver.switch_to.frame(iframe)

    # Activate checkbox
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, '//input[@data-testid="TERMS_AND_CONDITIONS_CHECKBOX"]'))
    ).click()
    time.sleep(2)

    # Click on the Start Verification button
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, '//button[@data-testid="START_BUTTON"]'))
    ).click()
    time.sleep(2)

    # Click on the Continue button
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, '//button[@type="button"]'))
    ).click()
    time.sleep(2)

    # Switch to extension window
    active_window = driver.window_handles[-1]
    driver.switch_to.window(active_window)

    # Signing in the extension
    WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="main"]/div/div/div[1]/div/div/div/div/div/div[2]/div/div[2]/div[1]/button'))
    ).click()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[0])

    time.sleep(20)

    iframe_xpath = '//iframe[@data-testid="IFRAME"]'
    iframe = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, iframe_xpath))
    )
    driver.switch_to.frame(iframe)

    # Wait for the button to appear after solving the captcha
    button_after_captcha_xpath = ('//button[@type="button" and @data-testid="OK_BUTTON" '
                                  'and contains(@class, "buttonDefault")]/div/span[text()="Continue"]')
    WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, button_after_captcha_xpath))
    )

    # Click the button after the captcha is solved
    driver.find_element(By.XPATH, button_after_captcha_xpath).click()

except Exception as ex:
    print(ex)
finally:
    time.sleep(60)
    driver.close()
    driver.quit()
