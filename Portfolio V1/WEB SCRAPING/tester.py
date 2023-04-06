#Yamaha
#agregar fecha
#sacar texto de precios y crear nueva columna adicional
#not found es 0
#crear columna con texto que diga si esta o no el link

import pandas as pd
import requests
import datetime
from bs4 import BeautifulSoup
df = pd.read_excel('LISTADODELINKS_2.xlsx')
data={
"MARCA":[],
"MODELO":[],
"URL":[],
"precio_desde":[],
"legal_bono":[],
"precio_bono":[],
"precio_lista":[],
"fecha_extraccion":[],
}
for ind in df.index:
    lista_captura_precio=[]
    url=df['URL'][ind]
    response=requests.get(url)
    webpage_soup=BeautifulSoup(response.text,features='html.parser')
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
    data["precio_desde"].append(lista_captura_precio[0])
    data["legal_bono"].append(lista_captura_precio[1])
    data["precio_bono"].append(lista_captura_precio[2])
    data["precio_lista"].append(lista_captura_precio[3])
    data["fecha_extraccion"].append(str(datetime.datetime.now()))


df2=pd.DataFrame(data) 
df3=pd.read_csv('Resultado_Webscrapping_Yamaha.csv')
df3=pd.concat([df3, df2])
df3.to_csv('Resultado_Webscrapping_Yamaha.csv',index=False)
print("Finished")


