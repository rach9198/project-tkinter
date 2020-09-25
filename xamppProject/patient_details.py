# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:28:04 2020

@author: rachana
"""
from tkinter import *
import pymysql
from tkinter import messagebox

root = Tk()
root.title('Patient Details')
root.geometry('500x500')
root.configure(bg = "purple2")

def insert_data():
    
    connection = pymysql.connect(host='localhost', user='root', password='', database='python')
    
    cursor = connection.cursor()
    pid = pid_field.get()
    pname = pname_field.get()
    pfname = pfname_field.get()
    disease = dis_field.get()
    phno = phno_field.get()
    
    print(pid+pname+pfname)
    insert_query = '''insert into patient(pid,pname,pfname,disease,phno) values(%s,%s,%s,%s,%s)'''
    cursor.execute(insert_query, (pid, pname, pfname, disease, phno))
    
    connection.commit()
    connection.close()
    
    messagebox.showinfo("Message", "data inserted successfully")
    
    
pid = Label(root, text="Patient ID")
pid.place(x=10, y=10)

pid_field = Entry(root)
pid_field.place(x= 100, y=10)

pname = Label(root, text="Patiend name")
pname.place(x=10, y =40)

pname_field=Entry(root)
pname_field.place(x=100, y=40)

pfname = Label(root, text="Father's name")
pfname.place(x=10, y=80)

pfname_field = Entry(root)
pfname_field.place(x=100, y=80)

disease = Label(root, text="Disease")
disease.place(x=10, y=120)

dis_field = Entry(root)
dis_field.place(x=100, y=120)

phno = Label(root, text="Contact No")
phno.place(x=10, y=160)

phno_field = Entry(root)
phno_field.place(x=100, y=160)

submit = Button(root, text="Submit", command=insert_data)
submit.place(x=300,y=300)

root.mainloop()