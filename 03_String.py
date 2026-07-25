# STRING SPLIT
str = "Lemon, Masala, Ginger, Mint, Clove"
print(str.split(", "))

# Count
chai = "Masala chai chai chai"
print(chai.count("chai"))

# Order formating
chai_type = "Masala"
quantity = 3
order = "I odered {} cups of {} chai"
print(order.format(quantity, chai_type))

# list to string
li = ["Masala", "Ginger", "Lemon"]
print(", ".join(li))

chai = "He said, \"Masala Chai is Awesome\""
print(chai)

raw_string = r"c:\user\pwd"
print(raw_string)

chai_name = "Masala chai"
print("Masala" in chai_name)
print("Masalaa" in chai_name)