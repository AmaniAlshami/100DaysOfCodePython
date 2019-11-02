f = open("Hello.txt",'x')
f.write("Hello world \n file created ! ")
f.close()

f = open("Hello.txt",'rt')
print(f.read())
f.close()

import os 
os.remove("Hello.txt")
