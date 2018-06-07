import DataFunctions as df

import Plots
import XHRScraper
import Plots

#XHRScraper.scrape_ya('https://query1.finance.yahoo.com/v8/finance/chart/CLN18.NYM?symbol=CLN18.NYM&range=6mo&interval=60m&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=FtjRNVKl1Hc&corsDomain=finance.yahoo.com','crude180606-')
#XHRScraper.scrape_ya('https://query1.finance.yahoo.com/v8/finance/chart/CLN18.NYM?symbol=CLN18.NYM&range=6mo&interval=60m&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=FtjRNVKl1Hc&corsDomain=finance.yahoo.com','lupe180606-')
#XHRScraper.scrape_ya('https://query1.finance.yahoo.com/v8/finance/chart/LUPE.ST?symbol=LUPE.ST&period1=1521763200&period2=1522911600&interval=15m&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=FtjRNVKl1Hc&corsDomain=finance.yahoo.com','lupe30min')
#XHRScraper.scrape_ya('https://query1.finance.yahoo.com/v8/finance/chart/BZ=F?symbol=BZ%3DF&period1=1522153800&period2=1524454200&interval=15m&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=FtjRNVKl1Hc&corsDomain=finance.yahoo.com','brent15min')
#Plots.double_line_chart(data.get('brent'),data.get('stock'))


data = df.pair_stock_and_crude('lupe180606-.csv' ,'crude180606-.csv')# förstaparametern
Plots.regression(data.get('brent'),data.get('stock'))