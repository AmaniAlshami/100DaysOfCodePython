color = tuple(("Red","Green","Yellow","Red"))
fruits = ('Apple','Banana','Orange')
Number= (1,2,3)
Number = Number + (4,5,6)


def check(fruits):
    fruit = input("Enter fruti name : ")
    if fruit in fruits :
        print("Yes")
    else:
        print("No")


print(color[:1])
print(color.count("Red"))
check(fruits)
print(color.index('Green'))
print(Number)
print(len(Number))


