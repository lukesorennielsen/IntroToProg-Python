def AddValues(v1, v2):
    try:
        sum = v1 + v2
    except:
        raise
    return sum


def SubtractValues(v1, v2):
    try:
        dif = v1 - v2
    except:
        raise
    return dif


def MultiplyValues(v1, v2):
    try:
        prod = v1 * v2
    except:
        raise
    return prod


def DivideValues(v1, v2):
    try:
        quot = v1 / v2
    except:
        raise
    return quot





number1 = 5
number2 = 4
print(number1 + number2)  # Output: 9
print(number1 - number2)  # Output: 1
print(number1 * number2)  # Output: 20.
print(number1 / number2)  # Output: 1.25
print(number1 % number2)  # Output: 1
