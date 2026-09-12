#-1 Basic Class And Object - Create a car class class with attribute like brand and model. Then Create an intance of this class
class Car:
   def __init__(self, brand, model):
      self.__Brand = brand
      self.Model = model

   def get_brand(self): #-4 Encapsulation - Modify the class to encapsulate the brand attribute, making it private, and provide a getter method for it
      return self.__Brand

   def fuel_type(self): #-5 Polymorphism - Demonstrate polymorphism by defineing a method fuel_type in both car and electric car classes but with diffrent behaviour
      return "Petrol or Diseal"

   def full_name(self): #-2 Class Method And Self - Add a method to the car class that displays the full name of the car (brand and model)
      return f"{self.__Brand}: {self.Model}"

my_Car = Car("Toyota", "Corolla")
# print(my_Car.Brand)
print(my_Car.Model)
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
#-6 Class Variable - Add a class variable to car that keeps track of the number of cars created.
#-7 Static Method
#-8 Property Decorators
#-9 Class Inheritance And Isinstance() Function
#-10 Multiple Inheritance




# Study About Setter In Python