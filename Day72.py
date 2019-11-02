import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

 # order by 
mycursor = mydb.cursor()

mycursor.execute("Select * from customers order by name ")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycursor.execute("Select * from customers order by name DESC")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
# delete 

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record deleted ")
# drop 
# mycursor.execute("DROP TABLE customers") 
mycursor.execute("DROP TABLE IF EXISTS customers")

