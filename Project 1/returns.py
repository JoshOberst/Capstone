from cProfile import label
from cmath import sqrt
import yfinance as yf
from yahoofinancials import YahooFinancials
import csv
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
from pypfopt import expected_returns
import math

dateMaster = datetime.date(2010, 12, 25) #this is the ultimate start date, preferably near the end of the year
bench = 'VT'
tenYearTbill = yf.download('^TNX',start = '2022-05-01').get('Adj Close')[-1]

popWeighted = list(csv.reader(open('Project 1\WeightsOfTheWorld.csv')))
gdpWeighted = list(csv.reader(open('Project 1\WeightOfTheWorldByGDP.csv')))

header = popWeighted.pop(0)

pop = pd.DataFrame(popWeighted,columns=header)
gdp = pd.DataFrame(gdpWeighted,columns=header)#simple searchable data frames

stockList = list(pop.get('Tick'))
stockList[-1] = bench

data = yf.download(stockList,dateMaster).get('Adj Close')

#Getting Log Returns
returns = np.log(data.copy()).diff().dropna()

#Spliting out the benchmark
assets = returns.loc[:, returns.columns != bench]
benchmark = returns.loc[:, returns.columns == bench]

#Calculating Expected returns and the Cov Matrix
eR = expected_returns.capm_return(assets,market_prices = benchmark, returns_data = True, risk_free_rate = tenYearTbill/100,frequency = 252)
covMatrix = assets.cov()*252

dfER = pd.DataFrame(eR)
dfPop = pd.DataFrame(pop.get('Percent')[:-1])
dfPop.Percent = pd.to_numeric(dfPop.Percent, errors='coerce')
dfGdp = pd.DataFrame(gdp.get('Percent')[1:-1])
dfGdp.Percent = pd.to_numeric(dfGdp.Percent,errors='coerce')

popER = np.dot(dfER.T,dfPop)[0][0]
popVar = np.dot(np.dot(dfPop.T,covMatrix),dfPop)[0][0]
popSharpe = (popER - (tenYearTbill/252))/sqrt(popVar).real

gdpER = np.dot(dfER.T,dfGdp)[0][0]
gdpVar = np.dot(np.dot(dfGdp.T,covMatrix),dfGdp)[0][0]
gdpSharpe = (gdpER - (tenYearTbill/252))/sqrt(gdpVar).real

print("Population Weighted Portfolio",'\n',"Expected Return: " + str(popER*100)+"% ",'\n',"Varience: " + str(popVar*100)+ "%",'\n', "Sharpe Ratio " + str(popSharpe*100)+"%",'\n'+" ")
print("GDP Weighted Portfolio",'\n',"Expected Return: " + str(gdpER*100)+"% ",'\n',"Varience: " + str(gdpVar*100)+ "%",'\n', "Sharpe Ratio " + str(gdpSharpe*100)+"%",'\n'+" ")
