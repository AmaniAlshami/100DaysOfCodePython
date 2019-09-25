# simple function 

def Hello():
    print("Hello world")

# function with parameter

def Hello2(name):
    print("Hello "+name)



# calling function 
Hello()
name = input("Enter your name : ")
Hello2(name)

# default parameter value 

def sum(num1 = 1 , num2 = 1):
    print(num1+num2)

sum()
sum(2,3)