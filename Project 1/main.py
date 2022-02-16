import yfinance as yf
from yahoofinancials import YahooFinancials
import numpy as np

data = yf.download(['SPEU','AAXJ','EWJ','ILF','EWA','AFK','SPY','EWC','EWW'], start='2011-01-01', end='2021-12-31', progress=False)
with open("/WeightsOfTheWorld.csv") as weightFile:
    weights = np.loadtxt(weightFile, delimiter=",")

print(weights)


print(data.get("Adj Close").get('SPY'))