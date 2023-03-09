import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()

# Task - 1
driver.get("https://www.oracle.com/in/database")
Task - 1
driver.get("https://www.oracle.com/in/database")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@data-lbl='sign-in-account']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Sign-In']").click()
time.sleep(3)
actual_title = driver.title
print("Title", actual_title)
actual_url = driver.current_url
print("URL", actual_url)

driver.find_element(By.XPATH, "//input[@name='ssousername']").send_keys("john")
driver.find_element(By.XPATH, "//input[contains(@title,'Please enter a password')]").send_keys("john123")
driver.find_element(By.XPATH, "//input[contains(@title,'Please click here to sign in')]").click()
time.sleep(3)


# Task - 2

driver.get("https://www.medibuddy.in/")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@data-lbl='sign-in-account']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Sign-In']").click()
time.sleep(3)
actual_title = driver.title
print("Title", actual_title)
actual_url = driver.current_url
print("URL", actual_url)

driver.find_element(By.XPATH, "//input[@name='ssousername']").send_keys("john")
driver.find_element(By.XPATH, "//input[contains(@title,'Please enter a password')]").send_keys("john123")
driver.find_element(By.XPATH, "//input[contains(@title,'Please click here to sign in')]").click()
time.sleep(3)


# Task - 2
driver.get("https://www.medibuddy.in/")
time.sleep(3)
driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
driver.find_element(By.XPATH, "//div[contains(text(),'I have a Corporate Account')]").click()
driver.find_element(By.XPATH, "//div[contains(text(),'Login using Username & Password')]").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter Username']").send_keys("john")
driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("john123")
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()
actual_error_text = driver.find_element(By.XPATH, "//div[@class='alert alert-danger errorTxt']").text
print(actual_error_text)
time.sleep(5)

# Task - 3

driver.get("https://www.online.citibank.co.in/")
driver.find_element(By.XPATH, "//a[@title='Login']").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH, "//div[contains(text(),'Forgot User ID?')]").click()
driver.find_element(By.XPATH, "//a[@class='sbSelector']").click()
driver.find_element(By.LINK_TEXT, "Credit Card").click()
driver.find_element(By.ID, "citiCard1").send_keys("4545")
driver.find_element(By.ID, "citiCard2").send_keys("5656")
driver.find_element(By.ID, "citiCard3").send_keys("8887")
driver.find_element(By.ID, "citiCard4").send_keys("9998")
driver.find_element(By.XPATH, "//input[@name='CCVNO']").send_keys("998")
driver.execute_script("document.querySelector('#bill-date-long').value='14/04/2022'")
# driver.find_element(By.XPATH, "//input[@id='bill-date-long']").send_keys("14/04/2022")
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='colCTA']").click()
print(driver.find_element(By.XPATH, "//li[Contains(text(),'Terms')]").text)
driver.find_element(By.XPATH, "//body/div[3]/div[3]/div[1]/button[1]").click()
time.sleep(5)