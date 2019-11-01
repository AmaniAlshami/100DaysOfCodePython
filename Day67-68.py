# Challenge1 
name = input("Enter your name :")
print("The frist letter in your name is : {} and the last is :{}".format(name[0],name[-1]))

# Challenge2

print("Dear Ahmad Ali, Your current balance is {bal} $".format(bal=53.44))

# Challenge3 
arr=[] 
arrNum = int(input("Enter number of element : "))

for x in range(arrNum):
   arr.append(input("Enter value : "))

for i in arr:
    print(i, end=" ")

     