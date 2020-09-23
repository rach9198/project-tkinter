# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:59:07 2020

@author: rachana
"""
import tkinter as tk

from tkinter import ttk

window=tk.Tk()
window.geometry('550x450')
#window.configure(background="black")

#value can be edited so not used

monthchoosen = ttk.Combobox(window)

#adding combobox drop down list
monthchoosen['values'] = ('jan',
                          'feb',
                          'mar',
                          'apr')

monthchoosen.place(x= 30, y=40)
#set current/default value as the first value in array jan
#var_name.current
monthchoosen.current(0)





window.mainloop()