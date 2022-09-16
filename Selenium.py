from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver = Service(r"C:\Users\Lenovo\PycharmProjects\SeleniumTest\Browsers\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver)
#driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
driver.maximize_window()

driver.find_element(By.XPATH,'//a[@href="/selenium-tutorials/how-to-configure-selenium-grid"]').click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//input[@type="email"]')))
driver.find_element(By.XPATH,'//input[@type="email"]').send_keys("karan.js910@gmail.com")
driver.find_element(By.CSS_SELECTOR,'input[type="submit"]').click()
driver.close()
