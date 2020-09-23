# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:48:17 2020

@author: rachana
"""
from tkinter import *
window = Tk()

window.geometry('850x500')

w = Label(window, text='hello how are you', font=("Helvetica", 95), fg='yellow', bg = 'white')
w.place(x=10,y=10)

window.mainloop()
