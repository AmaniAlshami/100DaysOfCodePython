# strip() :  is a method removes any whitespace from the beginning or the end.

a = " Hello Amani "
print(a.strip())
print(len(a)) # return the length of a string
# to make all letter in lower case or upper case 
print(a.lower() + " " + a.upper() )

# replace 'Amani' to 'World' 
b = a.replace("Amani","World")
print(b)
#ues split() method to splits the string into substrings as a list
print(b.split())
