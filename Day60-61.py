#Challenge1
# create tuple and convert to string by using JSON
import json
week = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')

print(json.dumps(week))

#Challenge2
import re

txt = 'data is the new oil'
ser = re.search('data',txt)
print(ser.group())



