# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:28:00 2020

@author: rachana
"""
import tkinter as tk
window = tk.Tk()

window.title("GUI")
window.geometry('500x500')
window.configure(background="black")

button = tk.Button(window) #will not be seen
#button = Button(window) if imported *

#to be seen - need to place
button.place(x=10, y=10)

tk.Button(window).place(x=30, y=10)

def user_name():
    #window2=tk.Tk()
    #window2.geometry('500x500')
    #window2.configure(background="black")
    #window2.mainloop()
    #print("hello")
    
    import sec_window

#confugure button
button2 = tk.Button(window, text = 'Stop', width =25, height=5, activebackground='red', activeforeground='red', command=user_name)
button2.place(x=40,y=50)



#command -user defined name














window.mainloop()