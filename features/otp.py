# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:01:52 2020

@author: rachana
"""
import urllib.request
import urllib.parse
import random
from tkinter import *

root = Tk()
root.geometry('500x500')

def generate_otp():
   global final_otp 
   otp = random.randint(1000, 9999)
   print(otp)
   
   sender_no =e1.get()
   apikey = '8qQEb6Lsp8Q-DDYU55wwsNkSeZXvSIGRAwzwrDr9cc'
   # receiver_phno = '8494942023'
   sender_name= ''
   message = otp
   actual_msg = 'your OTP generated for the application is: '+str(message) + sender_no[-5:-1]
   final_otp = str(message) + sender_no[-5:-1]
   
   print(actual_msg)
   
   # data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': sender_no,
   #     'message' : actual_msg, 'sender': sender_name})
   # data = data.encode('utf-8')
   # request = urllib.request.Request("https://api.textlocal.in/send/?")
   # f = urllib.request.urlopen(request, data)
   # fr = f.read()
   
def validate_otp():
    user_entered_otp = e2.get()
    
    if user_entered_otp == final_otp:
        print('success')
    else:
        print('fail')
   
l1 = Label(root, text="Enter contact no.")
l1.place(x=10,y=10)

e1=Entry(root)
e1.place(x=120, y=10)

b1=Button(root, text = "Generate OTP", command=generate_otp)
b1.place(x=250, y =10)

l2 = Label(root, text="Enter OTP")
l2.place(x=10, y=50)

e2 = Entry(root)
e2.place(x=120, y=50)

b2=Button(root, text="Validate OTP", command=validate_otp)
b2.place(x=250, y=50)

root.mainloop()
