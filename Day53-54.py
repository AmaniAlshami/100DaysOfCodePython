import Calculate as c 


print("1 + 8 = ",c.sum(8,1))
print("4 - 2 = ",c.sub(4,2))
print("6 * 6 = ",c.mult(6,6))
print("8 / 2 = ",c.dev(8,2))


###########################

import datetime 

time = datetime.datetime.now()
print(time)
print(time.year)
print(time.month)
print(time.day)

###########################
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
print("yesterday : " ,yesterday)

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
print("tomorrow : " ,tomorrow)