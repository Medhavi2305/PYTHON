import random
import math
from decimal import Decimal
from fractions import Fraction
# POWER
print(2 ** 2) # TWO POWER TWO

print(int(2.33)) # VALUE INTO INTEGER
print(float(30)) # VALUE INTO DECIMAL

x = 1
y = 2
z = 3
print(x, y, z)

print(math.floor(3.5)) 

# COMPLEX NUMBER 
print((2 + 3j) * 3)

print(0o20) # Octal Number
print(0x23) # Hex Number
print(0b1000) # Binnary Number

print(oct(55)) 
print(hex(55))
print(bin(55))

print(int('55', 8))
print(int('55', 16))
print(int('110011', 2))

print(3 << 3) # Left bit by 3 shift

print(random.random())
print(random.random(1, 10))

l1 = ['mint', 'masala', 'ginger', 'lemon']
print(random.choice(l1))
print(random.shuffle(l1))

print(0.1 + 0.1 + 0.1 - 0.3)
print(
   Decimal(0.1) +  Decimal(0.1) + Decimal(0.1) - Decimal(0.3)
)

myFra = Fraction(2, 7)
print(myFra)
myFra

setone = {1, 2, 3, 4, 5}
setone & {1, 3} # Intersection
setone | {1, 3} # Union
setone | {1, 3, 6} # Union
setone - {1, 2, 3, 4, 5}