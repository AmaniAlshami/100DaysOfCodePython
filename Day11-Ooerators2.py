# Logical Operators

x = int(input("Enter grade : "))
if x < 0 or x > 100:
    print("invalid range ! , 0 - 100")
elif x >= 90 and x <= 100 :
    print("A")
elif x >= 80 and x < 90 :
    print("B")
elif x >= 70 and x < 80 :
    print("C")
elif x >= 60 and x < 70 :
    print("D")
else:
    print("F")

# Identity Operators : used to compare the objects .

y = "Hello"
z = "World"
w = y # have the same location in the memory ..

print(y is z)
print(w is y) 
print(z is not y)

# Membership operators are used to test if a sequence is presented in an object.

color = ["Red","Green","Blue"]

print("yellow" in color)
print("Red" in color)


# Bitwise Operators 

a = 15    # 1111
b = 14    # 1110
c = a & b # 1110
d = a | b # 1111
print(c)
print(d)


