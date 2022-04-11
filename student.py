class Student():
  def __init__(self, name, major, gpa, year): # initializes the class, self is the instance of the class (object) and takes four arguments
    self.name = name #instance variable (attribute)
    self.major = major #instance variable (attribute)
    self.gpa = gpa #instance variable (attribute)
    self.year = year #instance variable (attribute)
    
  def greet():
    print("Hello ", self.name, "!")
    print("Welcome to Python University")
    print("While at PU, you will be a full-time", self.major, "major!")
    print("You will be in the class of", self.year, "and right now you have a GPA of", self.gpa, ".")
    print("You will be a Python Master by the end of the semester.")

student1 = Student("John", "Computer Science", 3.9, 2019) #instantiate a new object of the class Student with the required arguments  
print(student1.name) #prints the name of the object
print(student1.major) #prints the major of the object
print(student1.gpa) #prints the gpa of the object
print(student1.year) #prints the year of the object
student2 = Student("Jane", "Math", 3.5, 2020) #instantiate a new object of the class Student with the required arguments  
student3 = Student("Jack", "Physics", 3.7, 2021) #instantiate a new object of the class Student with the required arguments  
student4 = Student("Jill", "Biology", 3.8, 2022) #instantiate a new object of the class Student with the required arguments  
student5 = Student("Joe", "Chemistry", 3.9, 2023) #instantiate a new object of the class Student with the required arguments  