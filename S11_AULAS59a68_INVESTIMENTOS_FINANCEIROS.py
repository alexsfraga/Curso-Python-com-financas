# AULA 59 - Investimentos e analise de dados

# AULA 62

#import pip
#pip.main(['install','matplotlib'])

import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

#pg = wb.DataReader('PG',data_source='yahoo',start='1995-01-01',end='2017-03-23')
#pg.to_csv('C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/pg.csv')
#pg = pd.read_csv('C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/pg.csv')
#print(pg.head(),' \n  ---  \n  --- \n ', pg.tail())

print('   ----  pg simple_return ---- >>>>')
#pg['simple_return']= (pg['Adj Close']/pg['Adj Close'].shift(1))-1
#pg.to_csv('C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/pg1.csv')
pg = pd.read_csv('C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/pg1.csv')
#print(pg['simple_return'])
#print(pg)

# AULA 63 -  criando opu plotando um grafico
# taxa simples

#pg['simple_return'].plot(figsize=(5,5))
#plt.show()

print('\n --- taxa simples ou media    -------- »»»» \n')
avg_returns_d = pg['simple_return'].mean()
print(avg_returns_d)

print('\n --- taxa simples ou media anual cerca de 250 dias  -------- »»»» \n')
avg_returns_a = pg['simple_return'].mean()*250
print(avg_returns_a)

print('\n --- taxa simples ou media anual em percentagem  -------- »»»» \n')
print( str(round(avg_returns_a,4) * 100)+' %')



# AULA 64 -- calculando a taxa de retorno ou taxa logaritimica
# construir loops ou vetorizacao com matrizes multidimencionais ou unidimencionais

print('\n --- retorn Logaritimico   -------- »»»» \n')
pg['log_return'] = np.log(pg['Adj Close']/pg['Adj Close'].shift(1))
#print(pg['log_return'])

#pg['log_return'].plot(figsize=(8,5))
#plt.show()

print('\n --- taxa log   -------- »»»» \n')
log_return_a = pg['log_return'].mean()
print(log_return_a)

print('\n --- taxa log anual   -------- »»»» \n')
log_return_a = pg['log_return'].mean() * 250
print(log_return_a)

print('\n --- taxa log anual em percentagem  -------- »»»» \n')
print(str(round(log_return_a,5)*100),' %')

# Aula 65  - Portifolio ou carteira de investimentos
#calcular a taxa de retorno de uma carteira

# funcao para buscar os dados e salvar em csv
def get_tic(param):
    for t in param:
        dtf = wb.DataReader(t,data_source='yahoo',start='1995-01-01', end='2017-03-23')
        dtf.to_csv('C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/' + t + '.csv')

tickers = ['PG','MSFT','F','GE']
#get_tic(tickers)

dt = pd.DataFrame()
for t in tickers:
    #dt[t] = wb.DataReader(t,data_source='yahoo',start='1995-01-01', end='2017-03-23')
    dt[t] = pd.DataFrame(pd.read_csv('C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/'+t+'.csv')).set_index('Date')['Adj Close']

#print(dt.info())
#print('\n - dt.head   »»»»»  \n' ,dt.head())
#print('\n - dt.tail   »»»»»  \n' ,dt.tail())
print('\n - dt   »»»»»  \n' , dt.head(3))

# AULA 66
print('\n --- Normalização e plot  -------- »»»» \n')
#print(dt.iloc[0])
(dt / dt.iloc[0] * 1).plot(figsize =(13,5))

#print(dt.loc['1995-01-05'])
print(dt.iloc(1))
#dt.plot(figsize=(13,6))

#plt.show()

# retorno simples de algumas ações
# como criar uma matriz numpy
print('\n  ---- pesos ---»»»»» \n')
returns = (dt / dt.shift(1))-1
weights = np.array([0.25,0.25,0.25,0.25])
print('\n  - dot ---»»»»» \n',np.dot(returns, weights))
#print(returns.head())

annual_returns = returns.mean()*250

print('\n  - annual retunrs ---»»»»» \n',annual_returns, weights)
print('\n  - annual dot ---»»»»» \n',np.dot(annual_returns, weights))

pfolio1 = str(round(np.dot(annual_returns, weights),5)*100)+' %'
print(pfolio1)

weights2 = np.array([0.4,0.4,0.15,0.05])
pfolio2 = str(round(np.dot(annual_returns, weights2),5)*100) + ' %'
print('\n -- annual returns 2 -- »»» \n'+ pfolio2)

import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import quandl as ql
import matplotlib.pyplot as plt
import xlwt
import xlrd

#dt2 = pd.read_csv('C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/Data_02.csv')
#dt3 = pd.read_excel('C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/Data_03.xlsx')
#print(dt3)

#Aula 67

# alguns indices dos estados unidos
# S&P500 (STANDARD & POOR'S)
# DOWJONES (UM DOS MAIS ANTIGOS) UMA MEDIA DAS 30 MAIORES AÇÕES DO MERCADO NORTE AMERICANO
# NASDAQ (DADOS AGRUPADOS) e(EMPRESAS DE ti), (TAXA DE RETORNO DA EMPRESAS DE TECNOLOGIA)

#INDICES INTERNACIONAIS
# FTSE - REINO UNIDO
# DAX30 - ALEMANHA
# NIKKEI - JAPAO
# SEC - COMPOSIT INDEX CHINA

# AULA 68 - calculando taxas de retorno

def criaCSV(ticket, source, file):
    start = '1995-01-01'
    end = '2017-03-23'
    dtf = wb.DataReader(ticket,data_source=source,)
    dtf.to_csv(file)
    #dtf.close()
    print('csv criado para:'+ticket)

def SalvaEmCSV():
    #tk = ['^GSPC','^IXIC','^GDAXI','^FTSE']
    tk = ['^GSPC','^GDAXI','^IXIC','^FTSE']
    ind_data = pd.DataFrame()
    for t in tk:
        t2 = str(t).replace('^','')
        sf = t2 + '.csv'
        print(t2)
        f= 'C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/'+sf
        print(f)
        if np.os.path.exists(f):
            print('arquivo encontrado')
            ind_data[t2] = pd.DataFrame(pd.read_csv(f)).set_index('Date')['Adj Close']
            print(ind_data[t2])
        else:
            criaCSV(t,'google',f)
            print('nao encontrado')

#ind_returns = (ind_data / ind_data.shift(1))-1
#annual_ind_returns = ind_returns.mean()*250


def f_req2():
    tickets = ['^GSPC','^GDAXI','^IXIC'] #,'^FTSE'
    ind_data = pd.DataFrame()

    for t in tickets:
        ind_data[t]=wb.DataReader(t,data_source='yahoo',start='1997-01-01')['Adj Close']
    #print(ind_data.head())
    (ind_data / ind_data.iloc[0]*100).plot(figsize=(15,6))
    #plt.show()

    ind_ret = (ind_data / ind_data.shift(1))-1
    #print(ind_ret.tail())

    annual_ind_ret = (ind_ret.mean()*250)
    print(annual_ind_ret)

#f_req2()

def freq3():
    tik = ['PG','^GSPC','^DJI']
    data2 = pd.DataFrame()
    for t in tik:
        data2[t] = wb.DataReader(t,data_source='yahoo',start='2007-01-01')['Adj Close']

    print(data2.head())
    (data2 / data2.iloc[0]*100).plot(figsize=(15,6))
    plt.show()

freq3()