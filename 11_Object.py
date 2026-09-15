#-1 Basic Class And Object - Create a car class class with attribute like brand and model. Then Create an intance of this class
class Car:
   total_number_of_car_created = 0 #-6 Class Variable - Add a class variable to car that keeps track of the number of cars created.

   def __init__(self, brand, model):
      self.__Brand = brand
      self.__Model = model
      Car.total_number_of_car_created += 1 # (This type of method also used in to keeping the track how many times the object is created)
#      self.total_number_of_car_created += 1 #-6 Class Variable - Add a class variable to car that keeps track of the number of cars created.

   def get_brand(self): #-4 Encapsulation - Modify the class to encapsulate the brand attribute, making it private, and provide a getter method for it
      return self.__Brand

   def fuel_type(self): #-5 Polymorphism - Demonstrate polymorphism by defineing a method fuel_type in both car and electric car classes but with diffrent behaviour
      return "Petrol or Diseal"

   def full_name(self): #-2 Class Method And Self - Add a method to the car class that displays the full name of the car (brand and model)
      return f"{self.__Brand}: {self.Model}"

   @staticmethod #-7 Static Method - Add a static method to a car class that return a genral description of a car
   def genral_discription():
      return "Car are best mean of transport"

   @property #-8 Property Decorators - Use a property decorators in the class to make the model attribute read-only 
   def Model(self):
      return self.__Model

my_Car = Car("Toyota", "Corolla")
# print(my_Car.Brand)
print(my_Car.Model)
#my_Car.__Model = "xyz" (You cant change the object propery it is now read only) 
print(f"Car Fuel is :- {my_Car.fuel_type()}")

#-3 Inheritence - create an electricCar class that inherits from the car class nad has additional attribute battery_size.
class ElectricCar(Car):
   def __init__(self, brand, model, battery_size):
      super().__init__(brand, model)
      self.Battery_Size = battery_size

   def fuel_type(self): #-5 Polymorphism - Demonstrate polymorphism by defineing a method fuel_type in both car and electric car classes but with diffrent behaviour
         return "Electric Charge"

Tesla = ElectricCar("Tesla", "Model S", "100kWh")
print(Tesla.full_name())
print("Getter Method",Tesla.get_brand()) # This how you get encapsulated attribute
print(f"Electric car fuel type :- {Tesla.fuel_type()}")
print("Total Number of Cars: ", Car.total_number_of_car_created)
print(my_Car.genral_discription())
print(Car.genral_discription())
#-9 Class Inheritance And Isinstance() Function - Demonstrate the use of instance() to check if Tesla is an instance of Car or ElectricCar
print(isinstance(Tesla, Car))
print(isinstance(Tesla, ElectricCar))
#-10 Multiple Inheritance - Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance 
class Battery:
   def battery_info(self):
      return "This is battery info"

class Engine:
   def engine_info(self):
      return "This is Engine info"

class ElectricCarTwo(Battery, Engine, Car):
   pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
# Study About Setter In Python