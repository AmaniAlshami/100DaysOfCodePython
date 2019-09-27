# syntax of lambda
# ￼lambda arguments: expression

mult = lambda a , b : a*b

num1 = int(input("Enter frist number : "))
num2 = int(input("Enter second number : "))

print(f"{num1} * {num2} = "+str(mult(num1,num2)))