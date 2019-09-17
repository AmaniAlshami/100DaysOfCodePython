# IF - Else 

num1 = int(input("Enter frist number  : "))
num2 = int(input("Enter second number  : "))

if num1 > num2 :
    print(str(num1)+" greater than "+str(num2))
else:
    print(str(num2)+" greater than "+str(num1))

#elif , and , or 

grade = int(input("Enter Grade : "))

if grade < 0 or grade > 100:
    print("invalid range ! , 0 - 100")
elif grade >= 90 and grade <= 100 :
    print("A")
elif grade >= 80 and grade < 90 :
    print("B")
elif grade >= 70 and grade < 80 :
    print("C")
elif grade >= 60 and grade < 70 :
    print("D")
else:
    print("F")

# nested if 
# check number is between 20 - 40 and even
num3 = int(input("Enter Number  : "))

if num3 >= 20 and num3 <= 40 :
    if num3%2==0 :
        print(f"yse {num3} between 20 - 40 and even ") 
    else :
        print("NO")


