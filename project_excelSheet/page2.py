# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:18:52 2020

@author: rachana
"""
from tkinter import *
from openpyxl import *
import xlrd

root = Tk()

root.title("Search Name")
root.geometry('380x350')
root.configure(bg="turquoise1")

wb = load_workbook('C:\\Users\\rachana\\Desktop\\demo.xlsx')
sheet = wb.active

wb2 = xlrd.open_workbook('C:\\Users\\rachana\\Desktop\\demo.xlsx')
sheet2 = wb2.sheet_by_index(0)

row = sheet2.nrows
col = sheet2.ncols


def searchName():
    
    for i in range(row):     
        if (sheet2.cell_value(i, 0) == sname_field.get()):
            # print(sheet2.cell_value(i,0))
            # print(sheet2.cell_value(i,2))
            # name_field = StringVar()

            name_field = (sheet2.cell_value(i, 0))
            # sheet2.cell_value(i, 2)= f_field.set()
            # sheet2.cell_value(i, 3)= l_field.set()    

sname = Label(root, text='SearchName').place(x=20,y=20)
sname_field = Entry(root)
sname_field.place(x = 100, y= 20)

search = Button(root, text="Search", command=searchName)
search.place(x=250,y=20)

#name
name = Label(root, text='Name').place(x=20,y=70)
name_field = Entry(root)
name_field.place(x=90,y=70)

#fname
fname = Label(root, text='F-name').place(x=20,y=100)
f_field = Entry(root)
f_field.place(x=90,y=100)

#lname
lname = Label(root, text='L-name').place(x=20,y=130)
l_field = Entry(root)
l_field.place(x=90,y=130)

#gender
gender = Label(root, text='gender').place(x=20,y=160)
gen = Entry(root)
gen.place(x=90,y=160)

#age
ages = Label(root, text='age').place(x=20,y=190)
age = Entry(root)
age.place(x=90,y=190)

#intership
intern = Label(root, text='internship').place(x=20,y=220)
intern_field = Entry(root)
intern_field.place(x=90,y=220)

#month
month = Label(root, text='month').place(x=20,y=250)
month_field = Entry(root)
month_field.place(x=90,y=250)

#StartDate
sdate = Label(root, text='Start-Date').place(x=20,y=280)
date_field = Entry(root)
date_field.place(x=90,y=280)

myWidgets = [sname, name, fname, lname, gender, ages, intern, month, sdate ] # List of widgets to change colour
for i in myWidgets:
    print(wid)
    # wid.configure(bg = turquoise1)

root.mainloop()