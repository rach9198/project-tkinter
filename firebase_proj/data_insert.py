# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:09:45 2020

@author: rachana
"""
# pip install requests
# pip install firebase
import requests
from firebase import firebase

# pip install sseclient


firebase = firebase.FirebaseApplication('https://python-af4e6.firebaseio.com')

# data is always isnerted in form of dictionary -key-value pairs
data = {
        'p_id': 'p2',
        'p_name': 'asdfgh',
        'disease': 'viral',
        'phno': '987654321'}

obj = firebase.post('/hospital/svit', data)
print(obj) #prints id

