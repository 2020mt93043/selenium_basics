import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()

driver.get("https://www.oracle.com/in/database")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@data-lbl='sign-in-account']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Sign-In']").click()
time.sleep(3)
actual_title = driver.title
print(actual_title)
actual_url = driver.current_url
print(actual_url)
actual_header = driver.header
print(actual_header)

driver.find_element(By.XPATH, "//input[@name='ssousername']").send_keys("john")
driver.find_element(By.XPATH, "//input[contains(@title,'Please enter a password')]").send_keys("john123")
driver.find_element(By.XPATH, "//input[contains(@title,'Please click here to sign in')]").click()