# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 18:49:00 2022

@author: adams
"""

###aktualizacja bazy
def wyslij_mail():
    import smtplib 
    mailfrom = 'Rysiek Kitkowski'
    mailTO = 'rysiekkitkowski@gmail.com'
    mailsubject = 'Wykonanie skryptu'
    message_body = '''
    Udalo sie wykonac skrypt. Elo
    '''
    message = ''' From:{}
    Subject: {}
    
    {}
    '''.format(mailfrom, mailsubject, message_body)
    user = "d1837a7b76e5b1"
    password = "51ac76f89a4159"
    
    server = smtplib.SMTP('smtp.mailtrap.io',2525)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user,mailTO,message)
    server.close()
    print("Wysłano maila")
wyslij_mail()    
    

def uaktualnij_dane(baza):
    import sqlite3
    import pandas as pd 
    from datetime import datetime, timedelta
    from datetime import date
    import yfinance as yf
    
    conn = sqlite3.connect(baza)
    cursor = conn.cursor()
    
    base_last_date = pd.read_sql_query("SELECT date(max(date)) FROM dane ", con=conn)
    base_last_date = base_last_date.iloc[0,0]
    base_last_date = datetime.strptime(base_last_date , '%Y-%m-%d').date()
    base_last_date = base_last_date + timedelta(days=1)
    today = date.today()
    

    sciezka_tickery = 'C:/Users/adams/OneDrive/Pulpit/tickery.xlsx'
    
    tickery = pd.read_excel(sciezka_tickery,sheet_name='Tickery')
    tickery['Ticker'] = tickery['Ticker'] + ".WA"
    tickers_list = list(tickery['Ticker'])
    
    for spolka in tickers_list:
        data_spolka =pd.read_sql_query('SELECT date(max(date)) FROM dane where spolka =?', 
                                       con=conn, params=[spolka])
        data_spolka = data_spolka.iloc[0,0]
        if data_spolka is not None:
            data_spolka = datetime.strptime(data_spolka , '%Y-%m-%d').date()
            data_spolka = data_spolka + timedelta(days=1)
            today = date.today()
            if data_spolka < today:
                
                dana= yf.download(spolka, start =str(data_spolka) )['Close']
                dana = pd.DataFrame(dana)
                dana["spolka"] = spolka
                dana.reset_index(inplace=True)
                dana=dana[['Date','spolka','Close']]
                dana.to_sql('DANE',conn, if_exists='append',index=False)
                print(spolka +" dane zaktualizowane")
                conn.commit()
            else: print(spolka +' dane sa juz aktualne')
        else: print(spolka + 'jest pusta')

 
 
    
uaktualnij_dane('TEST2')
def wyslij_mail():
    import smtplib 
    mailfrom = 'Rysiek Kitkowski'
    mailTO = 'rysiekkitkowski@gmail.com'
    mailsubject = 'Wykonanie skryptu'
    message_body = '''
    Udalo sie wykonac skrypt. Elo
    '''
    message = ''' From:{}
    Subject: {}
    
    {}
    '''.format(mailfrom, mailsubject, message_body)
    user = "d1837a7b76e5b1"
    password = "51ac76f89a4159"
    
    server = smtplib.SMTP('smtp.mailtrap.io',2525)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user,mailTO,message)
    server.close()
    print("Wysłano maila")
wyslij_mail() 


def maile():
    import smtplib

    sender = "from@example.com"
    receiver = 'mailtrap@example.com'
    
    message = f"""\
    Subject: Hi Mailtrap
    To: {receiver}
    From: {sender}
    
    This is a test e-mail message."""
    
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("d1837a7b76e5b1", "51ac76f89a4159")
        server.sendmail(sender, receiver, message)
    print ('wysłano mail')
maile()
