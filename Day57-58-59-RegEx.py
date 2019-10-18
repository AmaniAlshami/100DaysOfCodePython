import re 

txt = "The rain in Spain"

Search1 = re.search("^The", txt)
if Search1 :
    print("Yse")
Search2 = re.search(r"\br\w+", txt)
print(Search2.span())
print(Search2.group())

find = re.findall('in',txt)
print(find)

split = re.split(' ',txt)
print(split)

re = re.sub(' ',':',txt,1)
print(re)
 

 ######################

