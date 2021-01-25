# Aula 46 - importanto modulos
# importanto modulos de bibliotecas existentes no python
import math

print((math.sqrt(20)).__round__(2))

from math import sqrt
print((sqrt(36)).__round__(2))

# renomear modulos
import math as m
print((m.sqrt(49)).__round__(2))

from math import *
print((sqrt(64)).__round__(2))

# listando informações sobre o modulo math
# help(math)

# Aula 47 - numpy

# instalando pacote no PyCharm
# https://stackoverflow.com/questions/46922260/pycharm-pandas-datareader-not-found
# import pip
# pip.main(['install', 'pandas_datareader'])
# pip.main(['install', 'matplotlib'])
# import pip
# pip.main(['install', 'pandas_datareader'])

# Aula 48  -  Arrays
# array todos os elementos deve ser do mesmo tipo de dados
# e na lista podemos ter tipos de dados diferentes
print("    ---  AULA 48   ---    ")
import numpy as np
a = np.array([[0,1,2,3],[4,5,6,7]])
# print(a)
# print(a.shape)

# print(a[1,3])

a[1,2]=8
# print(a)

# print(a[0])
# print(a[1])

b = np.array([3,5])
# print(b)

# Aula 49 - gerando numeros aleatorios
print("    ---  AULA 49   ---    ")
import random
prob = random.random()
# print(prob)

number = random.randint(1,6)
# print(number)
print(random.randint(1,6))
print("    ---     ---    ")
print(np.random.randint(1,6,(4,6)))

# Aula 52 --
print("    ---  AULA 52   ---    ")
# instalando pacote jupter
# pip.main(['install', 'jupyterlab'])
# pip install jupyterlab
# import jupyterlab
 #pip(['uninstall', 'pandas_datareader'])
# AULA 53 ---
import pandas as pd
ser = pd.Series(np.random.random(5), name = "Column 01")
print(ser)
print(ser[0])
print(ser[1])
print(ser[2])

from pandas_datareader import data as wb
import pandas_datareader as web
from pandas_datareader.iex.stats import DailySummaryReader as wiex
pg2 = web.DataReader('PG', data_source='iex' ,start='2020-1-1')
#PG = web.DataReader('PG', 'iex',start,end)
#CCRO3SA = wb.DataReader('CCRO3.SA', data_source='iex',start='2000-1-1')
#PETR4 = wb.DataReader('PETR4', data_source='yahoo',start='2000-1-1')
#print(pg2)
#print(CCRO3SA.head())
#print('\n\n   -----   PG     -----\n',CCR3SA)
#print('\n\n   -----   PG     -----\n',PETR4)
#tickers = ['PG','GE','T']
#new_data = pd.DataFrame()
#for t in tickers:
#    new_data[t] = wb.DataReader(t, data_source='yahoo',start='2020-1-1')['Adj Close']
#print(new_data.head())
#https://medium.com/@cesar.vieira/analisando-a%C3%A7%C3%B5es-da-bovespa-parte-i-500107703688

# AULA 55 -- MORNINGSTAR OU IEX OU YAHOO
# IEX SO FORNECE DADOS DOS ULTIMOS 5 ANOS EM RELAÇÃO A DATA ESPECIFICADA NO CODIGO
import pandas as pd
from pandas_datareader import data as wb
tickers = ['PG']
new_data2 = pd.DataFrame()
for ind in tickers:
    new_data2[ind] = wb.DataReader(ind, data_source='yahoo',start='2000-1-1')['Adj Close']

print(new_data2.head())


tickers2 = ['PG','MSFT','T','F','GE']
new_data3 = pd.DataFrame()
for ind in tickers2:
    new_data3[ind] = wb.DataReader(ind, data_source='yahoo',start='2015-01-01')['Adj Close']
print(new_data3.head())


 # AULA 56 -- importando dados com o quandl

import quandl as ql
import pandas as pd

dt1 = ql.get("FRED/GDP")
print(dt1.head())

dt1.to_csv('C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/ex1.csv')

dt2 = pd.read_csv('C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/Data_02.csv')
print(dt2.head(5))

# pacote nescessario para poder salvar e trabalhar com arquivos do excel
# o " xlwt "  e  o  " wlrd "
import xlwt
import xlrd

dt2.to_excel(excel_writer='C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/exemplo_2.xls')
# salvando sem indice
#dt2.to_excel(excel_writer='C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/ex2.xls',index=False)

dt3 = pd.read_excel('C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/Data_03.xlsx')
print(dt3)


#Aula 57 -- salvando e lendo arquivos csv e excel
print('\n   -------   outro bloco de codigo  --------  \n')

dt4 = pd.read_csv('C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/Data_02.csv',index_col='Date')
print(dt4)
#alterando o indice de busca alternativo sem alterar o objeto
print(dt3.set_index('Year'))

#alterando o indice no objeto
dt5 = dt3.set_index('Year')
print(dt5)

# AULA 58 --








