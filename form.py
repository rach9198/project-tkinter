import tkinter as tk 

from tkinter import *
from tkinter import ttk
# from tkinter import dkk

root = tk.Tk()

root.geometry('500x500')

heading = tk.Label(root, text = 'Application form')
heading.pack()


gender = tk.Label(root, text = 'Gender').place(x=10, y=30)
r1 = tk.Radiobutton(root, text = "Male").place(x=60, y= 30)
r2 = tk.Radiobutton(root, text = "Female").place(x=120, y= 30)
r3 = tk.Radiobutton(root, text = "Other").place(x=190, y= 30)

skills = tk.Label(root, text = 'Skills you know').place(x=10, y=60)
s1 = tk.Checkbutton(root, text='C').place(x=10, y=80)
s2 = tk.Checkbutton(root, text='C++').place(x=10, y=100)
s3 = tk.Checkbutton(root, text='Java').place(x=10, y=120)
s4 = tk.Checkbutton(root, text='Python').place(x=10, y=140)


dept = tk.Label(root, text = 'Your department').place(x=10, y=180)

depts = ttk.Combobox(root)
depts['values']=('CSE', 'ISE', 'ECE', 'EEE', 'MECH', 'CIV')
depts.place(x=130, y=180)


dob = tk.Label(root, text = 'DOB').place(x=10, y=260)
# dobsel = tk.DateEntry(root).place(x=25, y=260)

cgpa = tk.Label(root, text = 'CGPA').place(x=10, y=300)
cgpasel = tk.Spinbox(root, from_ = 0.0, to = 10.0).place(x=55, y=300)


submit = tk.Label(root, text = "SUBMIT", width="15",height="2", bg = "black", fg="white").place(x = 375, y = 450)





root.mainloop()
