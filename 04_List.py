# List in other languages it is know as Array
tea_varities = ["Oolong", "White", "empty", "Black", "Green", "Da Hong Pao", "Panda Dung Tea", "Vintage Pu'erh Tea", "Gyokuro", "Yellow Gold Buds", "Herbal"]
print(tea_varities[3])

tea_varities[2:3] = ["Lemon"]
print(tea_varities) # this will replace "empty" with "Lemon" and we can change even multiple with one or one with multiple

for tea in tea_varities:
   print(tea)
   print(tea, end="-")

if "Oolong" in tea_varities:
   print("Yes i have do you want Oolong tea")

#  LIST COMPARIHANSON
cubed_number = [x**3 for x in range(10)]
print(cubed_number)