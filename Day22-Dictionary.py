Student = { 'Name':'','ID':'', 'Mark':''}

Student['Name'] = input('Enter Student name : ')
Student['ID'] = int(input('Enter Student ID : '))
Student['Mark'] =float(input('Enter Mark : '))

for i in Student:
    print(Student[i])

