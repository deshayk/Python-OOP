# Remember, self will be replaced by whatever object is being created.     

class Car: # establishes Car class
  def __init__(self, make, model, year, color): # initializes the class, self is the instance of the class (object) and takes four arguments
      self.make = make #instance variable (attribute)
      self.model = model #instance variable (attribute)
      self.year = year #instance variable (attribute)
      self.color = color #instance variable (attribute)
  
  def drive(self): # method (action) that indicates the car is moving
      print("The car is driving.")
      
  def brake(self): # method (action) that indicates the car is stopping
      print("The brakes have been hit. The car is stopping.")
    