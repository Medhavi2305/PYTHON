import time
numbers = [1, 2, -3, -4, -5, 6, 7, 8, -9, -10]
positive_number_count = 0

for num in numbers:
   if num > 0:
      positive_number_count += 1
print("Total number of positive numbers are", positive_number_count)

for i in range(1, 11):
   if i == 5:
      continue 
   print(3, "x", i, "=", 3 * i)


# REVERSE STRING
reversed_str = ""
for char in "Python":
   reversed_str = char + reversed_str

print(reversed_str)

# FIND THE FIRST NON-REPEATED CHAREACTER
for char in "teeter":
   print(char)
   if "teeter".count(char) == 1:
      print("char is: ", char)
      break

# FACTORIAL CALCULATOR
number = 5
factorial = 1

while number > 0:
   factorial *= number
   number -= 1
print("Factorial", factorial)

# VALIDATE INPUT 
# input_number = input("Enter Number: ")
# validate_number = int(input_number)

# if validate_number > 0 and validate_number < 11:
#    print("Right Number")
# else:
#    print("Please enter number between 1 and 10")

while True:
   number = int(input("Enter a number: "))
   if 1 <= number <= 10:
      print("Right Number")
      break 
   else:
      print("Invalid Number")

# PRIME NUMBER

# while True:
#    number = int(input("Enter a number: "))
#    if number > 1:
#       for i in range(2, number):
#         if (number % 1) == 0:
#            print("Number is prime")
#            break 
#         else: 
#            print("Number is not prime")
#            break 
#    else:
#       print("Please positive Number")

prime_number = int(input("Enter Prime Number: "))

is_prime = True

for i in range(2, prime_number):
   if (prime_number % i) == 0:
      is_prime = False
      break 

print(is_prime)

# LIST UNIQUENESS CHECKER
items = ["Apple", "Banana", "Mango", "Grape", "PineApple", "Apple"]
unique_items = set()

for item in items:
   if item in unique_items:
      print("Unique item", item)
      break 
   unique_items.add(item)

# EXPONENTIAL BACKOFF
wait_time = 1
max_retires = 5
attempts = 0

while attempts < max_retires:
   print(attempts, attempts + 1, "- Wait time", wait_time)
   time.sleep(wait_time)
   wait_time *= 2
   attempts += 1