# ------------------------------------------------------------------------------------------ #
# Title: The  types
# Desc: Shows how to use the print function for output
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# ------------------------------------------------------------------------------------------ #
# Define the program's data
product_category: str
product_name: str
message: str
product_price: float
discount: float

# Concatenation "adds" two string together using the plus sign
product_category = "Hardware"
product_name = "Hammer"
message = product_name + "s are considered " + product_category
print(message)

# However, Python adds values when you use a plus sign with two numbers
product_price = 19.99
discount: float = 1.00
total_with_discount = product_price - discount
print(total_with_discount)

# Python will give you an error message if you try to "add" a number and a string
# message = product_name + " are currently " + total_with_discount_flt
# TypeError: can only concatenate str (not "float") to str

# You can fix this by converting the float to a string using the str() function
message = product_name + "'s are currently " + str(total_with_discount)
print(message)

# By the way, the Print function will automatically convert the float to string
print(product_name, "are currently", total_with_discount)  # and add spaces too

# However, for longer messages you use the += option to add more to a variable
message = product_name + "'s are currently " + str(total_with_discount)
message += " (This price includes a $" + str(discount) + "0 discount)"
print(message)  # Note we will use a better formatting option later in the course!
