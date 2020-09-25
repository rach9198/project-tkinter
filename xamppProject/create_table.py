# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:39:09 2020

@author: rachana
"""
import pymysql

# creating database conn.
connection = pymysql.connect(host='localhost', user='root', password='', database = 'python')

#creating cursor - perform all operations crud
cursor = connection.cursor()

# perform operations
# task1 - create table

# query ='''create table project2(
#     projid char(10),
#     projname char(10))'''

# # execute
# cursor.execute(query)




#task2 - insert data

# values directly
# insert_query = '''insert into project2 values('qw12','feature')'''
# cursor.execute(insert_query)

# # pass values from user 
# projid = input("Enter Proj ID: ")
# projname = input("Enter proj name: ")

# query_user = '''insert into project2 values(%s,%s)'''
# cursor.execute(query_user, (projid, projname))




# task3 - display 
# select_query = '''select * from project2'''
# cursor.execute(select_query)

# data = cursor.fetchall() # data datattype - tuple
# print(data)

# for each_data in data:
#     # print(each_data)
#     print(each_data[1]) #prints only projName - access using index
    



# task 4 - updating the database
# update_query = '''update project2 set projname = 'java' where projid = 'vid12' '''
# cursor.execute(update_query)

# # update custom var
# projname = input("enter projname")
# projid = input("enter projid")

# update_query2 = '''update project2 set projname=%s where projid = %s '''
# cursor.execute(update_query2, (projname, projid))




# task5 - delete 
delete_query = '''delete from project2 where projid = 'vid12' '''
cursor.execute(delete_query)

    
# to save data perm..
connection.commit()
connection.close()


