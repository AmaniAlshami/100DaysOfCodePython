import datetime 

time = datetime.datetime.now()
print(time)
print(time.year)

G = datetime.datetime(2021,6,3)

print(G)
print(G.strftime("%B"))
print(G.strftime("%A"))