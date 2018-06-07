import plotly
import pandas as pd
from bokeh.models import HoverTool
import matplotlib.pyplot as plt
import numpy as np


plotly.tools.set_credentials_file(username='seb142', api_key='jKvY196YE02TJmwuMwEH')
from bokeh.layouts import column
from bokeh.plotting import figure, output_file, show
import DataFunctions as dfunc

def candlestick(df,df2):

    inc = df.close > df.open
    dec = df.open > df.close

    p = figure(plot_width=1000, title="MSFT Candlestick with Custom X-Axis")

    # map dataframe indices to date strings and use as label overrides
    p.xaxis.major_label_overrides = {
        i: date.strftime('%b %d') for i, date in enumerate(pd.to_datetime(df["date"]))
    }
    p.xaxis.bounds = (0, df.index[-1])
    p.x_range.range_padding = 0.05

    p.segment(df.index, df.high, df.index, df.low, color="black")
    p.vbar(df.index[inc], 0.5, df.open[inc], df.close[inc], fill_color="#D5E1DD", line_color="black")
    p.vbar(df.index[dec], 0.5, df.open[dec], df.close[dec], fill_color="#F2583E", line_color="black")

    output_file("custom_datetime_axis.html", title="custom_datetime_axis.py example")

    show(p)

def double_line_chart(df1,df2):

    f = round(df1['close_x'][0],2)
    p = figure(plot_width=1200, plot_height=800)
    hover = HoverTool(
        tooltips=[
            ('date', '@date{%F}'),
            ('close', '$@{adj close}{%0.2f}'),  # use @{ } for field names with spaces
            ('volume', '@volume{0.00 a}'),
        ],

        formatters={
            'date': 'datetime',  # use 'datetime' formatter for 'date' field
            'adj close': 'printf',  # use 'printf' formatter for 'adj close' field
            # use default 'numeral' formatter for other fields
        },

        # display a tooltip whenever the cursor is vertically in line with a glyph
        mode='vline'
    )
    p.add_tools(hover)
    p.multi_line(xs=[df1.index.tolist(), df2.index.tolist()], ys=[dfunc.normalize_dataframe(f,df1.close_x.tolist()),dfunc.normalize_dataframe(f,df2.close_y.tolist())],
                 color=['red', 'green'], legend="3*sin(x)")

    show(p)

def regression(df1,df2):

    np.random.seed(19680801)

    data_list1 = df1.close_x.tolist()
    data_list2 = df2.close_y.tolist()
    data_list3 = df2.close_y.tolist()

    print("test",data_list2)
    count = 0
    positives = 0
    negatives = 0

    predictions(data_list1, data_list2, df1)





def predictions(data_list1, data_list2, df1):
    count = 0
    positives = 0
    print('**********************',df1)
    for i in range(9,len(df1.close_x.tolist())):
        data_list1[i-1] = df1.close_x.tolist()[i-3]/df1.close_x.tolist()[i - 9]

        if data_list1[i-1] > 1.006:
            print("oil movement",df1.date.tolist()[i-3],"value:",df1.close_x.tolist()[i-3], "stockmovement",df1.date[i], data_list2[i]/data_list2[i-2], data_list2[i])
            count += 1
            if data_list2[i]/data_list2[i-2] > 1:
                positives += 1
                print("positive")

    print(positives," ", count)
    print("andel pos:",positives/count)

    print(len(df1.close_x.tolist()))
    print(len(data_list1))
