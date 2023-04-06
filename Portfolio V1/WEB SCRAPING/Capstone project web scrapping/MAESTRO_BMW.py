# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:55:47 2023

@author: ignac
"""
def bmw():
    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    import time
    import datetime

    df = pd.read_excel(r'C://Users/SCT05060/OneDrive - Honda/Escritorio/Alumnos Practicas/2W_WebScraping/URL_MOTOS.xlsx', engine='openpyxl',  sheet_name=[ 'BMW','YAMAHA','BAJAJ','SUZUKI',], skiprows=0)

    bmw= df["BMW"]
    marca= bmw["MODELO"]
    BMW_LISTA={
    "MARCA":[],
    "MODELO":[],
    "URL":[],
    "PRECIO_LISTA":[],
    "PRECIO_BONO":[],
    "FECHA_EXTRACCION":[],
    }
    for i in bmw.index:
        print(i)
        
        try:
            url =bmw['URL'][i]
            options = Options()
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(url)
            time.sleep(8)
            try:
                if url == "https://www.bmw-motorrad.cl/es/models/tour/k1600gtl.html" or url == 'https://www.bmw-motorrad.cl/es/models/tour/k1600gt.html':
                    xpath= '//*[@id="pageMain"]/section[1]/div[2]/div/div[1]/p/span[2]/b/span'
                    xpath2= '//*[@id="pageMain"]/section[1]/div[2]/div/div[1]/p'

                    elem = driver.find_elements(By.XPATH, xpath)
                    elem2 = driver.find_elements(By.XPATH, xpath2)
                    captura_precio=( str(elem[0].text)).replace("$","").replace("*","").replace(" .","")
                    captura_precio2=(str(elem2[0].text.split('\n')[1].split('$')[1])).replace("$","").replace("*","").replace(" .","")

                
                else:
                    xpath= '//*[@id="pageMain"]/section[1]/div[2]/div/div[1]/p/span/b/span'
                    xpath2= '/html/body/main/section[1]/div[2]/div/div[1]/p'

                    elem = driver.find_elements(By.XPATH, xpath)
                    elem2 = driver.find_elements(By.XPATH, xpath2)
                    captura_precio= str(elem[0].text).replace("$","").replace("*","").replace(" .","")
                    captura_precio2= str(elem2[0].text.split('\n')[0].split('$')[1].split('*')[0]).replace("$","").replace("*","").replace(" .","")


                

                BMW_LISTA["MARCA"].append(bmw['MARCA'][i])
                BMW_LISTA["MODELO"].append(bmw['MODELO'][i])
                BMW_LISTA["URL"].append(bmw['URL'][i])
                BMW_LISTA["PRECIO_LISTA"].append(captura_precio2)
                BMW_LISTA["PRECIO_BONO"].append(captura_precio)
                BMW_LISTA["FECHA_EXTRACCION"].append(str(datetime.datetime.now()))
                    
            except:
                
                BMW_LISTA["MARCA"].append(bmw['MARCA'][i])
                BMW_LISTA["MODELO"].append(bmw['MODELO'][i])
                BMW_LISTA["URL"].append(bmw['URL'][i])
                BMW_LISTA["PRECIO_LISTA"].append("0")
                BMW_LISTA["PRECIO_BONO"].append("0")
                BMW_LISTA["FECHA_EXTRACCION"].append(str(datetime.datetime.now()))             
            

        except:
            
            BMW_LISTA["MARCA"].append(bmw['MARCA'][i])
            BMW_LISTA["MODELO"].append(bmw['MODELO'][i])
            BMW_LISTA["URL"].append(bmw['URL'][i])
            BMW_LISTA["PRECIO_LISTA"].append("0")
            BMW_LISTA["PRECIO_BONO"].append("0")
            BMW_LISTA["FECHA_EXTRACCION"].append(str(datetime.datetime.now()))   
            print(BMW_LISTA)
    df2=pd.DataFrame(BMW_LISTA) 
    df3=pd.read_csv('MAESTRO_BMW.csv')
    df3=pd.concat([df3, df2])
    df3.to_csv('MAESTRO_BMW.csv',index=False)
    print("Finished")
        
if __name__ == "__main__":
    bmw()




    #YAMAHA













