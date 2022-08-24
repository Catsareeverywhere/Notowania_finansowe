# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 12:21:29 2022

@author: adams
"""

import sqlite3
import pandas as pd 
import yfinance as yf
from datetime import datetime
from datetime import timedelta
###Tworzenie bazy danych DG - dane giełdowe


##Utworzenie bazy danych i pobranie archiwalnych sany do 2022.07.01
# =============================================================================
# conn = sqlite3.connect('DG')
# c = conn.cursor()
# 
# c.execute('''
#           DROP TABLE IF EXISTS DANE ''')
# 
# c.execute('''
#           CREATE TABLE IF NOT EXISTS DANE
#           ([id] INTEGER PRIMARY KEY,
#            [Date] TEXT,
#            [spolka] TEXT,
#            [Close] REAL)
#           ''')
# conn.commit()
# 
# sciezka_tickery = 'C:/Users/adams/OneDrive/Pulpit/tickery.xlsx'
# # 
# tickery = pd.read_excel(sciezka_tickery,sheet_name='Tickery')
# tickery['Ticker'] = tickery['Ticker'] + ".WA"
# tickers_list = list(tickery['Ticker'])
# conn = sqlite3.connect('DG')
# c = conn.cursor()
# for spolka in tickers_list:
#     dana= yf.download(spolka ,end='2022-08-20')['Close']
#     dana = pd.DataFrame(dana)
#     dana["spolka"] = spolka
#     dana.reset_index(inplace=True)
#     dana=dana[['Date','spolka','Close']]
#     dana.to_sql('DANE',conn, if_exists='append',index=False)
# 
# conn.commit()
# =============================================================================

###Pobranie zaległych kursów 
# =============================================================================
# conn = sqlite3.connect('DG')
# c = conn.cursor()
# 
# 
# 
# maks = (max(analiza['Date']))
# 
# data = datetime.strptime(maks,'%Y-%m-%d %H:%M:%S').date()
# 
# data = data+ timedelta(days=1)
# data = str(data)
# sciezka_tickery = 'C:/Users/adams/OneDrive/Pulpit/tickery.xlsx'
# tickery = pd.read_excel(sciezka_tickery,sheet_name='Tickery')
# tickery['Ticker'] = tickery['Ticker'] + ".WA"
# tickers_list = list(tickery['Ticker'])
# conn = sqlite3.connect('DG')
# c = conn.cursor()
# for spolka in tickers_list:
#      dana= yf.download(spolka ,start=data)['Close']
#      dana = pd.DataFrame(dana)
#      dana["spolka"] = spolka
#      dana.reset_index(inplace=True)
#      dana=dana[['Date','spolka','Close']]
#      dana.to_sql('DANE',conn, if_exists='append',index=False)
# 
# conn.commit()
# =============================================================================


# =============================================================================
# conn = sqlite3.connect('BAZA')
# c = conn.cursor()
# analiza = pd.read_sql('SELECT * FROM dane WHERE spolka ="BST.WA"', con=conn)
# conn.close()
# 
# analiza['Date'] = pd.to_datetime(analiza['Date'], format='%Y%m%d %H:%M:%S')
# 
# print(analiza.dtypes)
# =============================================================================
