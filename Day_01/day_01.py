# Day 1 - 30 Days of Python
# Exercise from https://github.com/Asabeneh/30-Days-Of-Python

# Level 1 - Q2: Operations with 3 and 4
print(3 + 4) # addition
print(3 - 4) # subtraction
print(3 * 4) # multiplication
print(3 % 4) # modulus
print(3 / 4) # division
print(3 ** 4) # exponential
print(3 // 4) # floor division

# Level 1 - Q3: Strings
print("Veera Manohar B") # Your name
print("B") # Your family name
print("India") # Your country
print("I am enjoying 30 days of python")

# Level 1 - Q4: Check data types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Veera Manohar B"))
print(type("B"))
print(type("India"))

# Level 3 - Q1: Different data types
print("\n--- Level 3 ---")
print(type(10)) # int
print(type(3.14)) # float
print(type(1 + 3j)) # complex
print(type("Hello")) # string
print(type(True)) # bool
print(type([1, 2, 3])) # list
print(type((1, 2))) # tuple
print(type({1, 2, 3})) # set
print(type({'name':'Veera'})) # dict

# Level 3 - Q2: Euclidean distance between (2, 3) and (10, 8)
import math
dist = math.sqrt((10 - 2)**2 + (8 - 3)**2)
print(f"Euclidean distance: {dist}")