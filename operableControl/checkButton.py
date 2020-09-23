# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:50:04 2020

@author: rachana
"""
#from tkinter import *
import tkinter as tk

window = tk.Tk()

window.title("GUI")
window.geometry('550x450')
window.configure(background="black")


b=tk.Checkbutton(window, text="male")
b.place(x=50,y=60)


window.mainloop()