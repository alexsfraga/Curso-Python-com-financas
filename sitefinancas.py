
import requests
import pandas_datareader as wb
import pandas as pd
import self as self


class ConWeb():

    def __init__(self):
        self.API_URL = "https://www.alphavantage.co/query"
        self.myAPIKey = 'OTGYTHIMBWAK650C'
        #self.tiket = ''

    def RequestAdjClose(tk):
        #self.tiket = tk #'WEGE3.SA'
        data = {
            #"function": "TIME_SERIES_DAILY",
            "function": 'TIME_SERIES_DAILY_ADJUSTED',
            "symbol": tk,
            #"outputsize": "compact",
            "apikey": self.myAPIKey,
            "adjusted" : "false",
            #adjusted=True (para retornar data de dividendos)
            "date": "2020-01-01"
            }
        response = requests.get(self.API_URL, params=data).json()
        #cota = response['Time Series (Daily)']
        return response


    def RequestList(self,plist, dateStart):
        #tik = plist

        response = pd.DataFrame()
        for t in plist:
            response[t] = wb.DataReader(t, data_source='yahoo', start=dateStart )['Adj Close']

        #response = requests.get(self.API_URL, params=data).json()
        #cota = response['Time Series (Daily)']
        return response

        #data_req_list = pd.DataFrame()
        #for t in tik:
        #    data_req_list[t] = wb.DataReader(t, data_source='yahoo', dateStart)['Adj Close']
        #return data_req_list

    #freq3()