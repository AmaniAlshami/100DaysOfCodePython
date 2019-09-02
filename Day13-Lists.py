# Number 
list1 = [1,2,3,4]
# String
list2 = ["Yellwo","Red","Green"]
# String and Number 
list3 = list1 + list2

print(list3)

# use for loop tp print all items in the list , and can be do any opretor on items
for x in list1:
    print(x*2)

list2[2] = "Blue"
print(list2)

# delete items 
del list3[0:4]
print(list3)

# or can use del to delete list 

del list3

########

lis4 = [x for x in range(0,10)]
print(lis4)

    