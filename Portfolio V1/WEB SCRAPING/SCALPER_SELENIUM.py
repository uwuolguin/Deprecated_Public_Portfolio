import time
import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

url= "https://www.pcfactory.cl/producto/47808-sapphire-video-amd-pulse-rx-7900xt-20gb-gddr6-dual-hdmi-dual-dp"
options = Options()
options.add_experimental_option("detach", True)
#options=webdriver.ChromeOptions()
#options.add_argument("headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

loadtime=300
wait= WebDriverWait(driver,loadtime)


xPath_interno_para_que_se_demore_mas='//*[@id="app"]/div[6]/div[2]/div[2]/div[1]/a[1]/h5[1]'
xPath='//*[@id="addtocart_47808_1"]'
wait.until(ec.visibility_of_all_elements_located((By.XPATH, xPath_interno_para_que_se_demore_mas)))
add_to_cart_button = driver.find_elements(By.ID, "addtocart_47808_1")
add_to_cart_button[0].click()
time.sleep(1)
pay_button = driver.find_elements(By.ID, "pagar_ahora")
pay_button[0].click()
time.sleep(1)
guest_button = driver.find_elements(By.ID, "btn_invitado")
guest_button[0].click()
time.sleep(1)
guest_button = driver.find_elements(By.ID, "accordion2")
guest_button[0].click()
time.sleep(1)
Direccion_input=driver.find_elements(By.ID, "autocomplete")
Direccion_input[0].send_keys("LOS ARRAYANES 098")
