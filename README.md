Type Conversion in Programming
Introduction
Type conversion is the process of converting a value from one data type to another. It is commonly used when working with different types of data, such as integers, floating-point numbers, and strings.

Types of Type Conversion
1. Implicit Type Conversion
Implicit type conversion happens automatically by the programming language without requiring the programmer to convert the value manually.

Example in Python:


a = 10
b = 2.5

result = a + b

print(result)        # 12.5
print(type(result))  # <class 'float'>
In this example, Python automatically converts the integer 10 into a floating-point number during the addition.

2. Explicit Type Conversion
Explicit type conversion happens when the programmer manually converts a value from one data type to another using conversion functions.

Example in Python:


number = "100"

converted_number = int(number)

print(converted_number)        # 100
print(type(converted_number))  # <class 'int'>
Here, the string "100" is converted into the integer 100 using the int() function.

Common Type Conversion Functions in Python

Function	Description	Example
int()	Converts a compatible value to an integer	int("25") → 25
float()	Converts a compatible value to a float	float("3.5") → 3.5
str()	Converts a value to a string	str(100) → "100"
bool()	Converts a value to a Boolean	bool(1) → True
list()	Converts an iterable into a list	list("abc") → ['a', 'b', 'c']
tuple()	Converts an iterable into a tuple	tuple([1, 2]) → (1, 2)
set()	Converts an iterable into a set	set([1, 1, 2]) → {1, 2}
Example Program

# Integer to float
a = 10
print(float(a))  # 10.0

# Float to integer
b = 5.8
print(int(b))    # 5

# Integer to string
c = 25
print(str(c))    # "25"

# String to integer
d = "50"
print(int(d))    # 50

# Integer to Boolean
e = 1
print(bool(e))   # True
Note: Converting a float to an integer using int() removes the decimal part; it does not round the value. Also, converting an invalid numeric string, such as "hello", using int() raises a ValueError.

Advantages of Type Conversion
Helps perform operations between compatible data types.
Makes it easier to process user input.
Allows data to be represented in the required format.
Helps avoid certain type-related errors.
