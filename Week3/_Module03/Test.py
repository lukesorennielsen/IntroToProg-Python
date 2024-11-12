# Use this file for ad-hoc demos, testing, and troubleshooting

first_number = 100
second_number = 100

print("Zero test")
if (0 == (first_number == second_number)):  # Does False == (True)
    print("true")
else:
    print("false")  # Will be false

print("One test")
if (1 == (first_number == second_number)):  # Does True == (True)
    print("true")  # Will be True
else:
    print("false")

print("Neither Zero or One test")
if (2 == (first_number == second_number)):  # However what about this one?
    print("true")
else:
    print("false")  # Will be False
