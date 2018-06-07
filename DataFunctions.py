import csv
import datetime
from decimal import Decimal
import pandas as pd

def normalize_dataframe(divisor, raw):
    print(raw[0])
    print(raw[1])
    multiplier = divisor / raw[0]
    test_list = []
    for number in raw:
        temp = number*multiplier
        test_list.append(temp)

    return test_list

def pair_stock_and_crude(stock_data, oil_data):
    index_list = []
    time_list1 = []
    open_price = []
    high_price = []
    low_price = []
    close_price = []

    with open('%s' % (stock_data)) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in readCSV:
            if row[0] != '' and row[1] != '' and row[2] != '' and row[3] != '' and row[4] != '':
                index_list.append(i)
                date1 = datetime.datetime.fromtimestamp(int(row[0]))
                date2 = date1+ datetime.timedelta(hours=6)
                time_list1.append(date2.strftime('%Y-%m-%d %H:%M:%S'))

                open_price.append(float(row[1].replace(',', '')))
                high_price.append(float(row[2].replace(',', '')))
                low_price.append(float(row[3].replace(',', '')))
                close_price.append(float(row[4].replace(',', '')))
                i += 1
        print(time_list1)
        stock = pd.DataFrame(

            {'index': index_list,
             'date': time_list1,
             'open': open_price,
             'high': high_price,
             'low': low_price,
             'close': close_price
             })

    index_list = []
    time_list = []
    open_price = []
    high_price = []
    low_price = []
    close_price = []


    with open('%s' % (oil_data)) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        i = 0

        for row in readCSV:
            if(datetime.datetime.fromtimestamp(int(row[0])).strftime('%Y-%m-%d %H:%M:%S') in time_list1):
                if row[0] != '' and row[1] != '' and row[2] != '' and row[3] != '' and row[4] != '':
                    index_list.append(i)
                    time_list.append(datetime.datetime.fromtimestamp(int(row[0])).strftime('%Y-%m-%d %H:%M:%S')) #Påverkar int() hur datumet blir ?
                    open_price.append(float(row[1].replace(',', '')))
                    high_price.append(float(row[2].replace(',', '')))
                    low_price.append(float(row[3].replace(',', '')))
                    close_price.append(float(row[4].replace(',', '')))
                    print("----------")
                    i +=1
        print(time_list)
        brent = pd.DataFrame(

            {'index': index_list,
             'date': time_list,
             'open': open_price,
             'high': high_price,
             'low': low_price,
             'close': close_price
             })

    merged = pd.merge(brent,stock, on='date', how='inner')

    #print(merged)
    stock_formatted = pd.concat([merged['date'], merged['open_x'], merged['high_x'], merged['low_x'], merged['close_x']], axis=1,
              keys=None)
    brent_formatted = pd.concat([merged['date'], merged['open_y'], merged['high_y'], merged['low_y'], merged['close_y']], axis=1,
              keys=None)

    brent_formatted = pd.concat([merged['date'], merged['open_x'], merged['high_x'], merged['low_x'], merged['close_x']], axis=1,
              keys=None)
    stock_formatted = pd.concat([merged['date'], merged['open_y'], merged['high_y'], merged['low_y'], merged['close_y']], axis=1,
              keys=None)

    print('-----------------------')
    print(stock_formatted)
    print(brent_formatted)


    return {'brent':brent_formatted, 'stock':stock_formatted}

