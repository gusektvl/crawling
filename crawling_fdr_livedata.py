import numpy as np
import pandas as pd
import pandas_datareader as pdr
import yfinance as yf
import FinanceDataReader as fdr
import requests
import time

start, end = '2000-03-01', '2022-04-10'
ust_close = fdr.DataReader("US3MT=X", start, end)['Close']
ust_close = pd.DataFrame(ust_close)
ust_close.columns = ['UST 3M']
for N in [1, 2, 3, 5, 7, 10, 30]:
    df = fdr.DataReader("US{}YT=X".format(N), start, end)['Close']
    df = pd.DataFrame(df)
    df.columns = ["UST {}Y".format(N)]
    ust_close = pd.concat([ust_close, df], axis=1)
display(ust_close)

ust_10y3y = pd.DataFrame(ust_close['UST 10Y'] - ust_close['UST 3Y'], columns=['10y-3y'])
ust_10y2y = pd.DataFrame(ust_close['UST 10Y'] - ust_close['UST 2Y'], columns=['10y-2y'])
ust_10y3m = pd.DataFrame(ust_close['UST 10Y'] - ust_close['UST 3M'], columns=['10y-3m'])
ust_spread = pd.concat([ust_10y3y, ust_10y2y, ust_10y3m], axis=1)
display(ust_spread)