from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("F:\Staff\Softwares\Drivers\geckodriver-v0.33.0-win64\geckodriver.exe")
driver = webdriver.Firefox(service=serv_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

tags = driver.find_element(By.TAG_NAME, "a")

print(tags.get_attribute())

driver.close()
