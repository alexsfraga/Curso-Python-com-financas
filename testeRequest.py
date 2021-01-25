#https://blog.restcase.com/4-most-used-rest-api-authentication-methods/
#https://stackoverflow.com/questions/19069701/python-requests-library-how-to-pass-authorization-header-with-single-token

'''
# teste request B3
import requests
url = "https://api-marketdata-sandbox.b3.com.br/api/trade/v1.0/TradeInformation?SessionStartDate=2020-01-01&SessionEndDate=2020-01-24&Symbol=WEGE3&ItemsPerPage=1"
payload = {}
headers = {
  'KeyId': '73d90e13-c4cb-4b5f-acd6-7f3d89ce7d8b',
  #'Cookie': 'TS01871345=019a3dd3c1d1d1d27faed90c1b4cb2070b0ddd2a2f9e6948d6c9157ded89d75aeb77c6308db775a07573af4044ee79a81446f70469'
}
response = requests.request("GET", url, headers=headers, data = payload, verify=False).json()
#print(response.text.encode('utf8'))
dt1 = response['Data']
dt2 = dt1[0]
#print(response['Data'])
#for i in response['Data']:
tk = {}
tk = {'Ticket':dt2['InstrumentSymbol']}
print(tk)
print(dt2)
'''


import pip
#pip.main(['install','pandas'])
#pip.main(['install','numpy'])
#pip.main(['install','cx_Oracle'])



import conectaBD as bd


#pip.main(['install','pandas_datareader'])
def f_req2():
    import pandas as pd
    import numpy as np
    from pandas_datareader import data as wb
    #import matplotlib.pyplot as plt

    pg = wb.DataReader('PG',data_source='yahoo',start='1995-01-01',end='2017-03-23')
    print(pg)


def f_request(tk):
    import requests
    API_URL = "https://www.alphavantage.co/query"
    myAPIKey = 'OTGYTHIMBWAK650C'
    tiket = tk #'WEGE3.SA'
    # "AAPL"
    data = {
        #"function": "TIME_SERIES_DAILY",
        "function": 'TIME_SERIES_DAILY_ADJUSTED',
        "symbol": tiket,
        "outputsize": "compact",
        "apikey": myAPIKey
        }
    #print(data)
    response = requests.get(API_URL, params=data).json()
    #print(response)
    cota = response['Time Series (Daily)']
    #print(" print cota »»»»» \n",cota)
    return cota

def f_parse(cota):
    #cota = f_request()
    n = []
    for t in cota:
        #print(cota)
        obj = {}
        var1 = list(cota)[list(cota).index(t)]
        #print(var1)
        var2 = cota[t]
        #print(var2)
        obj['data'] = var1
        #print(obj)
        for i in var2:
            var3 = list(var2)[list(var2).index(i)]
            var3 = var3[3:]
            var3 = var3.replace(' ','_')
            var4 = var2[i]
            #var4 = var4.replace(''','"')
            obj[var3] = var4
        n.append(obj)
    print(n)
    return n

cota = f_request("WEGE3.SA")
list = f_parse(cota)



#bd.select("select sigla, tipo, bolsa, pais from acoes where sigla='WEGE3.SA'")


#bd.insertCotacoes(1,list)
#bd.insertToBd("PG","ON","NYSE")
#bd.insertToBd("WEGE3.SA","ON","B3")
#bd.insertToBd("CCRO3.SA","ON","B3")
#bd.insertToBd("EGIE3.SA","ON","B3")



dic2 = {'data': "2020-10-23",
     'open': '82.2500'}
dic = {
     'data': '2020-10-23',
     'open': '82.2500',
     'high': '83.2600',
     'low': '80.6400',
     'close': '81.6700',
     'adj_close': '81.6700',
     'volume': '8068300',
     'div_amount': '0.0000',
     'split_coef': '1.0',
     }
#for p_data, p_open, p_high, p_low, p_close, p_adj_close, p_volume, p_dividend_amount, p_split in dic.keys():
    #print(p_data, p_open, p_high, p_low, p_close, p_adj_close, p_volume, p_dividend_amount, p_split)

#for p_data, p_open in dic2.keys():
    #var = dic2[p_data]
    #print(var)

try:
    print(' Try ---»»')
    #fc1()
    tk = 'WEGE3.SA'
    fonte = 'yahoo'
    #set_csv(tk,fonte,'C:/DEV_WorkSpace/Rep_Python/Curso_Python_com_financas/csv/'+tk+'.csv')
    #te = wb.DataReader('^IXIC',data_source='yahoo',start='1995-01-01')
    #print(te.head())
    print(' fim do Try --')
except ValueError:
    print('entrou no ValueError --')
except RuntimeError:
    print('entrou no RuntimeError')
except:
    print('» -- ocorreu um erro, invocou exceção -- ««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««')
#finally:
    #te.close()
    #print('entrou no finally --')