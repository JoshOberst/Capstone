from cProfile import label
import yfinance as yf
from yahoofinancials import YahooFinancials
import csv
import pandas as pd
import datetime
import matplotlib.pyplot as plt

dateMaster = datetime.date(2010, 12, 25) #this is the ultimate start date, preferably near the end of the year
dateVar = dateMaster

def returns(weightCSV):
    global dateVar
    weights = pd.DataFrame(weightCSV,columns=weightCSV[0])
    data = yf.download(weights["Tick"][1:len(weights)-1].to_list(), start='2010-12-25', end='2021-12-31').get('Adj Close') #don't touch this it just works

    fullData = pd.DataFrame([],weights["Tick"][1:len(weights)-1].to_list(),['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021'])
    returns = pd.DataFrame([],weights["Tick"][1:len(weights)-1].to_list(),['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021'])

    #creating the returns dataframe
    for tick in data:
        for price in data.get(tick):
            for date in data.get(tick)[data.get(tick) == price].index:
                if date > dateVar:
                    fullData[str(date.year)][tick] = price 
                    dateVar = date              
        dateVar = dateMaster

    for etf in returns.index:
        for year in returns.iloc[0].index:
            if year != '2010':
                returns[year][etf] = ((fullData[year][etf] - fullData[str(int(year)-1)][etf])/ fullData[str(int(year)-1)][etf])*100

    #Portfolio Performace
    startingCash = 100000
    value = pd.DataFrame([],weights["Tick"][1:len(weights)-1].to_list(),['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021'])
    for tick in data:
        moneyToSpend = float(weights.loc[weights['Tick'] == tick].get('Percent').values[0]) * startingCash
        shares = moneyToSpend/data.get(tick)[0]
        for year in value.iloc[0].index:
            if year != '2010':
                value[year][tick] = fullData[year][tick] * shares

    #Total Row
    yearTotals = []
    for year in value.iloc[0].index:
        yearTotals.append(value[year].sum())
    value.loc['Total'] = yearTotals
    

    #Creating Plots
    fig, ax = plt.subplots(3,3)
    fig.tight_layout()
    fig.suptitle('ETFs in the Portfolio', fontsize=16)
    i = 0
    j = 0
    for etf in returns.index:
        ax[i][j].tick_params(axis='x', labelrotation = 45)
        ax[i][j].plot(returns.transpose().get(etf))
        ax[i][j].set_title(etf)
        ax[i][j].set_ylabel('Returns(%)')
        j=j+1
        if j > 2:
            j = 0
            i = i+1
    plt.show()
    return(value)
#end of Function

popWeighted = list(csv.reader(open('Project 1\WeightsOfTheWorld.csv')))
gdpWeighted = list(csv.reader(open('Project 1\WeightOfTheWorldByGDP.csv')))

gdpW = returns(gdpWeighted)
popW = returns(popWeighted)

popValue = popW.transpose().get('Total')
gdpValue = gdpW.transpose().get('Total')

popReturns = pd.Series(data = [0,0,0,0,0,0,0,0,0,0,0],index = ['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021'])
gdpReturns = pd.Series(data = [0,0,0,0,0,0,0,0,0,0,0],index = ['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021'])

for year in popValue.index:
    if year != '2011':
        popReturns[year] = (popValue[year] - popValue[str(int(year)-1)]) / popValue[str(int(year)-1)] * 100
        gdpReturns[year] = (gdpValue[year] - gdpValue[str(int(year)-1)]) / gdpValue[str(int(year)-1)] * 100




plt.plot(popValue,label="Weighted By Population")
plt.plot(gdpValue,label="Weighted By GDP")
plt.title("Value of the Portfolios")
plt.ylabel("Value(USD$)")
plt.legend()
plt.show()

plt.close()

plt.plot(popReturns,label="Weighted By Population")
plt.plot(gdpReturns,label="Weighted By GDP")
plt.title("Returns of the Portfolios")
plt.ylabel("Returns(%)")
plt.legend()
plt.show()