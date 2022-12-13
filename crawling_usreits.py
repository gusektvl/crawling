import pandas as pd
from datetime import datetime
import yfinance as yf
import FinanceDataReader as fdr

companies = {'Alexandria':'ARE', 'American Tower':'AMT', 'Realty Income':'O', 'Americold':'COLD',
           'American Homes 4 Rent':'AMH', 'Avalon Bay':'AVB', 'Crown Castle':'CCI', 'Digital Realty':'DLR',
           'Equinix':'EQIX', 'Prologis':'PLD', 'Public Storage':'PSA',
           'Medical Properties Trust Inc.':'MPW', 'Boston Properties':'BXP', 'Vornado':'VNO',
           'Camden Property Trust':'CPT', 'Duke Realty Corp':'DRE', 'Equity Lifestyle Properties':'ELS',
           'Equity Residential':'EQR', 'Essex Property Trust Inc.':'ESS', 'Extra Space':'EXR',
           'Federal Realty Investment':'FRT', 'Gaming and Leisure Properties':'GLPI',
           'Healthpeak Properties Inc.':'PEAK', 'Host Hotel & Resort':'HST', 'Invitation Homes':'INVH',
           'Iron Mountain Inc.':'IRM', 'Kilroy Realty Corp.':'KRC', 'W.P. Carey':'WPC',
           'Mid-America Apartment Communities':'MAA', 'National Retail Properties':'NNN',
           'Omega Healthcare':'OHI', 'Park Hotels & Resorts Inc':'PK', 'Regency Centers Corp.':'REG',
           'SBA Communications':'SBAC', 'Simon Property':'SPG', 'STAG Industrial':'STAG',
           'Sun Communities Inc.':'SUI', 'UDR Inc.':'UDR', 'Ventas Inc.':'VTR',
           'Vici Property':'VICI', 'Well Tower':'WELL', 'Blackstone Mortgage':'BXMT', 'Weyerhaeuser':'WY',
           'AGNC Investment':'AGNC', 'Lamar Advertising Company':'LAMR', 'Brixmor Property Group Inc.':'BRX', 'EastGroup Properties, Inc.':'EGP'}
symbols = list(companies.values())

with pd.ExcelWriter('US REITs.xlsx') as writer:
    hist = pd.DataFrame()
    for symbol in symbols:
        ticker = yf.Ticker(symbol)
        ticker_BS_a = ticker.balancesheet
        ticker_BS_q = ticker.quarterly_balancesheet
        ticker_FS_a = ticker.financials
        ticker_FS_q = ticker.quarterly_financials
        ticker_E_a = ticker.earnings
        ticker_E_q = ticker.quarterly_earnings
        ticker_CF_a = ticker.cashflow
        ticker_CF_q = ticker.quarterly_financials
        data_a = pd.concat([ticker_BS_a, ticker_FS_a, ticker_CF_a])
        data_q = pd.concat([ticker_BS_q, ticker_FS_q, ticker_CF_q])
        data_div = ticker.dividends
        data_div.index = data_div.index.tz_localize(None)
        data_info = pd.DataFrame(list(ticker.get_info().values()), index=list(ticker.get_info().keys()))
        data_info.to_excel(writer, sheet_name=symbol+'_info')
        data_a.to_excel(writer, sheet_name=symbol+'_annual')
        data_q.to_excel(writer, sheet_name=symbol+'_quarter')
        data_div.to_excel(writer, sheet_name=symbol+'_div')
        h = ticker.history(period='3y')[['Close', 'Volume']][::-1]
        h.columns = [symbol + '_Close', symbol + '_Volume']
        h.index = h.index.tz_localize(None)
        hist = pd.concat([hist, h], axis=1)
        print(symbol+' done!')
    hist.to_excel(writer, sheet_name='price')

hist = pd.DataFrame()
for symbol in symbols:
    ticker = yf.Ticker(symbol)
    h = ticker.history(period='3y')[['Close', 'Volume']][::-1]
    h.columns = [symbol+'_Close', symbol+'_Volume']
    hist = pd.concat([hist, h], axis=1)
hist.index = hist.index.tz_localize(None)
hist.to_excel('us reits price_221111.xlsx')

info = pd.DataFrame()
for symbol in symbols:
    ticker = yf.Ticker(symbol)
    ticker_info = ticker.info
    i = pd.DataFrame(ticker_info.values(), ticker_info.keys())
    info = pd.concat([info, i], axis=1)