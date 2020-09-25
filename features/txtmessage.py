# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:53:22 2020

@author: rachana
"""
#!/usr/bin/env python
 
import urllib.request
import urllib.parse

apikey = '8qQEb6Lsp8Q-DDYU55wwsNkSeZXvSIGRAwzwrDr9cc'
receiver_phno = '8494942023'
sender_name= ''
message = 'URGENT :You are expected to pay the pending amount of Rs.3600 to the nearest police station strictly by tomorrow, failing which will lead to increase in amount as per standards. Section 192MV -Bangalore Traffic Department'
 
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
resp =  sendSMS(apikey, receiver_phno,
    sender_name, message)
print (resp)