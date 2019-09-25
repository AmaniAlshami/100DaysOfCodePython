# list odd number 3 - 17 
# list even number 2 - 16

odd = [x for x in range(3,18,2)]
even = [x for x in range(2,17,2)]

for x in odd:
    for y in even:
        print(y,x)
    