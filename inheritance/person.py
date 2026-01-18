#class 
class Person: 
     def __init__(self, fname, lname, status): 
          self.fname = fname 
          self.lname = lname 
          self.status = status 

     def speak(self): 
           print(f"Hello, my name is {self.fname} {self.lname} and I am a {self.status}.") 

class Teacher(Person): 
     def __init__(self, fname, lname, status, subject): 
          super().__init__(fname, lname, status) 
          self.subject = subject 

     def teach(self): 
          print(f"I'm teaching {self.subject}.") 

class Student(Person):
     def __init__(self, fname, lname, status, gradeLevel):
          super().__init__(fname, lname, status)
          self.gradeLevel = gradeLevel
    
     def displayGrade(self):
          print(f"My grade is {self.gradeLevel}")

teacher1 = Teacher("Sarah", "Jones", "teacher", "Computer Science")
student1 = Student("Oscar", "Noonan", "student", "87.3")

teacher1.speak() 
teacher1.teach()

student1.speak()
student1.displayGrade()