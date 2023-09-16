from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("F:\Staff\Softwares\Drivers\geckodriver-v0.33.0-win64\geckodriver.exe")

driver = webdriver.Firefox(service=serv_obj)

driver.get("https://www.facebook.com/")

driver.quit()