#select te genera un conjunto de elementos, cada elemento al interior de este conjunto es html, 
# pero el conjunto en si mismo no es html
import requests
from bs4 import BeautifulSoup

url= "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

response=requests.get(url)

webpage_soup=BeautifulSoup(response.text,features='html.parser')

tabla=webpage_soup.find('table', id="constituents")

cuerpo_tabla= tabla.find('tbody')

a_cuerpo_tabla=cuerpo_tabla.select('a[class="external text"]')

lista_de_symbols=[]

[lista_de_symbols.append(i.text) for i in a_cuerpo_tabla]

print(lista_de_symbols)