# Numbers

x = 1 # integer
y = 1.1 # float
z = 1j  # complex

# Use type() function to verify the type of any object in Python

print(type(x))
print(type(y))
print(type(z))

# to convert from one type to another :
a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

# Random Number
# import random module and use random() function
# to  print number (1 - 5)

import random

print(random.randrange(1,6))
