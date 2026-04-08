class Student:
  def __init__(self, name, cgpa):
    self.name  = name
    self.cgpa = cgpa
  subject = "Python"
  college = "ABC"
  year = "4th year"
  
  def get_cgpa(self):
    return self.cgpa

stu1 = Student("Rahul", 9.0)  
stu2 = Student("Urvashi", 9.2)  
print(stu1.name, stu1.cgpa, stu1.subject, stu1.college, stu1.year)
print(stu2.name, stu2.cgpa, stu2.subject, stu2.college, stu2.year)

print(stu1.get_cgpa())
