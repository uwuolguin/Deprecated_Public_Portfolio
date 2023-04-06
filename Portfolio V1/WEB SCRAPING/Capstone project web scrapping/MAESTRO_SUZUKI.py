# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:13:25 2023

@author: ignac
"""
def suzuki():

    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    import time
    import datetime

    df = pd.read_excel(r'C://Users/SCT05060/OneDrive - Honda/Escritorio/Alumnos Practicas/2W_WebScraping/URL_MOTOS.xlsx', engine='openpyxl',  sheet_name=[ 'BMW','YAMAHA','BAJAJ','SUZUKI',], skiprows=0)
    SUZUKI= df["SUZUKI"]
    marca= SUZUKI["MODELO"]
    SUZUKI_LISTA={
    "MARCA":[],
    "MODELO":[],
    "URL":[],
    "PRECIO_LISTA":[],
    "FECHA_EXTRACCION":[],
    }

    for i in SUZUKI.index:
        print(i)
        try:
            url =SUZUKI['URL'][i]
            options = Options()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(url)
            time.sleep(2)
            
            try:
                
                xpath= '//*[@id="moto_autofin"]/div/div[1]/h4[1]/small'
                elem = driver.find_elements(By.XPATH, xpath)
                captura_precio= str(elem[0].text).split("$")[1]
                print(captura_precio)

                
                SUZUKI_LISTA["MARCA"].append(SUZUKI['MARCA'][i])
                SUZUKI_LISTA["MODELO"].append(SUZUKI['MODELO'][i])
                SUZUKI_LISTA["URL"].append(SUZUKI['URL'][i])
                SUZUKI_LISTA["PRECIO_LISTA"].append(captura_precio)
                SUZUKI_LISTA["FECHA_EXTRACCION"].append(str(datetime.datetime.now()))
                    
            except:
                
                SUZUKI_LISTA["MARCA"].append(SUZUKI['MARCA'][i])
                SUZUKI_LISTA["MODELO"].append(SUZUKI['MODELO'][i])
                SUZUKI_LISTA["URL"].append(SUZUKI['URL'][i])
                SUZUKI_LISTA["PRECIO_LISTA"].append("no encontrado")
                SUZUKI_LISTA["FECHA_EXTRACCION"].append(str(datetime.datetime.now()))             
            

        except:
            
            SUZUKI_LISTA["MARCA"].append(SUZUKI['MARCA'][i])
            SUZUKI_LISTA["MODELO"].append(SUZUKI['MODELO'][i])
            SUZUKI_LISTA["URL"].append(SUZUKI['URL'][i])
            SUZUKI_LISTA["PRECIO_LISTA"].append("no encontrado")
            SUZUKI_LISTA["FECHA_EXTRACCION"].append(str(datetime.datetime.now()))   

    df2=pd.DataFrame(SUZUKI_LISTA) 
    df3=pd.read_csv('MAESTRO_SUZUKI.csv')
    df3=pd.concat([df3, df2])
    df3.to_csv('MAESTRO_SUZUKI.csv',index=False)
    print("Finished")
if __name__ == "__main__":
    suzuki()
    
 
