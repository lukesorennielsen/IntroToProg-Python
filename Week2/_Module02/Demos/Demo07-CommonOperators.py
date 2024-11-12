# ------------------------------------------------------------------------------------------ #
# Title: Common Operators
# Desc: Shows several examples of Operators
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
result: None
number1: int
number2: int


# The Parentheses Operator determines the order of operation in arithmetic
result: int = (4 * (2 + 2))
print(result)

# The Parentheses Operator extract a character from a string
result: str = "This is a test"[1]  # This will change the data type to a string of one character
print(result)  # Output: h

# The not operator changes a True output to False, or the reverse
result: bool = not True
print(result)  # Output: False
print(not result)  # Output: True

# The != operator evaluates to True if data is not equal to each other.
number1 = 5
number2 = 4
print(number1 != number2)  # Output: True

# The common arithmetic operators work the same in almost every programming language.
number1 = 5
number2 = 4
print(number1 + number2)  # Output: 9
print(number1 - number2)  # Output: 1
print(number1 * number2)  # Output: 20.
print(number1 / number2)  # Output: 1.25
print(number1 % number2)  # Output: 1

# Comparison or Logical operators work the same as in algebra too
result: bool = number1 > number2
print("The first number is greater than the second: ", result)  # Output: True


result = number1 < number2
print("The first number is less than the second: ", result)  # Output: False

result = number1 == number2
print("The first number is equal to the second: ", result)  # Output: False

result = number1 >= number2
print("The first number is greater than or equal to the second: ", result)  # Output: True

result = number1 <= number2
print("The first number is less than or equal to the second: ", result)  # Output: False

# Here is a good article for more information
# https://realpython.com/python-operators-expressions/
