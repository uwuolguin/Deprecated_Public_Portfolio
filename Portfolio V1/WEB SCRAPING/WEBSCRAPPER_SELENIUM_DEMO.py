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

url= "https://finance.yahoo.com/chart/EPAM#eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6bnVsbCwiY2FuZGxlV2lkdGgiOjgsImZsaXBwZWQiOmZhbHNlLCJ2b2x1bWVVbmRlcmxheSI6dHJ1ZSwiYWRqIjp0cnVlLCJjcm9zc2hhaXIiOnRydWUsImNoYXJ0VHlwZSI6ImxpbmUiLCJleHRlbmRlZCI6ZmFsc2UsIm1hcmtldFNlc3Npb25zIjp7fSwiYWdncmVnYXRpb25UeXBlIjoib2hsYyIsImNoYXJ0U2NhbGUiOiJsaW5lYXIiLCJwYW5lbHMiOnsiY2hhcnQiOnsicGVyY2VudCI6MSwiZGlzcGxheSI6IkVQQU0iLCJjaGFydE5hbWUiOiJjaGFydCIsImluZGV4IjowLCJ5QXhpcyI6eyJuYW1lIjoiY2hhcnQiLCJwb3NpdGlvbiI6bnVsbH0sInlheGlzTEhTIjpbXSwieWF4aXNSSFMiOlsiY2hhcnQiLCLigIx2b2wgdW5kcuKAjCJdfX0sInNldFNwYW4iOnt9LCJsaW5lV2lkdGgiOjIsInN0cmlwZWRCYWNrZ3JvdW5kIjp0cnVlLCJldmVudHMiOnRydWUsImNvbG9yIjoiIzAwODFmMiIsInN0cmlwZWRCYWNrZ3JvdWQiOnRydWUsImV2ZW50TWFwIjp7ImNvcnBvcmF0ZSI6eyJkaXZzIjp0cnVlLCJzcGxpdHMiOnRydWV9LCJzaWdEZXYiOnt9fSwic3ltYm9scyI6W3sic3ltYm9sIjoiRVBBTSIsInN5bWJvbE9iamVjdCI6eyJzeW1ib2wiOiJFUEFNIiwicXVvdGVUeXBlIjoiRVFVSVRZIiwiZXhjaGFuZ2VUaW1lWm9uZSI6IkFtZXJpY2EvTmV3X1lvcmsifSwicGVyaW9kaWNpdHkiOjEsImludGVydmFsIjoiZGF5IiwidGltZVVuaXQiOm51bGwsInNldFNwYW4iOnt9fV0sInN0dWRpZXMiOnsi4oCMdm9sIHVuZHLigIwiOnsidHlwZSI6InZvbCB1bmRyIiwiaW5wdXRzIjp7ImlkIjoi4oCMdm9sIHVuZHLigIwiLCJkaXNwbGF5Ijoi4oCMdm9sIHVuZHLigIwifSwib3V0cHV0cyI6eyJVcCBWb2x1bWUiOiIjMDBiMDYxIiwiRG93biBWb2x1bWUiOiIjZmYzMzNhIn0sInBhbmVsIjoiY2hhcnQiLCJwYXJhbWV0ZXJzIjp7IndpZHRoRmFjdG9yIjowLjQ1LCJjaGFydE5hbWUiOiJjaGFydCIsInBhbmVsTmFtZSI6ImNoYXJ0In19fX0-"
options = Options()
#options=webdriver.ChromeOptions()
#options.add_argument("headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)
#time.sleep(3)
loadtime=300
wait= WebDriverWait(driver,loadtime)
#time.sleep(5)
# driver.implicitly_wait(30)
saveEveryXTime=10
while True:
    time.sleep(saveEveryXTime)
    try:    
        for i in range(1,6):
            xPath_interno_para_que_se_demore_mas='//*[@id="data-util-col"]/section[2]/table/tbody/tr['+str(i)+']/td[2]/p'
            xPath='//*[@id="data-util-col"]/section[2]/table/tbody/tr['+str(i)+']'
            wait.until(ec.visibility_of_all_elements_located((By.XPATH, xPath_interno_para_que_se_demore_mas)))
            elem = driver.find_elements(By.XPATH, xPath)
            for i in elem:
                texto=''
                for x in i.text.split('\n'):
                    texto=texto+x+','
                texto=texto+str(datetime.datetime.now())
                if os.path.isfile('savefile.txt'):
                    with open("savefile.txt","a") as out:
                        out.write(texto)
                        out.write('\n') 
                else:
                    with open("savefile.txt","w") as out:
                        out.write('a,b,c,fecha')
                        out.write('\n')
            
            
        for i in range(1,6):
            xPath_interno_para_que_se_demore_mas='//*[@id="data-util-col"]/section[2]/table/tbody/tr['+str(i)+']/td[2]/p'
            xPath='//*[@id="data-util-col"]/section[2]/table/tbody/tr['+str(i)+']'+'/td[1]/a'
            wait.until(ec.visibility_of_all_elements_located((By.XPATH, xPath_interno_para_que_se_demore_mas)))
            elem = driver.find_elements(By.XPATH, xPath)
            for i in elem:
                texto=i.get_attribute("href")+','
                texto=texto+str(datetime.datetime.now())
                if os.path.isfile('savelinks.txt'):
                    with open("savelinks.txt","a") as out:
                        out.write(texto)
                        out.write('\n') 
                else:
                    with open("savelinks.txt","w") as out:
                        out.write('Links-Fecha')
                        out.write('\n')                   
    except:
        print("Fallo")
#driver.close()