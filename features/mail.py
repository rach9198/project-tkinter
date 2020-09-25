# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:27:51 2020

@author: rachana
"""
import smtplib 
#simple mail transfer protocol, 

sender_email = "projmailnewrach@gmail.com"
sender_pass = "#projmail#12"

receiver_email = "rachanak0712@gmail.com"
message="helloooo, from spyder"

#smtp gmail server, port number
#port number of google = 80

s = smtplib.SMTP('smtp.gmail.com', 587)

#program ready to send and receive data
s.starttls()



#login
s.login(sender_email, sender_pass)

#1.sender-email-id 2. rec mail 3. msg var
s.sendmail(sender_email, receiver_email, message)