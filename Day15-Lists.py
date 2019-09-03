 # To Know length of list 
list1 = [i for i in range(0,100)]
print(len(list1))

list2 = ['Red','blue','green']

# To add new item 
list2.append('pink')
# To add an item at the specified index
list2.insert(2,'Red')
print(list2)
################################

# To copy list 
list3 = list2.copy()
print(list3)
# OR 
list4 = list(list2)
print(list4)
# use the list() constructor to make a new list.
list5 = list(('A','B','C'))
print(list5)
###################################

# To remove item
list2.remove('Red') # remove frist item have 'Red' value 
list2.pop(2) # remove item in index 2 
list2.pop() # remove last item 
print(list2)

list2.clear() # remove all items 
print(list2) 

###############################







