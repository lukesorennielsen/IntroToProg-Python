# ------------------------------------------------------------------------------------------ #
# Title: The  types
# Desc: Shows how to use the Format() function to format strings
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the program's data
product_name: str
product_price: float
discount: float
message: str

# Python adds values when you use a plus sign with two numbers
product_name = "Hammer"
product_price = 19.99
discount = 1.00
total_with_discount = product_price - discount

# Processing with Concatenation
# Concatenation "adds" two string together using the plus sign
message = product_name + "'s are " + str(product_price) + "."
print("Standard Concatenation")
print(message)
print("--------------------------------------------------------------")

# Processing with Substitution Parameters
# Substitution adds strings to a string based on parameters indicated with a % sign
message = " %s's are %d." % (product_name, total_with_discount)
print("The Substitution Parameter Option")
print(message)
print("--------------------------------------------------------------")

# The format() function
#  adds strings to a string based on parameters indicated with {} signs
message = "{}s are {}.".format(product_price, total_with_discount)
print("The Substitution Parameter Option")
print(message)
print("--------------------------------------------------------------")

# You also use the format() function on any string variable like this
message = "{}s are currently {}. (This price includes a {} discount)"
print("The format() Function Option")
print(message.format(product_name, total_with_discount, discount))
print("--------------------------------------------------------------")

# The format() function has built in formatting codes like this one for a
# floating point number with two values after the decimal
message = "{}s are currently ${:.2f}. (This price includes a ${:.2f} discount)"
print("The format() Function with a custom format code")
print(message.format(product_name, total_with_discount, discount))
print("--------------------------------------------------------------")

message = f"{product_name}s are currently "
message += f"${total_with_discount:.2f}. "
message += f"(This price includes a ${discount:.2f} discount)"
print("The f-string Option with a custom format code")
print(message)
print("--------------------------------------------------------------")

# Formatting Constants
# If we do not expect a formatted message to change we can make it a constant
MESSAGE: str = "{}s are currently ${:.2f}. (This price includes a ${:.2f} discount)"

# Now, we define and set variables to store the data
product_name = "Hammer"
product_price = 19.99
discount = 1.00
total_with_discount = product_price - discount

# Then display for the user to see
print(MESSAGE.format(product_name, total_with_discount, discount))

# Afterwards, we can change the data values and reuse in our program like this:
product_name = "1lb -Nail"
product_price = 7.99
discount = 0.00
total_with_discount = product_price - discount

print(MESSAGE.format(product_name, total_with_discount, discount))

# Warning
# Don't use a string with the {:.2f} format code or you will get a
# ValueError: Unknown format code 'f' for object of type 'str'
test_number: str = "123.45"  # This has double-quotes around it
print("This is a decimal number {:.2f}".format(test_number))  # ERROR!
print("--------------------------------------------------------------")  # This line never runs!

# Here is a simple article for reference
# https://www.w3schools.com/python/ref_string_format.asp
