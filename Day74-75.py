# challenge 1 
# f = open("Python.txt",'x')
# f.write("What is Python language? \nPython is a widely used high-level, general-purpose, interpreted, dynamic programming language.\nIts design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in language such as C++ or Java.\nPython supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles. It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.")
# f.close()
# f = open("Python.txt",'w')
# f.write("￼The best way we learn anything is by practice and exercise questions")
# f.close()
# f = open("Python.txt",'rt')
# print(f.read())
# f.close()

# challenge 2 

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="",
#   database="MyEmployee"
# )

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE MyEmployee")
#mycursor.execute("CREATE TABLE Emolyee (Id INT AUTO_INCREMENT PRIMARY KEY,Fname varchar(30),Lname varchar(30),age INT ,Gender varchar(10),Salary INT)")
# sql = ("INSERT INTO Emolyee(Fname,Lname,age,Gender,Salary) VALUES (%s, %s,%s,%s,%s)")
# val = [
#   ('Ahmed', 'Ali',30,'Male',10000),
#   ('Khalid', 'Muhammad',34,'Male',7000),
#   ('Norah', 'Saleh',29,'Female',7000)
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
mycursor.execute("Select * from Emolyee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
mycursor.execute("Select Fname,Gender,Salary from Emolyee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycursor.execute("Select * from Emolyee order by Fname DESC")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#mycursor.execute("DELETE FROM Emolyee WHERE age = 34 ")
#mydb.commit()
mycursor.execute("Select * from Emolyee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# challenge 3 

f = open("challeng3.txt",'r')
print(f.readlines())
f.close()

