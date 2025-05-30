a = int(input("Enter your a value : "))
b = int(input("Enter your b value : "))
a = a + b
b = a - b
a = a - b
print("After swap: a =", a, ", b =", b)
a = a ^ b
b = a ^ b
a = a ^ b
print("Before swap: a =", a, ", b =", b)