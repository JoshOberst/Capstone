import yfinance as yf
from yahoofinancials import YahooFinancials
import csv
import pandas as pd

cash = 100000
data = yf.download(['SPEU','AAXJ','EWJ','ILF','EWA','AFK','SPY','EWC','EWW'], start='2011-01-01', end='2021-12-31', progress=False).get("Adj Close")
weightList = list(csv.reader(open('Project 1\WeightsOfTheWorld.csv')))
weights = pd.DataFrame(weightList,columns=weightList[0])
portfolioShares = []
for tick in data:
    moneyToSpend = float(weights.loc[weights['Tick'] == tick].get('Percent').values[0]) * cash
    shares = moneyToSpend/data.get(tick)[0]
    portfolioShares.append([tick,shares,data.get(tick)[0],data.get(tick)[-1]])
    #[tick,shares,2011 price,2021 price]
finalCash = 0
for tick in portfolioShares:
    finalCash = finalCash + (tick[1]*tick[3])
    oCost = tick[1]*tick[2]
    nCost = tick[1]*tick[3]
    pctChange = ((nCost-oCost)/oCost)*100
    print(tick[0],oCost,nCost,pctChange,'%')
print(finalCash)