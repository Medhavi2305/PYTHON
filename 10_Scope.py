x = 99

def func():
   global x # THis will change the global variable 
   x=12

func()
print(x) 