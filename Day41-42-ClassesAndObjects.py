class student:
    def __init__(self,name,level):
        self.student_name = name 
        self.level = level
    
    def info(self):
        print(f"Student Name :{self.student_name} \nLevel :{self.level}")
    def grade(self,grade):
        print(f"Student Name :{self.student_name}\nGrade : {grade}")

Student1 = student(name = "Amani" , level = 7)
Student1.info()
Student1.grade(100)

Student2 = student(name = "Maha" , level = 7)
Student2.info()
Student2.grade(99)

del Student2 

