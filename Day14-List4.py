lis1 = [1,2,3,4,5,6]
print(lis1[2:5])


# use in to check item is in list or not 
colorsList= ["Yellow","red","black",'green']
color = input("Enter color : ").lower()
def check(color):
    if (color in colorsList):
        print(f"Yes {color} is in our colors list")
    else:
        print(f"{color} is not in our colors list")
check(color)

# repeat any item in list 
lis = ["Python"] * 5 
print(lis)

integer = [1,2,3,4]
floating = [1.5,2.2,3.8,4.6]
print(integer + floating)


