# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:18:50 2023

@author: ignac
"""

def bajaj():

    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    import time
    import datetime

    df = pd.read_excel(r'C://Users/SCT05060/OneDrive - Honda/Escritorio/Alumnos Practicas/2W_WebScraping/URL_MOTOS.xlsx', engine='openpyxl',  sheet_name=[ 'BMW','YAMAHA','BAJAJ','SUZUKI',], skiprows=0)
    BAJAJ= df["BAJAJ"]
    marca= BAJAJ["MODELO"]
    BAJAJ_LISTA={
    "MARCA":[],
    "MODELO":[],
    "URL":[],
    "PRECIO_LISTA":[],
    "FECHA_EXTRACCION":[],
    }

    for i in BAJAJ.index:
        print(i)
        try:
            url =BAJAJ['URL'][i]
            options = Options()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(url)
            time.sleep(8)
            
            try:
                if url == "https://motochile.cl/pulsar-ns160/":
                    xpath= '//*[@id="slider-cosmetics"]/rs-slides/rs-slide/rs-layer-wrap[6]/rs-loop-wrap/rs-mask-wrap'
                    elem = driver.find_elements(By.XPATH, xpath)
                    captura_precio= str(elem[0].text).replace('$','')
                    
        
                    
                    BAJAJ_LISTA["MARCA"].append(BAJAJ['MARCA'][i])
                    BAJAJ_LISTA["MODELO"].append(BAJAJ['MODELO'][i])
                    BAJAJ_LISTA["URL"].append(BAJAJ['URL'][i])
                    BAJAJ_LISTA["PRECIO_LISTA"].append(captura_precio)
                    BAJAJ_LISTA["FECHA_EXTRACCION"].append(str(datetime.datetime.now()))
                    
                    
                elif url == "https://motochile.cl/pulsar-ns125/":   
                    xpath= '//*[@id="slider-cosmetics"]/rs-slides/rs-slide/rs-layer-wrap[2]/rs-loop-wrap/rs-mask-wrap'

                    elem = driver.find_elements(By.XPATH, xpath)
                    captura_precio= str(elem[0].text).replace('$','')
                    
                    
                else:
                    xpath= '//*[@id="slider-cosmetics"]/rs-slides/rs-slide/rs-layer-wrap/rs-loop-wrap/rs-mask-wrap/rs-layer'
                    elem = driver.find_elements(By.XPATH, xpath)
                    captura_precio= str(elem[0].text).replace('$','')
                    
                    
                    
                BAJAJ_LISTA["MARCA"].append(BAJAJ['MARCA'][i])
                BAJAJ_LISTA["MODELO"].append(BAJAJ['MODELO'][i])
                BAJAJ_LISTA["URL"].append(BAJAJ['URL'][i])
                BAJAJ_LISTA["PRECIO_LISTA"].append(captura_precio)
                BAJAJ_LISTA["FECHA_EXTRACCION"].append(str(datetime.datetime.now()))
                    
            except:
                
                BAJAJ_LISTA["MARCA"].append(BAJAJ['MARCA'][i])
                BAJAJ_LISTA["MODELO"].append(BAJAJ['MODELO'][i])
                BAJAJ_LISTA["URL"].append(BAJAJ['URL'][i])
                BAJAJ_LISTA["PRECIO_LISTA"].append("no encontrado")
                BAJAJ_LISTA["FECHA_EXTRACCION"].append(str(datetime.datetime.now()))             
            

        except:
            
            BAJAJ_LISTA["MARCA"].append(BAJAJ['MARCA'][i])
            BAJAJ_LISTA["MODELO"].append(BAJAJ['MODELO'][i])
            BAJAJ_LISTA["URL"].append(BAJAJ['URL'][i])
            BAJAJ_LISTA["PRECIO_LISTA"].append("no encontrado")
            BAJAJ_LISTA["FECHA_EXTRACCION"].append(str(datetime.datetime.now()))   

    df2=pd.DataFrame(BAJAJ_LISTA) 
    df3=pd.read_csv('MAESTRO_BAJAJ.csv')
    df3=pd.concat([df3, df2])
    df3.to_csv('MAESTRO_BAJAJ.csv',index=False)
    print("Finished")
if __name__ == "__main__":
    bajaj()