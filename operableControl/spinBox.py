# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:09:19 2020

@author: rachana
"""
from tkinter import *
master = Tk()

w = Spinbox(master, from_ = 1, to = 20)
w.place(x=10, y=10)

master.mainloop()