
import sqlite3

#conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('data.db')


c =conn.cursor() #cursor create


many_customers = [('John','Hann','123_cat@gmail.com','123'),
                  ('Karl','Misy','KarlM@gmail.com','sss'),
                  ('Cumb','Amy','Ammmy@gmail.com','shoes')
                 ]
  
#functions

      #create database
def create_db():
        c.execute(""" CREATE TABLE IF NOT EXISTS customer(
          first_name text,
          last_name  text,
          email text,
          password text   
          )""")
  #customers


def insert():
 c.execute("INSERT INTO customer VALUES('John','Elder','john_elder@gmail.com','123')")
 c.execute("INSERT INTO customer VALUES('Joan','Elon','cactusr@gmail.com','cactus')")
 c.execute("INSERT INTO customer VALUES('Kira','Mis','cactusr@gmail.com','sss')")
 c.execute("INSERT INTO customer VALUES('Mathew','Pop','pop12@gmail.com','12ld')")
 c.execute("INSERT INTO customer VALUES('Karlos','Anders','karrandr@gmail.com','shoes')")
 c.executemany("INSERT INTO customer VALUES (?,?,?,?)", many_customers)

def print():
 c.execute("SELECT * FROM customer")
 print("Users:")
 print("________________________________")
 print(c.fetchall()) #c.fetchmany(3) print last 3

 items = c.fetchall()
 print("")
 print("for login:")
 print("email  \t\t   password:")
 for item in items:
      print(item[2] + "\t\t"  + item[3])
 print("")
 print("Password not strong enough for:")
 print("________________________________")     
 c.execute("SELECT * FROM customer WHERE password LIKE '123%' ")
 



#call functions 


create_db()
insert()

#print("Command executed succesfully...")
conn.commit()

conn.close() #close connection


