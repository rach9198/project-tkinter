# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:22:56 2020

@author: rachana
"""
from firebase import firebase
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

# create obj of storage class
storage = firebase.storage()

# to have same path in cloud and db 
path_on_cloud="imgs/dog.jpg"
path_on_local="imgs/dog.jpg"

# child - path on storage. put - img present in path_on local
storage.child(path_on_cloud).put(path_on_local)
