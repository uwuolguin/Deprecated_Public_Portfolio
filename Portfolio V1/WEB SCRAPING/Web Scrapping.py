#select te genera un conjunto de elementos, cada elemento al interior de este conjunto es html, 
# pero el conjunto en si mismo no es html
import pandas as pd
import requests
import time,os,datetime
from bs4 import BeautifulSoup

def getListOfCompanies():

    url= "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    response=requests.get(url)

    webpage_soup=BeautifulSoup(response.text,features='html.parser')

    tabla=webpage_soup.find('table', id="constituents")

    cuerpo_tabla= tabla.find('tbody')

    a_cuerpo_tabla=cuerpo_tabla.select('a[class="external text"]')

    lista_de_symbols=[]

    [lista_de_symbols.append(i.text) for i in a_cuerpo_tabla]

    return lista_de_symbols


def getFinalcialInformation(symbol):

    nameValue={}
    
    url = "https://finance.yahoo.com/quote/"+symbol+"/"

    response=requests.get(url)

    webpage_soup=BeautifulSoup(response.text,features='html.parser')

    tabla=webpage_soup.find('div', id="quote-summary")
    
    tr_tabla= tabla.select('tr[class*="Bxz(bb) Bdbw"]')
    
    for i in tr_tabla:
        nameValue[i.contents[0].text] = i.contents[1].text
    
    return nameValue
contador=0
while contador < 10:
    
    time.sleep(15)
    
    data={
    "symbol":[],
    "metric":[],
    "value":[],
    "date":[],
    }
    #listOfCompanies=getListOfCompanies()
    listOfCompanies=['MMM','EPAM']


    for i in listOfCompanies:
        for key, value in getFinalcialInformation(i).items():
            data["date"].append(str(datetime.datetime.now()))
            data["symbol"].append(i)
            data["metric"].append(key)
            data["value"].append(value)


    df=pd.DataFrame(data)
    savePath="financial_data.csv"
    if os.path.isfile(savePath):
        df.to_csv(savePath, mode ="a", header= False)
    else:
        df.to_csv(savePath)
    contador+=contador
    print("1 iteracion completa")
