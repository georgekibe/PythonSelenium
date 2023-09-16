from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_objj = Service("F:\Staff\Softwares\Drivers\geckodriver-v0.33.0-win64\geckodriver.exe")
driver = webdriver.Firefox(service=serv_objj)

driver.get("https://demo.nopcommerce.com/")
search = driver.find_element(By.ID, "small-searchterms")
search.send_keys("Lenovo")
driver.find_element(By.XPATH, "//button[@class='button-1 search-box-button']").click()
