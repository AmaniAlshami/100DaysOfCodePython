import json 

# Convert from JSON to Python
x =  '{ "Name":"Ali", "age":40, "city":"Qassim"}'
y = json.loads(x)
print(y["age"])

# Convert from Python to JSON
a = {"name":"Ali","age":40,"city":"Qassim","married":True}
b = json.dumps(a)
print(b)
c = ['Apple','Banana','Orange']
print(json.dumps(c)) # list == arrays
#####################

print(json.dumps(a,indent=3))
print(json.dumps(a,separators=('||',' ')))
print(json.dumps(a,sort_keys=True))