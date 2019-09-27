# use return in function & pass list as a parameter 


number = [x for x in range(1,11)]
def sum(lis):
    sum = 0
    for x in lis:
        sum += x
    return sum 

print(sum(number))

# Recursion     
def factorial(n):
    if n == 0 or n == 1:
        return 1 
    else :
        return n*factorial(n-1)

print(factorial(10)) 


