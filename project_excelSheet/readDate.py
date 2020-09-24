# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:57:13 2020

@author: rachana
"""

# from tkinter import *

# root=Tk()


import xlrd


wb2 = xlrd.open_workbook('C:\\Users\\rachana\\Desktop\\demo.xlsx')
sheet2 = wb2.sheet_by_index(0)


value = sheet2.cell_value(1,0)
print(value)

rows=sheet2.nrows
col = sheet2.ncols

print(rows)
print(col)

for i in range(rows):
    # print(sheet2.cell_value(i,0))
    
    #authentication
    if(sheet2.cell_value(i,0) == "ram"):
    
root.mainloop()


