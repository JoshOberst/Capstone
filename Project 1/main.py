import yfinance as yf
from yahoofinancials import YahooFinancials
import csv
import pandas as pd


weightList = list(csv.reader(open('Project 1\WeightsOfTheWorld.csv')))
weights = pd.DataFrame(weightList,columns=weightList[0])
data = yf.download(weights["Tick"][1:len(weights)-2].to_list(), start='2011-01-01', end='2021-12-31', progress=False) #don't touch this it works

print(data)