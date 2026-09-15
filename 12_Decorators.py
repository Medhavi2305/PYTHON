#-1 Timming function Execution - Write a decorator that measures the time a function takes to execute
import time

def timer(func):
   def wrapper(*args, **kwargs):
      start = time.time()
      result = func(*args, **kwargs)
      end = time.time()
      print(f"{func.__name__} ran in {end-start} time")
      return result
   return wrapper

@timer
def sleep_function(n):
   time.sleep(n)

sleep_function(5)
#-2 Debugging Function Calls - Create a decorator to print the function name and the values of its arguments every time the function is called.
def debug(func):
   def wrapper(*args, **kwargs):
      args_value = ', '.join(str(arg) for arg in args)
      kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
      print(f"{func.__name__} with args {args_value} and kwargs {kwargs_value}")
   return wrapper

@debug
def greet(name, greeting="Hello"):
   print(f"{greeting}, {name}")

greet("Medhavi", greeting="Hanji")
#-3 Cache Retrun Values - implement the decorator that cache the retrun values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function
def cache(func):
   cache_value = {}
   print(cache_value)
   def wrapper(*args):
      if args in cache_value:
         return cache_value
      result = func(*args)
      cache_value[args] = result
      return result
   return wrapper

@cache
def long_running_function(a, b):
   time.sleep(2)
   return a+b

print(long_running_function(2, 3))
print(long_running_function(5, 5))