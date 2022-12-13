import pandas as pd
from datetime import datetime
import yfinance as yf
import FinanceDataReader as fdr

companies = {'Ares Capital Corp' : 'ARCC', 'FS KKR Capital Corp.' : 'FSK', 'Owl Rock Capital Corporation' : 'ORCC', 'Blackstone Secured Lending Fund':'BXSL', 'Prospect Capital Corp' : 'PSEC', 'Main Street Capital Corp' : 'MAIN', 'Golub Capital BDC Inc' : 'GBDC', 'Hercules Capital Inc.' : 'HTGC', 'Goldman Sachs BDC Inc' : 'GSBD', 'TPG Specialty Lending Inc' : 'TSLX', 'New Mountain Finance Corp' : 'NMFC', 'Oaktree Specialty Lending Corporation' : 'OCSL', 'Barings BDC Inc.' : 'BBDC', 'Bain Capital Specialty Finance, Inc.' : 'BCSF', 'Solar Capital Ltd' : 'SLRC', 'TCP Capital Corp' : 'TCPC', 'TCG BDC' : 'CGBD', 'CION Investment Corporation' : 'CION', 'Capital Southwest Corp' : 'CSWC', 'PennantPark Floating Rate Capital Ltd' : 'PFLT', 'Fidus Investment Corp' : 'FDUS', 'Gladstone Investment Corp' : 'GAIN', 'Triplepoint Venture Growth BDC Corp' : 'TPVG', 'Crescent Capital BDC, Inc.' : 'CCAP', 'Newtek Business Services Corp' : 'NEWT', 'Trinity Capital Inc.' : 'TRIN', 'PennantPark Investment Corp' : 'PNNT', 'Horizon Technology Finance Corp' : 'HRZN', 'Gladstone Capital Corp' : 'GLAD', 'WhiteHorse Finance Inc' : 'WHF', 'BlackRock Capital Investment Corporation' : 'BKCC', 'Saratoga Investment' : 'SAR', 'Stellus Capital Investment Corp' : 'SCM', 'Portman Ridge Finance Corporation' : 'PTMN', 'Monroe Capital Corp' : 'MRCC', 'Oxford Square Capital Corp' : 'OXSQ', 'OFS Capital Corp' : 'OFS', 'First Eagle Alternative Capital BDC, Inc.' : 'FCRD', 'PhenixFIN Corporation' : 'PFX', 'Great Elm Capital Corp' : 'GECC', 'Silver Spike Investment Corp.' : 'SSIC', '180 Degree Capital' : 'TURN', 'Investcorp Credit Management BDC, Inc.' : 'ICMB', 'Logan Ridge Finance Corporation' : 'LRFC', 'Rand Capital' : 'RAND', 'Equus Total Return' : 'EQS', 'Firsthand Technology Value Fund' : 'SVVC'}
symbols = list(companies.values())

with pd.ExcelWriter('US BDCs.xlsx') as writer:
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
hist.to_excel('US_BDC_prices_221122.xlsx')

info = pd.DataFrame()
for symbol in symbols:
    ticker = yf.Ticker(symbol)
    ticker_info = ticker.info
    i = pd.DataFrame(ticker_info.values(), ticker_info.keys())
    info = pd.concat([info, i], axis=1)