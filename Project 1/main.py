import yfinance as yf
from yahoofinancials import YahooFinancials

data = yf.download(['SPEU','AAXJ','EWJ','ILF','EWA','AFK','SPY','EWC','EWW'], start='2011-01-01', end='2021-12-31', progress=False)

print(data.get("Adj Close").get('SPY'))