import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://github.com/login")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='login_field']").send_keys("hello")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("89hello")
driver.find_element(By.XPATH, "//input[@name='commit']").click()
time.sleep(3)