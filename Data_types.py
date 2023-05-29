"""
100 days of Python course
DAY 2
"""

# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")

# Check the data type of two_digit_number
print(type(two_digit_number))

# Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two digits togeter
two_digit_number = first_digit + second_digit

print(two_digit_number)
