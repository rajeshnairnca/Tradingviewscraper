from tradingview_ta import TA_Handler, Interval, Analysis
from StoreData import create_tables, insert_indicator_data, nifty_twohundred
import pandas as pd
import sqlite3
import time

db = sqlite3.connect('C:/Users/44774/Desktop/Raj/TradingView/Indicators.db')

# handler.set_interval_as(Interval.INTERVAL_1_WEEK)
# handler.set_interval_as(Interval.INTERVAL_1_DAY)
# handler.set_interval_as(Interval.INTERVAL_1_HOUR)
# handler.set_interval_as(Interval.INTERVAL_15_MINUTES)

create_tables()

# Stocks removed from Nifty200 list since these have not completed 100 weeks yet
# IRCTC
# Polycab
# SBICard


for stock in nifty_twohundred:
    handler = TA_Handler()
    handler.set_symbol_as(stock)
    handler.set_exchange_as_crypto_or_stock("NSE")
    handler.set_screener_as_stock("india")
    handler.set_interval_as(Interval.INTERVAL_1_WEEK)
    analysis_one = handler.get_analysis()
    all_indicators = analysis_one.indicators
    insert_indicator_data(all_indicators, analysis_one, stock)
    print(stock)
    time.sleep(2)

global buy_stocks, sell_stocks
buy_stocks = []
sell_stocks = []

for stock in nifty_twohundred:
    data = pd.read_sql('''SELECT * FROM {};'''.format(stock), db)
    data['Position'] = data['Signal'].diff()
    if data['Position'].iloc[-1] == 0:
        buy_stocks.append(stock)
    elif data['Position'].iloc[-1] == -1:
        sell_stocks.append(stock)

print('Buy Stocks\n\n', buy_stocks, '\n')
print('Sell Stocks\n\n', sell_stocks)
