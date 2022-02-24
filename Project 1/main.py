import yfinance as yf
from yahoofinancials import YahooFinancials
import csv
import pandas as pd
import datetime

dateMaster = datetime.date(2011, 1, 1)

weightList = list(csv.reader(open('Project 1\WeightsOfTheWorld.csv')))
weights = pd.DataFrame(weightList,columns=weightList[0])
data = yf.download(weights["Tick"][1:len(weights)].to_list(), start='2011-01-01', end='2021-12-31').get('Adj Close') #don't touch this it just works

fullData = pd.DataFrame([],weights["Tick"][1:len(weights)-2].to_list(),['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021'])


for tick in data:
    for price in data.get(tick):
        for date in data.get(tick)[data.get(tick) == price].index:
            if date > dateMaster:
                if str(date.year) == '2011':
                    fullData[str(date.year)][tick] = (price - data[tick][0])/data[tick][0] * 100
                else:
                    fullData[str(date.year)][tick] = (price - fullData[str(date.year-1)][tick])/fullData[str(date.year-1)][tick] * 100
                dateMaster = date
                
    dateMaster = datetime.date(2011, 1, 1)

print(fullData)
