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
    
car_1 = Car("Honda", "Civic", "2019", "Red") #instantiate a new object of the class Car with the required arguments
car_2 = Car("Toyota", "Corolla", "2020", "Blue") #instantiate a new object of the class Car with the required arguments
car_3 = Car("Ford", "F150", "2021", "White") #instantiate a new object of the class Car with the required arguments
car_4 = Car("Chevy", "Camaro", "2022", "Black") #instantiate a new object of the class Car with the required arguments
car_5 = Car("Dodge", "Charger", "2023", "Yellow") #instantiate a new object of the class Car with the required arguments

car_1.drive()
car_3.drive()
car_5.drive()