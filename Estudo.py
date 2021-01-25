import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import quandl as ql
import matplotlib.pyplot as plt
import sitefinancas as sf

#Aula 69 a 71 Calculos de Media e desvio padrão

#tik = ['PG', 'BEI.DE']
#result = con.RequestList(tk,'2020-01-01')
#data2 = pd.DataFrame()
#for t in tik:
#    data2[t] = wb.DataReader(t, data_source='yahoo', start='2007-01-01')['Adj Close']
con = sf.ConWeb()
#tk = ['^PETR4','^USDBRL=X','^DJI']
x = 'PETR4.SA'
y = 'BRL=x'
#y = 'BEI.DE'
vdata = '2017-01-01'
tk = [x, y]
data2 = con.RequestList(tk,vdata)

def f3():
    #print(data2.head())
    #(data2 / data2.iloc[0]*100).plot(figsize=(15,6))
    #plt.show()

    tab2 = np.log(data2 / data2.shift(1))
    #print(tab2)

    print(tab2['PG'].mean())
    print(tab2['PG'].mean() * 250)
    print(tab2['PG'].std())
    print(tab2['PG'].std() * 250 ** 0.5)
    print('  ---  ---  ')
    print(tab2['BEI.DE'].mean())
    print(tab2['BEI.DE'].mean() * 250)
    print(tab2['BEI.DE'].std())
    print(tab2['BEI.DE'].std() * 250 **0.5)
    print(' mean ---  --- std ')
    #obtendo a MEdia e a Volatilidade
    print(tab2[['PG','BEI.DE']].mean() * 250)
    print(tab2[['PG', 'BEI.DE']].std() * 250 ** 0.5)

#f3()

#Aula 72,73 e 74 calculando Covariancia e Correlação

# matriz de covariancia
sec_returns = data2
sec_returns[[x,y]].mean() * 250

x_var = sec_returns[x].var()
y_var = sec_returns[y].var()

x_var_a = sec_returns[x].var() * 250
y_var_a = sec_returns[y].var() * 250

print(x_var,"\n",y_var)
print(x_var,"\n",y_var_a)

cov_matrix = sec_returns.cov()
print(cov_matrix)

cov_matrix_a = sec_returns.cov() * 250
print(cov_matrix_a)

corr_matrix = sec_returns.corr()
print(corr_matrix)

#AULA 76

wg = np.array([0.5,0.5])
#varianca do portifolio
pfolio_var = np.dot(wg.T,np.dot(sec_returns.cov() * 250, wg))
print(pfolio_var)

#portifolio Volatility
pfolio_vol = (np.dot(wg.T,np.dot(sec_returns.cov() * 250 , wg)))**0.5
print(pfolio_vol)
print(str(round(pfolio_vol, 5) * 100) + '%')