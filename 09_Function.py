#-1 Basic Function Syntax (Write function to find square of a number)
def square_of_number(number):
   return number ** 2

result = square_of_number(3)
#-2 Function With Multiple Parameters
#-3 Polymorphism in Function
#-4 Function Returning Multiple Values (Create a function that return both area and circumfrence of a circle given its radius till two presicicion)
#-5 Default Parameter Values 
#-6 Lambda Function
#-7 Function With *args
#-8 Function With **Kwargs (Create a function that accepts any number of keyword arguments and print them in the format key: value)
def print_kwargs(**kwargs):
   for key, value in kwargs.items():
      print(f"{key}: {value}")
#-9 Genrator Function With Yield (Write a genrator function that yields even numbers upto a specificied limits)
def even_number_genrator(limit):
   for i in range(2, limit + 1, 2):
      yield i # Understand it it store function in refrence

for num in even_number_genrator(10):
   print(num)
#-10 Recursive Function
def factorial(n):
   if (n == 0):
      return 1
   else: return n * (factorial - 1)