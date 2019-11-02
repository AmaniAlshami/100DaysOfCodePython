import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)


mycursor = mydb.cursor()

# UPDATE :

# mycursor.execute("UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'")
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

# LIMIT 
mycursor.execute("SELECT * FROM customers LIMIT 5 offset 3")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# JOIN 

sql = "SELECT \
  customers.name AS user, \
  product.name AS favorite \
  FROM customers \
  INNER JOIN product ON customers.PID = product.ID"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

