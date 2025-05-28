import sqlite3
#connect to sqlite
connection=sqlite3.connect("warehouse.db")

#create a cursor object to insert record,create table,retrieve
cursor=connection.cursor()

cursor.execute("DROP TABLE IF EXISTS product")

#Create the products table
table_info="""
Create table product (NAME VARCHAR(25),PRICE int,STOCK int, SOLD int);
"""

cursor.execute(table_info)
#insert some more records
cursor.execute("INSERT INTO product values('Soaps',50,20,30)")
cursor.execute("INSERT INTO product values('Notebook',39,150,15)")
cursor.execute("INSERT INTO product values('Smartphone case',199,50,45)")
cursor.execute("INSERT INTO product values('Towels',250,80,15)")
cursor.execute("INSERT INTO product values('Peanut butter',325,45,20)")
cursor.execute("INSERT INTO product values('tshirts',200,60,12)")
cursor.execute("INSERT INTO product values('Maggie',50 ,10,20)")
# DISPLAY ALL THE RECORDS
print("The inserted records are")
data=cursor.execute('''Select * From PRODUCT ''')
for row in data:
    print(row)

#close the connection
connection.commit()
connection.close()