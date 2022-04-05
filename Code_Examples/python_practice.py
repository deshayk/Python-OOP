def Work(): # class definition
  
    def employee(self, name, email, pay): # method definition
        self.name = name # instance variable
        self.email = email # instance variable
        self.pay = pay # instance variable

    def employer(self, name): # method definition
        self.name = name # instance variable
        
w1 = Work() # create instance
w1.employee('John', 'johnjacob@python.inc', '$100') # call method
print(w1.name) # access instance variable
print(w1.email) # access instance variable
print(w1.pay) # access instance variable

j1 = Work() # create instance
j1.employer('Python Inc.') # call method
print(j1.name) # access instance variable