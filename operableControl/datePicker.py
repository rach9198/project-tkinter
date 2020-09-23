# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:30:59 2020

@author: rachana
"""

from tkinter import *
root = Tk()
root.geometry('500x500')

from tkcalendar import DateEntry

#datepicker
cal = DateEntry(root, width=12, year=2019, month=7, day=21, bg='darkblue', foreground='white', borderwidth='8' )
cal.place(x=50, y=50)



root.mainloop()