class Student():
  def __init__(self, name, major, gpa, year):
    self.name = name
    self.major = major
    self.gpa = gpa
    self.year = year
    
  def greet():
    print("Hello ", self.name, "!")
    print("Welcome to Python University")
    print("While at PU, you will be a full-time", self.major, "major!")
    print("You will be in the class of", self.year, "and right now you have a GPA of", self.gpa, ".")
    print("You will be a Python Master by the end of the semester.")
    
student1 = Student("John", "Computer Science", 3.9, 2019)
student2 = Student("Jane", "Math", 3.5, 2020)
student3 = Student("Jack", "Physics", 3.7, 2021)
student4 = Student("Jill", "Biology", 3.8, 2022)
student5 = Student("Joe", "Chemistry", 3.9, 2023)