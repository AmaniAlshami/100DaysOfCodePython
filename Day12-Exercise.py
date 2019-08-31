a = "￼Please, I want {} sandwishes and {} donutes"
print(a)
# replase "i"  with "we"
b = a.replace("I","we")
print(b)

# use format 
num1 = 5 
num2 = 7
c = b.format(num1,num2)
print(c)

# capitalize every "a"
def up(txt):
    for i in txt:
      if i == "a" :
        return txt.replace(i,i.upper())
print(up(c))



