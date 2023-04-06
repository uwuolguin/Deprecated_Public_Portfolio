# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:04:22 2023

@author: ignac
"""
def yamaha():

    import pandas as pd
    import requests
    import datetime
    import time
    from bs4 import BeautifulSoup

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager


    pf = pd.read_excel(r'C://Users/SCT05060/OneDrive - Honda/Escritorio/Alumnos Practicas/2W_WebScraping/URL_MOTOS.xlsx', engine='openpyxl',  sheet_name=[ 'BMW','YAMAHA','BAJAJ','SUZUKI',], skiprows=0)
    df= pf['YAMAHA']
    data={
    "MARCA":[],
    "MODELO":[],
    "URL":[],
    "PRECIO_DESDE":[],
    "legal_bono":[],
    "PRECIO_BONO":[],
    "PRECIO_LISTA":[],
    "FECHA_EXTRACCION":[],
    }
    for ind in df.index:
        lista_captura_precio=[]
        url=df['URL'][ind]
        response=requests.get(url)
        webpage_soup=BeautifulSoup(response.text,features='html.parser')
        time.sleep(1)

        if  url == 'https://www.yamahamotos.cl/producto/xtz150/':
            try:
                options = Options()
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                driver.get(url)
                xpath= '//*[@id="product-12650"]/div[1]/div[2]/div[1]/p/span'
                elem = driver.find_elements(By.XPATH, xpath)
                lista_captura_precio.append(str(elem[0].text).replace('$','').replace('precio de lista',''))
                print(lista_captura_precio)
                
            except:
                lista_captura_precio.append('0')
            lista_captura_precio.append('0')        
            try:
                options = Options()
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                driver.get(url)
                xpath= '//*[@id="product-12650"]/div[1]/div[2]/div[1]/p/span'
                elem =driver.find_elements(By.XPATH, xpath)
                lista_captura_precio.append(str(elem[0].text).replace('$','').replace('precio de lista',''))
                print(lista_captura_precio)
            except:
                precio_bono_yamaha='0'
                lista_captura_precio.append(precio_bono_yamaha)
            try:
                options = Options()
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                driver.get(url)
                xpath= '//*[@id="product-12650"]/div[1]/div[2]/div[1]/div[1]'
                elem = driver.find_elements(By.XPATH, xpath)
                lista_captura_precio.append(str(elem[0].text).replace('$','').replace('precio de lista',''))
                print(lista_captura_precio)
                
            except:
                    precio_lista='0' 
                    lista_captura_precio.append(precio_lista)
                        
        elif url == 'https://www.yamahamotos.cl/producto/fzn150/' :
            try:
                options = Options()
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                driver.get(url)
                xpath= '//*[@id="product-20"]/div[1]/div[2]/div[1]/p/span'
                elem = driver.find_elements(By.XPATH, xpath)
                lista_captura_precio.append(str(elem[0].text).replace('$','').replace('precio de lista',''))
                print(lista_captura_precio)
                
            except:
                lista_captura_precio.append('0')
            lista_captura_precio.append('0')
            try:
                options = Options()
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                driver.get(url)
                xpath= '//*[@id="product-20"]/div[1]/div[2]/div[1]/p/span'
                elem = driver.find_elements(By.XPATH, xpath)
                lista_captura_precio.append(str(elem[0].text).replace('$','').replace('precio de lista',''))
                print(lista_captura_precio)
            except:
                precio_bono_yamaha='0'
                lista_captura_precio.append(precio_bono_yamaha)
            try:
                options = Options()
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                driver.get(url)
                xpath= '//*[@id="product-20"]/div[1]/div[2]/div[1]/div[1]'
                elem = driver.find_elements(By.XPATH, xpath)
                lista_captura_precio.append(str(elem[0].text).replace('$','').replace('precio de lista',''))
                print(lista_captura_precio)
                
            except:
                    precio_lista='0' 
                    lista_captura_precio.append(precio_lista)            
        else:
            print('normal')
            try:
                contenedor_precio_desde=webpage_soup.select('div[class="et_pb_module et_pb_wc_price et_pb_wc_price_0"]')
                precio_desde=contenedor_precio_desde[0].select('span[class="woocommerce-Price-amount amount"]')
                lista_captura_precio.append(precio_desde[0].contents[1].text)
            except:
                lista_captura_precio.append('0')
            try:
                contenedor_precio_full_1=webpage_soup.select('div[class="et_pb_module et_pb_code et_pb_code_1"]')
                contenedor_precio_full_2=contenedor_precio_full_1[0].select('div[class="et_pb_code_inner"]')
                try:
                    legal_bono=(contenedor_precio_full_2[0].select('div[class="legal-bono"]')[0]).text.split("$")[1]
                    lista_captura_precio.append(legal_bono)
                except:
                    legal_bono='0'
                    lista_captura_precio.append(legal_bono)
                try:
                    precio_bono_yamaha=(contenedor_precio_full_2[0].select('div[class="precio-bono-yamaha"]')[0]).text.split(" ")[0].split("$")[1]
                    lista_captura_precio.append(precio_bono_yamaha)
                except:
                    precio_bono_yamaha='0'
                    lista_captura_precio.append(precio_bono_yamaha)
                try:
                    precio_lista=(contenedor_precio_full_2[0].select('div[class="precio-lista"]')[0]).text.split(" ")[0].split("$")[1]
                    lista_captura_precio.append(precio_lista)
                except:
                    precio_lista='0' 
                    lista_captura_precio.append(precio_lista)
            except:
                lista_captura_precio.append('0')
                lista_captura_precio.append('0')
                lista_captura_precio.append('0')
        
        data["MARCA"].append(df['MARCA'][ind])
        data["MODELO"].append(df['MODELO'][ind])
        data["URL"].append(df['URL'][ind])
        data["PRECIO_DESDE"].append(lista_captura_precio[0])
        data["legal_bono"].append(lista_captura_precio[1])
        data["PRECIO_BONO"].append(lista_captura_precio[2])
        data["PRECIO_LISTA"].append(lista_captura_precio[3])
        data["FECHA_EXTRACCION"].append(str(datetime.datetime.now()))


    df2=pd.DataFrame(data) 
    df3=pd.read_csv('Resultado_Webscrapping_Yamaha.csv')
    df3=pd.concat([df3, df2])
    df3.to_csv('Resultado_Webscrapping_Yamaha.csv',index=False)
    print("Finished")

if __name__ == "__main__":
    yamaha()
