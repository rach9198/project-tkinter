# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 10:57:19 2020

@author: rachana
"""
import pyrebase

# 1- create conn.
firebaseConfig = {
    'apiKey': "AIzaSyAQdk-n2JT93qtW6B7y7qe0Gc69d3yuJA4",
    'authDomain': "python-af4e6.firebaseapp.com",
    'databaseURL': "https://python-af4e6.firebaseio.com",
    'projectId': "python-af4e6",
    'storageBucket': "python-af4e6.appspot.com",
    'messagingSenderId': "223351775852",
    'appId': "1:223351775852:web:a06d1ffab58472a697ee49",
    'measurementId': "G-NM746GE82F"
  }

# 2 - initialise firebase object
firebase = pyrebase.initialize_app(firebaseConfig)

# create authentication class obj.
auth = firebase.auth() 

email = input("Enter email ID: ")
pwd = input("Enter password: ")

try:
    auth.sign_in_with_email_and_password(email, pwd)
    print("Sign in successful")

except:
    print("Incorrect credentials")
    
    
    
    
    
    
    
    
    
    