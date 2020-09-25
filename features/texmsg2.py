# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:09:44 2020

@author: rachana
"""
#dynamic server request package
#json = data will go in json formet not plaini text
import requests #help in establishing conn. and object transfer
import json #data structure  - dict and tuple

#mention url
url = "https://www.fast2sms.com/dev/bulk"
#sender_phno='7619190486'

# message = "fst3sms test msg"
#create dictionary key &value

my_data = {
    'sender_id': 'FSTSMS',
    'message': 'fst3sms test msg', 
    
    'language': 'english',
    'route': 'p', 
    'numbers': 7619190486
}

#create authorixation doct

headers = {
    'authorization': 'ehX0fqukNSQ3zm9t1BbZ4JUsKHxrPOnpVic2dyoWv5ajMl8gTL4YM79kSC51tbIEK6yVjDwQFsmfB0ha',
    'content-Type':"application/x-www-form-urlencoded",
    'Cache-Control': "no-cache"
}


#make a post request
response = requests.request("POST",
                           url,
                           data = my_data,
                           headers = headers)

#load json data from source
returned_msg = json.loads(response.text)


#print the send message
print(returned_msg['message'])



