"""
100 days of Python course
DAY 2
"""

# note that input for height is with a fullstop as decimal place
# and that weight is not a decimal number so that we can
# explore the differences between int and float
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weight_as_int = int(weight)
height_as_float = float(height)

# two approaches to calculate below: line 17 is what will be stored in bmi
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2

# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)
