import sqlite3
import datetime
import numpy as np
import pandas as pd

db = sqlite3.connect('C:/Users/44774/Desktop/Raj/TradingView/Indicators.db')

nifty_twohundred = ["ACC", "AUBANK", "AARTIIND", "ABBOTINDIA", "ADANIENT", "ADANIGAS", "ADANIGREEN", "ADANIPORTS",
                    "ADANITRANS", "ABCAPITAL", "ABFRL", "AJANTPHARM", "APLLTD", "ALKEM", "AMARAJABAT", "AMBUJACEM",
                    "APOLLOHOSP", "APOLLOTYRE", "ASHOKLEY", "ASIANPAINT", "AUROPHARMA", "DMART", "AXISBANK",
                    "BAJAJ_AUTO", "BAJFINANCE", "BAJAJFINSV", "BAJAJHLDNG", "BALKRISIND", "BANDHANBNK", "BANKBARODA",
                    "BANKINDIA", "BATAINDIA", "BERGEPAINT", "BEL", "BHARATFORG", "BHEL", "BPCL", "BHARTIARTL",
                    "BIOCON", "BBTC", "BOSCHLTD", "BRITANNIA", "CESC", "CADILAHC", "CANBK", "CASTROLIND",
                    "CHOLAFIN", "CIPLA", "CUB", "COALINDIA", "COFORGE", "COLPAL", "CONCOR", "COROMANDEL", "CROMPTON",
                    "CUMMINSIND", "DLF", "DABUR", "DALBHARAT", "DHANI", "DIVISLAB", "LALPATHLAB", "DRREDDY",
                    "EDELWEISS", "EICHERMOT", "EMAMILTD", "ENDURANCE", "ESCORTS", "EXIDEIND", "FEDERALBNK", "FORTIS",
                    "FRETAIL", "GAIL", "GMRINFRA", "GICRE", "GLENMARK", "GODREJAGRO", "GODREJCP", "GODREJIND",
                    "GODREJPROP", "GRASIM", "GUJGASLTD", "GSPL", "HCLTECH", "HDFCAMC", "HDFCBANK", "HDFCLIFE",
                    "HAVELLS", "HEROMOTOCO", "HINDALCO", "HINDPETRO", "HINDUNILVR", "HINDZINC", "HUDCO", "HDFC",
                    "ICICIBANK", "ICICIGI", "ICICIPRULI", "ISEC", "IDFCFIRSTB", "ITC", "IBULHSGFIN", "INDHOTEL", "IOC", "IGL", "INDUSINDBK", "NAUKRI",
                    "INFY", "INDIGO", "IPCALAB", "JSWENERGY", "JSWSTEEL",
                    "JINDALSTEL", "JUBLFOOD", "KOTAKBANK", "L_TFH", "LTTS", "LICHSGFIN", "LTI", "LT", "LUPIN", "MRF",
                    "MGL", "M_MFIN", "M_M", "MANAPPURAM", "MARICO", "MARUTI", "MFSL", "MINDTREE", "MOTHERSUMI",
                    "MPHASIS", "MUTHOOTFIN", "NATCOPHARM", "NMDC", "NTPC", "NATIONALUM", "NAVINFLUOR", "NESTLEIND",
                    "NAM_INDIA", "OBEROIRLTY", "ONGC", "OIL", "OFSS", "PIIND", "PAGEIND", "PETRONET", "PFIZER",
                    "PIDILITIND", "PEL", "PFC", "POWERGRID", "PRESTIGE", "PGHH", "PNB", "RBLBANK", "RECLTD",
                    "RAJESHEXPO", "RELIANCE", "SBILIFE", "SRF", "SANOFI", "SHREECEM", "SRTRANSFIN",
                    "SIEMENS", "SBIN", "SAIL", "SUNPHARMA", "SUNTV", "SYNGENE", "TVSMOTOR", "TATACHEM", "TCS",
                    "TATACONSUM", "TATAMOTORS", "TATAPOWER", "TATASTEEL", "TECHM", "RAMCOCEM", "TITAN", "TORNTPHARM",
                    "TORNTPOWER", "TRENT", "UPL", "ULTRACEMCO", "UNIONBANK", "UBL", "MCDOWELL_N", "VGUARD", "VBL",
                    "IDEA", "VOLTAS", "WHIRLPOOL", "WIPRO", "YESBANK", "ZEEL"]


# def create_tables():
#     c = db.cursor()
#     for i in nifty_twohundred:
#         c.execute("CREATE TABLE IF NOT EXISTS {} (Date datetime primary key, Price real(15,5), Week_SMA_5 real(15,5), Week_SMA_10 "
#                   "real(15,5), Week_SMA_20 real(15,5), Week_SMA_30 real(15,5), Week_SMA_50 real(15,5), Week_SMA_100 real(15,5), Day_SMA_5 real(15,"
#                   "5), Day_SMA_10 real(15,5), Day_SMA_20 real(15,5), Day_SMA_30 real(15,5), Day_SMA_50 real(15,5), Day_SMA_100 real(15,"
#                   "5))".format(i))
#     try:
#         db.commit()
#     except:
#         db.rollback()

def create_tables():
    c = db.cursor()
    for i in nifty_twohundred:
        c.execute("CREATE TABLE IF NOT EXISTS {} (Date datetime primary key, Price real(15,5), Week_SMA_5 real(15,5), Week_SMA_10 "
                  "real(15,5), Week_SMA_20 real(15,5), Week_SMA_30 real(15,5), Week_SMA_50 real(15,5), Week_SMA_100 real(15,5), Signal integer)".format(
            i))
    try:
        db.commit()
    except:
        db.rollback()


def insert_indicator_data(data, data_two, stock):
    c = db.cursor()
    signal = 0
    if data['SMA50'] > data['SMA100']:
        signal = 1.0
    vals = [datetime.datetime.now(), data_two.price, data['SMA5'], data['SMA10'], data['SMA20'], data['SMA30'], data['SMA50'], data['SMA100'], signal]
    query = "INSERT INTO {}(Date,Price,Week_SMA_5,Week_SMA_10,Week_SMA_20,Week_SMA_30,Week_SMA_50,Week_SMA_100,Signal) VALUES (?,?,?,?,?,?,?,?,?)".format(
        stock)
    c.execute(query, vals)
    try:
        db.commit()
    except:
        db.rollback()
