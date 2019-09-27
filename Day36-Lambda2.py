# Use lambda functions when an anonymous function is required for a short period of time


def multipleByTwo(n):
    return lambda a : a * n

num = int(input("Enter number : "))
a = multipleByTwo(2)

print(a(num))
