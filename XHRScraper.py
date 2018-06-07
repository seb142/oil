import requests
import json
import datetime
import csv
import plotly
import calendar
import pandas as pd
def scrape_inv(url):


    #url='https://tvc4.forexpros.com/c914652be853639fbabbacab5bec16d5/1526117000/13/13/16/history?symbol=8861&resolution=15&from=1524821004&to=1526117064'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    payload = {'pair_id': 8849, 'pair_id_for_news:': 8849, 'chart_type': 'candlestick','pair_interval': 60,'candle_count': 70,'events': 'yes','volume_series': 'yes', 'period':''}
    response = requests.get(url, headers=headers, params=payload)

    str_response = response.content.decode('utf-8')
    obj = json.loads(str_response)

    time =obj["t"]
    opend = obj["o"]
    high = obj["h"]
    low = obj["l"]
    close = obj["c"]



    with open("lupe_swe.csv", "a", newline='') as f:
        newFileWriter = csv.writer(f)

        for i in range(0, len(time)):
            newFileWriter.writerow([time[i],opend[i],high[i],low[i],close[i]])

def scrape_ya(url, name):
    # url='https://tvc4.forexpros.com/c914652be853639fbabbacab5bec16d5/1526117000/13/13/16/history?symbol=8861&resolution=15&from=1524821004&to=1526117064'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    payload = {'pair_id': 8849, 'pair_id_for_news:': 8849, 'chart_type': 'candlestick', 'pair_interval': 60,
               'candle_count': 70, 'events': 'yes', 'volume_series': 'yes', 'period': ''}
    response = requests.get(url, headers=headers, params=payload)

    str_response = response.content.decode('utf-8')
    obj = json.loads(str_response)

    print(obj['chart']['result'][0]['timestamp'])
    print(obj['chart']['result'][0]['indicators']['quote'][0]['open'])
    print(obj['chart']['result'][0]['indicators']['quote'][0]['high'])
    print(obj['chart']['result'][0]['indicators']['quote'][0]['low'])
    print(obj['chart']['result'][0]['indicators']['quote'][0]['close'])

    time = obj['chart']['result'][0]['timestamp']
    open_price = obj['chart']['result'][0]['indicators']['quote'][0]['open']
    high_price = obj['chart']['result'][0]['indicators']['quote'][0]['high']
    low_price = obj['chart']['result'][0]['indicators']['quote'][0]['low']
    close_price = obj['chart']['result'][0]['indicators']['quote'][0]['close']

    with open("%s.csv"%(name), "a", newline='') as f:
        newFileWriter = csv.writer(f)

        for i in range(0, len(time)):
            newFileWriter.writerow([time[i],open_price[i],high_price[i],low_price[i],close_price[i]])

def readCSV():
    with open('precision_drilling_corp.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
           print(row)