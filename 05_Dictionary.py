user = {"username": "Medhavi2305", "email": "medhavisharma2305", "password": "*******"}
print(user["username"])
print(user.get("username"))

for keys in user:
   print(keys)
   print(keys,":", user[keys])

for key, value in user.items():
   print(key, value)

if "username" in user:
   print("Yes username is there")

print(len(user))

user["isVerified"] = True
print(user)

del user["isVerified"]
print(user)

cubed_number = {x: x**3 for x in range(10)}
print(cubed_number)
cubed_number.clear()
print(cubed_number)

keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)