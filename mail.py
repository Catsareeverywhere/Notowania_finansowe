# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 23:13:01 2022

@author: adams
"""
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