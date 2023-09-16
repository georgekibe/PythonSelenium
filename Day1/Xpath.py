from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("F:\Staff\Softwares\Drivers\geckodriver-v0.33.0-win64\geckodriver.exe")
driver = webdriver.Firefox(service=serv_obj)

driver.get("https://orangehrm.com/")
#driver.find_element(By.XPATH, '/html[1]/body[1]/nav[1]/div[1]/div[2]/div[2]/ul[1]/li[2]/a[1]/button[1]').click()
#driver.find_element(By.XPATH, '/html/body/nav/div/div[2]/div[2]/ul/li[2]/a/button').click()
driver.find_element(By.XPATH, "/html/body/div[3]/div/div/section/div/div/div/div/div/div/form/fieldset/div/div/input").send_keys("testtest")

