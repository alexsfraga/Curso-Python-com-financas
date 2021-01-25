
import pip
#import googlefinance
#pip.main(['install','googlefinance'])
#pip.main(['install','FinanceScraper'])


#https://financescraper.readthedocs.io/en/latest/quickstart.html
from financescraper import scraper
my_scraper = scraper.FinanceScraper()
#data1 = my_scraper.get_data('AMZN')
#data2 = my_scraper.get_company_data('AMZN')
#print(data1)
#print(data2)

from googlefinance import getQuotes
import json
print(json.dumps(getQuotes('AAPL'), indent=2))

#import pip
#pip.main(['install','alphavantage'])

from sitefinancas.price_history import (
  AdjustedPriceHistory, get_results, PriceHistory, IntradayPriceHistory,
  filter_dividends
)

# weekly prices
history = PriceHistory(period='W', output_size='compact')
results = history.get('AAPL')

# intraday prices, 5 minute interval
history = IntradayPriceHistory(utc=True, interval=5)
results = history.get('AAPL')

# adjusted daily prices
history = AdjustedPriceHistory(period='D')
results = history.get('AAPL')
dividends = list(filter_dividends(results.records))

# Return multiple tickers
parameters = {'output_size': 'compact', 'period': 'D'}
tickers = ['AAPL', 'MSFT']
results = dict(get_results(PriceHistory, tickers, parameters))


import pip
pip.main(['uninstall','alphavantage'])
pip.main(['install','alpha_vantage'])

import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

myAPIKey ='OTGYTHIMBWAK650C'
tk  = 'AAPL'
ts = TimeSeries(key=myAPIKey, output_format='pandas')
#data, meta_data = ts.get_intraday(symbol='WEGE',outputsize='full')
data, meta_data = ts.get_daily(symbol=tk,outputsize='full')
#meta_data = ts.get_intraday(symbol='WEGE3.SA',interval='1min', outputsize='full')
#ts.get_intraday(symbol='MSFT',outputsize='full')
data.plot(figsize=(13,6))
print(data)
#plt.title('Intraday Times Series for the WEGE3.SA stock (1 min)')
#plt.show()


import requests
API_URL = "https://www.alphavantage.co/query"
data = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "AAPL",
 "outputsize": "compact",
    "apikey": myAPIKey
    }

response = requests.get(API_URL, params=data)
print(response.json())import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

myAPIKey ='OTGYTHIMBWAK650C'
tk  = 'AAPL'
ts = TimeSeries(key=myAPIKey, output_format='pandas')
#data, meta_data = ts.get_intraday(symbol='WEGE',outputsize='full')
data, meta_data = ts.get_daily(symbol=tk,outputsize='full')
#meta_data = ts.get_intraday(symbol='WEGE3.SA',interval='1min', outputsize='full')
#ts.get_intraday(symbol='MSFT',outputsize='full')
data.plot(figsize=(13,6))
print(data)
#plt.title('Intraday Times Series for the WEGE3.SA stock (1 min)')
#plt.show()


import requests
API_URL = "https://www.alphavantage.co/query"
data = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "AAPL",
 "outputsize": "compact",
    "apikey": myAPIKey
    }

response = requests.get(API_URL, params=data)
print(response.json())

# https://cadernodelaboratorio.com.br/args-e-kwargs-o-que-significam-em-python/