# use recursion to find 5^3 
# this code can be used to solve any exponential equation
def cube(x,y):
    if y > 0:
        r =  x * cube(x,y-1)
    else:
        r = 1
    return r

print(cube(5,3))

###########################
# print positive number by using lambda 
lisNumber = [-4,-6,-5,2,3,7,9,88]
positive = list(filter(lambda i : i > 0 ,lisNumber))
print(positive)

