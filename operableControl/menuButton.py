# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 16:12:13 2020

@author: rachana
"""
from tkinter import *
root = Tk()
root.geometry('500x500')

def fun1():
    root.destroy() #destroy page/window/frame

#menu button
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)

#cascade
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='open..')
filemenu.add_separator()
filemenu.add_command(label='Exit', command = fun1)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='AboutUS')


root.mainloop()