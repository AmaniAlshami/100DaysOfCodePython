#global
x = 1 
y = 0
print("global x: ",x)
print("global y: ",y)


def func():
    global y 
    y = 2
    x = 8 
    print("local x : ",x)#local
func()

print("global y after change in func: ",y)

