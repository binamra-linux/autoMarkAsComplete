from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import getpass

userid = "ENter your Username"
passid = "Enter your password"
# print("Password Has been entered")



driver = webdriver.Firefox()
driver.get("https://schoolworkspro.com/modules/computer-system-and-networks")
wait = WebDriverWait(driver, 10)

try:
    # Wait for username and password fields to load
    username = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    password = driver.find_element(By.NAME, "password")

    # Perform login
    username.send_keys(f"{userid}")
    password.send_keys(f"{passid}")
    password.send_keys(Keys.RETURN)
    resources_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="#Resources" and contains(text(), "Resources")]')))

    resources_link.click()
    print("Successfully clicked on Resources!")

except Exception as e:
    print(f"An error occurred: {e}")




week_1_link = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(@data-target, '1')]"))
)
week_1_link.click()
lesson_1 = driver.find_element(By.CSS_SELECTOR, ".lectures_lists_title")
lesson_1.click()



while True:
    time.sleep(5)
    try:
        start_now_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn swp_blue font-bold mt-3 btn-curve') and text()='Start Now']"))
        )
        start_now_button.click()
    except:
        pass

    lesson_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h4.title.pb-3.pl-md-5.wrapword.text-bold span")))
    text = lesson_title.text
    print(text)

    try:
        mark_complete_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.mark-complete button.swp_button.swp_pink .text")))
        mark_complete_button.click()
    except:
        pass


    # try:
    #     mark_complete_button = driver.find_element(By.CSS_SELECTOR, "div.mark-complete button.swp_button.swp_pink .text")
    #     mark_complete_button.click()
    # except:
    #     pass

    # Find and click the 'Next' element using CSS selector targeting the text
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "p.theme-cl.text-right.font-bold")
        next_button.click()
    except:
        pass