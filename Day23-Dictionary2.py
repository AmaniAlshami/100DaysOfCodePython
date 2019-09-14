Student = { 'Name':'Amani','ID':1, 'Mark':100}
# Check if Key Exists
if 'Name' in Student:
    print("Yes")
# length 
print(len(Student))
# Adding Items
Student['Age'] = 21

print(Student)
# Removing Items
Student.popitem() # remove last inserted item 
Student.pop('Mark') # remove item with the specified key name
print(Student)
Student.clear() # remove all items 
print(Student)
del Student # delete the dictionary completely
