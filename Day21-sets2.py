colors ={'Red','Blue','Pink','Black'} 



# remove , if item not in the set will get an erorr
colors.remove("Black")
# discard()
colors.discard('white')

# use len() to know length of Set 
print(len(colors))

# pop() : return last item in set
print(colors.pop())
# clear : delete all items
colors.clear()
print(colors)
# del : delele the set 
del colors

color = set(('Red','Blue','Pink','Black'))
print(color)

