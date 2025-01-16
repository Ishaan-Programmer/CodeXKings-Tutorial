# Variables 
a = 10 # ----> a is a variable that stores 10 in the memory

# Data Types
num = 55 # ----> Integer data type
decimal = 6.67 # -----> Floating point number data type
text = "readme" # -----> String data type
b = True # -----> Boolean data type
nothing = None # -----> None data type

# Rules for writing Variable
ishaan = 45 # it doesn't throw error
# 9ishaan = 10 # it does throw error
_my_name_is = "Ishaan" # it doesn't throw error

# Operators in Python

# 1. Arithmetic Operators
a = 7
b = 4
c = a+b
print(c)

# 2. Assignment Operators
a = 4-2 # Assign 4-2 in a
print(a)
b = 6
# b += 3 # Increment the value of b by 3 and then assign it to b
b -= 3 # Decrement the value of b by 3 and then assign it to b
print (b)

# 3. Comparison Operators
d = 5==5
print(d)

# 4. Logical Operators
e = True or False

# Truth table of 'or'
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is", False or False)

# Truth table of 'and'
print("True and False is", True and False)
print("True and True is ", True and True)
print("False and True is", False and True)
print("False and False is", False and False)

print(not(False))

# Type() function and Type Casting:

# 1. Type Casting
num1 = 5
print(type(num1))

name = "Shreyash"
print(type(name))

nothing1 = None
print(type(nothing1))

# 2. Type() function
num2 = "55.6"
num3 = float(num2)
print(num3)

user = 23
user1 = str(user)
print(type(user1))

# Input() Function:
a = int(input("enter name ")) # if a is "ishaan", the user entered ishaan 
print(a)
print(type(a))
c = a + 5
print(c)




