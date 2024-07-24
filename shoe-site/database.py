
import sqlite3

#conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('data.db')


c =conn.cursor() #cursor create


many_customers1 = [('6','John','Hann','123_cat@gmail.com','123',17),
                  ('7','Karl','Misy','KarlM@gmail.com','sss',29),
                  ('8','Cumb','Amy','Ammmy@gmail.com','shoes',45)
                 ]



  
#functions

      #create database
def create_db():
        c.execute(""" CREATE TABLE IF NOT EXISTS customers1(
          id text,
          first_name text,
          last_name  text,
          email text,
          password text,
           age number          
          )""")
  #customers1


def insert_all():
 c.execute("INSERT INTO customers1 VALUES('1','John','Elder','john_elder@gmail.com','123',13)")
 c.execute("INSERT INTO customers1 VALUES('2','Joan','Elon','cactusr@gmail.com','cactus',34)")
 c.execute("INSERT INTO customers1 VALUES('3','Kira','Mis','cactusr@gmail.com','sss',19)")
 c.execute("INSERT INTO customers1 VALUES('4','Mathew','Pop','pop12@gmail.com','12ld',16)")
 c.execute("INSERT INTO customers1 VALUES('5','Karlos','Anders','karrandr@gmail.com','shoes',25)")
 c.executemany("INSERT INTO customers1 VALUES (?,?,?,?,?,?)", many_customers1)



def insert(customer):
    c.executemany("INSERT INTO customers1 VALUES (?,?,?,?,?,?)", customer)


def printf():
 c.execute("SELECT * FROM customers1")
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

def passw(): 
 print("Password not strong enough for:")
 print("________________________________") 
 print("set stronger password:")    
 print(" ")
 c.execute("""UPDATE customers1 SET password = 'iuski379os' WHERE password LIKE '123%' OR password LIKE '%789' """)

def age_over18():
 c.execute("SELECT age, * FROM customers1 ORDER BY age CRESC")
 c.execute("DELETE from customers1 WHERE age LIMIT 17")



#call functions 
create_db()
insert()
printf()
passw()
age_over18()


#print("Command executed succesfully...")
conn.commit()

conn.close() #close connection


