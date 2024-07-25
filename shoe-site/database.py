import sqlite3


conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_db():
    c.execute("""
        CREATE TABLE IF NOT EXISTS customers1 (
            id TEXT PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT,
            password TEXT,
            age INTEGER
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS shoes (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            discount INTEGER,
            price REAL,
            available BOOLEAN
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS cart (
            customer_id TEXT NOT NULL,
            shoe_id TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers1(id),
            FOREIGN KEY (shoe_id) REFERENCES shoes(id)
        )
    """)
               

               #users functions

def insert_all():
    many_customers1 = [
        ('6', 'John', 'Hann', '123_cat@gmail.com', '123', 17),
        ('7', 'Karl', 'Misy', 'KarlM@gmail.com', 'sss', 29),
        ('8', 'Cumb', 'Amy', 'Ammmy@gmail.com', 'shoes', 45)
    ]
    c.executemany("INSERT INTO customers1 VALUES (?, ?, ?, ?, ?, ?)", many_customers1)

    many_shoes = [
        ('1', 'Nike Air Max', 10, 99.99, True),
        ('2', 'Adidas Ultraboost', 15, 120.50, True),
        ('3', 'Puma Runner', 5, 80.00, False)
    ]
    c.executemany("INSERT INTO shoes VALUES (?, ?, ?, ?, ?)", many_shoes)


def insert_customer(customer):
    c.executemany("INSERT INTO customers1 VALUES (?, ?, ?, ?, ?, ?)", customer)


def add_to_cart(customer_id, shoe_id):
    c.execute("INSERT INTO cart VALUES (?, ?)", (customer_id, shoe_id))


def printf():
    c.execute("SELECT * FROM customers1")
    items = c.fetchall()
    print("Users:")
    print("________________________________")
    for item in items:
        print(item)


def passw():
    print("Password not strong enough for:")
    print("________________________________")
    print("set stronger password:")
    print(" ")
    c.execute("UPDATE customers1 SET password = 'iuski379os' WHERE password LIKE '123%' OR password LIKE '%789'")

def age_over18():
    c.execute("DELETE FROM customers1 WHERE age < 18")


def view_cart(customer_id):
    c.execute("""
        SELECT shoes.name, shoes.price, shoes.discount, shoes.available
        FROM cart
        JOIN shoes ON cart.shoe_id = shoes.id
        WHERE cart.customer_id = ?
    """, (customer_id,))
    items = c.fetchall()
    print(f"Cart for customer {customer_id}:")
    print("________________________________")
    for item in items:
        print(item)



                          #shoes

def discount_special_days():
   c.execute("ALTER TABLE shoes ADD reduced bool")
   c.execute("select date('now')")
   current_date=c.fetchone()[0]
   year, month, day = current_date.split('-')
   if day == '23' and month == '12':
     c.execute("UPDATE shoes SET discount=50 where discount IN(0,10,15) AND available=1")
     reduced=1 
   else:
       c.execute("UPDATE shoes SET discount=5 where discount IN(0,10,15) AND available=1") 
       reduced=0 
   if day == '01' and month == '01':
      c.execute("UPDATE shoes SET discount=50 where discount IN(0,10,15) AND available=1")
      reduced=1  
   if day == '07' and month == '07':
      c.execute("UPDATE shoes SET discount=50 where discount IN(0,10,15) AND available=1")
      reduced=1  
   c.execute("select time('now')")
   current_time=c.fetchone()[0]
   hour, minute = current_time.split(':')
   if hour == '23':
      c.execute("UPDATE shoes SET discount=25 where discount IN(0,10,15) AND available=1")
      reduced=1  
   


def printf_shoes():
 print("________________________")
 c.execute("SELECT * FROM shoes")
 c.execute(" .mode column")
 c.execute(" .tables")
 c.execute(" .schema")
 c.execute("DELETE reduced FROM shoes ")


def backup_all():
    c.execute("SELECT * FROM shoes")
    c.execute(" .backup shoes_bkp.db")
    c.execute("SELECT * FROM cart")
    c.execute(" .backup cart_bkp.db")
    c.execute("SELECT * FROM customers1")
    c.execute(" .backup customers1_bkp.db")

def restore_all():
    c.execute(" .restore shoes_bkp.db")
    c.execute(" .restore cart_bkp.db")
    c.execute(" .restore customers1_bkp.db")             

      
#users 

create_db()
insert_all()
printf()
passw()
age_over18()
add_to_cart('6', '1')
add_to_cart('6', '2')
view_cart('6')
backup_all()




conn.commit()
conn.close()
