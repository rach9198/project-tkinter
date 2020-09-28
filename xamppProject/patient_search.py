# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 12:50:05 2020

@author: rachana
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:28:04 2020

@author: rachana
"""
from tkinter import *
import pymysql
from tkinter import messagebox

root = Tk()
root.title('Search Patient Details')
root.geometry('400x350')
root.configure(bg = "green2")

def search_data():
    try:
        connection = pymysql.connect(host='localhost', user='root', password='', database='python')
        
        cursor = connection.cursor()
        
        pid = pid_field.get()
        
        
        query = '''select * from patient where pid = %s'''
        cursor.execute(query, pid)
        
        data = cursor.fetchall() # data datattype - tuple
        # print(data)
        if data:
            
            for each_data in data:
            # print(each_data)
                # print(each_data) #prints only projName - access using index
                name = each_data[1]
                fname = each_data[2]
                dis = each_data[3]
                ph_no = each_data[4]
        
            messagebox.showinfo("Message", "data found successfully")
            
            pname = Label(root, text="Patient name: " +name)
            pname.place(x=10, y =60)
            
            pfname = Label(root, text="Father's name: " +fname)
            pfname.place(x=10, y=100)
            
            disease = Label(root, text="Disease: " +dis)
            disease.place(x=10, y=140)
            
            phno = Label(root, text="Contact No: " +ph_no)
            phno.place(x=10, y=180)
        
        else:
            messagebox.showinfo("Message", "data not found")
        
        connection.commit()
        connection.close()
        
    except:
        print('Error, data not found')
        
        messagebox.showinfo("Message", "data not found")
    
    
    
    
pid = Label(root, text="Patient ID")
pid.place(x=10, y=10)

pid_field = Entry(root)
pid_field.place(x= 100, y=10)

sbutton = Button(root, text = "Search", command=search_data)
sbutton.place(x=250, y=10)


root.mainloop()