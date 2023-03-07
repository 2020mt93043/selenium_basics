import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()

# Task - 1
driver.get("https://github.com/login")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='login_field']").send_keys("hello")
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("89hello")
driver.find_element(By.XPATH, "//input[@name='commit']").click()
time.sleep(3)

# Task - 2
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='UserFirstName']").send_keys("John")
driver.find_element(By.XPATH, "//input[@name='UserLastName']").send_keys("wick")
driver.find_element(By.XPATH, "//input[@name='UserEmail']").send_keys("john@gmail.com")
driver.find_element(By.XPATH, "//select[@name='UserTitle']").send_keys("IT Manager")
driver.find_element(By.XPATH, "//input[@name='CompanyName']").send_keys("eInfochips")
driver.find_element(By.XPATH, "//select[@name='CompanyEmployees']").send_keys("101-500")
driver.find_element(By.XPATH, "//select[@name='CompanyCountry']").send_keys("United Kingdom")
driver.find_element(By.XPATH, "//div[@class='msaCheckbox checkboxInput section']//div//div[@class='checkbox-ui']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='start my free trial']").click()
time.sleep(5)