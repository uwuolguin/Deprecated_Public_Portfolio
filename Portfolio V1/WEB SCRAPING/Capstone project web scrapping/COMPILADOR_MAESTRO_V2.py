import pandas as pd

import MAESTRO_YAMAHA
import MAESTRO_BAJAJ
import MAESTRO_SUZUKI
import MAESTRO_BMW

MAESTRO_YAMAHA.yamaha()
MAESTRO_BAJAJ.bajaj()
MAESTRO_SUZUKI.suzuki()
MAESTRO_BMW.bmw()

df2=pd.read_csv('MAESTRO_BAJAJ.csv')
df1=pd.read_csv('MAESTRO_SUZUKI.csv')
df=pd.read_csv('Resultado_Webscrapping_Yamaha.csv')
df3=pd.read_csv('MAESTRO_BMW.csv')

df=pd.concat([df,df1,df2,df3])
df.to_csv('MAESTRO.csv',index=False)
print('fin')