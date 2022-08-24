# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 17:32:44 2022

@author: adams
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 14:45:06 2022

@author: adams
"""
import sqlite3
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

spolka = 'KRU.WA'
conn = sqlite3.connect('DG')
cursor = conn.cursor()

#######################
lista_spolek = pd.read_sql_query("SELECT Distinct spolka FROM dane where Date > date('now','-5 days')", con=conn)

tabela_stosunki = {}

for spolka in lista_spolek['spolka']:
    
    analiza = pd.read_sql("SELECT * FROM dane WHERE spolka =? and Date > '2022-01-01'", con=conn, params=[spolka])
    analiza['Date'] = pd.to_datetime(analiza['Date'], format='%Y%m%d %H:%M:%S')
    maks_cena = max(analiza['Close'])
    ostatnia_data = max(analiza['Date'])
    ostatnia_cena = analiza[analiza['Date']==ostatnia_data]
    ostatnia_cena = ostatnia_cena['Close']
    ostatnia_cena = list(ostatnia_cena)
    ostatnia_cena = ostatnia_cena[0]
    stosunek = ostatnia_cena/maks_cena
    tabela_stosunki[spolka] = stosunek
    print(spolka)

tabela = pd.DataFrame.from_dict(data=tabela_stosunki, orient='index',columns=['stosunek'])

spolki_upadle = tabela.query('stosunek <0.3')