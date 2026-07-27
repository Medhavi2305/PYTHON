# Find User age
age = input("Your Age: ")
int_age = int(age)

if int_age < 13:
   print("child")
elif int_age < 20:
   print("teenage")
elif int_age < 60:
   print("adult")
elif int_age > 101:
   print('are you really alive')
else:
   print('senior')

day = input("what is the day: ")
price = "$12" if int_age >= 18 else "$8"

if int_age < 13 and day == "wednesday":
   print("You are child and today is wednesday you will get $2 discount on $8")
elif int_age > 19 and day == "wednesday":
   print("you are adult you will get $2 discount on $12")
else:
   print("$8 for child and $12 for adult")

# if day == "wednesday":
#    price -= "$2"
#    print(price)
# else:
#    print(price)