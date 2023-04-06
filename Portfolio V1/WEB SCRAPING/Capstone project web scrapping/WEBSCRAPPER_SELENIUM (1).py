import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By




url= "https://www.bmw-motorrad.cl/es/models/roadster/s1000r.html"
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)
time.sleep(5)
xPath='//*[@id="pageMain"]/div/section[2]/div[1]/div[1]/span'
elem = driver.find_elements(By.XPATH, '//*[@id="pageMain"]/section[1]/div[2]/div/div[1]/p')
for i in elem:
    print(i.text)
#driver.close()