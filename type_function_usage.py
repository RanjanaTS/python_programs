# type() returns the type/class of a value
print("data type of 7          :", type(7)) # output : <class 'int'>
print("data type of 3.14       :", type(3.14)) # output : <class 'float'>
print("data type of 'hello'    :", type('hello')) # output : <class 'str'>
print("data type of [1, 2, 3]  :", type([1, 2, 3])) # output : <class 'list'>
print("data type of (1, 2)     :", type((1, 2))) # output : <class 'tuple'>
print("data type of {'key': 'value'} :", type({'key': 'value'})) # output : <class 'dict'>
print("data type of True       :", type(True)) # output : <class 'bool'>
print("data type of range(5)   :", type(range(5))) # output : <class 'range'>

print(type(int))   # ➤ Output: <class 'type'>
# 'int' is a class/type used to create integer values like 7.
# In Python, classes themselves are objects.
# The type of any class (like int, str, list) is 'type'.

# So:
# type(7)    → int       (value → type)
# type(int)  → type      (type → meta-type)

# All types in Python (int, str, float, list, etc.) are objects of the class 'type'.
