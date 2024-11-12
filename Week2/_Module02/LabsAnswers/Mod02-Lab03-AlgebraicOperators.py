# ------------------------------------------------------------------------------------------ #
# Title: Module02-Lab03-AlgebraicOperators
# Desc: Practice working with algebraic operators
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
first_number: float
second_number: float
sum: float
difference: float
product: float
quotient: float
modulo: float

# Input user data using is the assignment operator
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Process data using addition, subtraction, multiplication, and division operators
sum = first_number + second_number
difference = (first_number - second_number)  # "You can also use the optional abs function
product = first_number * second_number
quotient = first_number / second_number
modulo = first_number % second_number  # Modulo shows a remainder

# Output processed data to the user
print("The sum is: " + str(sum))  # Concatenation print with auto conversion
print("The difference is: ", difference)  # Standard print with auto conversion
print(f"The product is: {product}")  # The f String

message_str = "The {} is: {}"  # Create a reuseable message
print(message_str.format("quotient", quotient))  # The format() function
print(message_str.format("modulus", modulo))  # The format() function with numbered place holders
