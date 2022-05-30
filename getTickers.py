import random
from get_all_tickers import get_tickers

allTickers = get_tickers(NYSE=True, NASDAQ = True, AMEX=False)

length = len(allTickers)

tickerNumbers = []
tickers =[]

while len(tickerNumbers) < 50:
    randomInt = random.randint(0,len(allTickers)-1)
    if(randomInt not in tickerNumbers):
        tickerNumbers.append(randomInt)

for i in tickerNumbers:
    tickers.append(allTickers(i))