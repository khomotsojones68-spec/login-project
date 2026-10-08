#creating A DATABASE FOR LOGINS!!!
import sqlite3


# creating a database named login 

conn= sqlite3.connect("login.sqlite")

cur=conn.cursor()
#create table id, username,pin

cur.execute("DROP TABLE IF  EXISTS details")
cur.execute("CREATE  TABLE   details(id INTEGER PRIMARY KEY , username TEXT UNIQUE, pin INTEGER UNIQUE)")
#insert rows
cur.execute("INSERT INTO  details(id , username,pin ) VALUES(1, 'tumelo',4478)")
cur.execute("INSERT INTO   details(id , username,pin ) VALUES(2,'katliso',7228)")

conn.commit()






#user login
while True: 
    try:
     name=input("enter username :  ")
     pin=int(input("enter pin:  "))


     cur.execute("SELECT * FROM details WHERE username=? AND pin=?", (name,pin ))
     user=cur.fetchone()
     if user:
        print(f"welcome {name}")
        break
     else:
        print("incorrect details")
    except Exception as e:
      print(e)
      
 
conn.close()