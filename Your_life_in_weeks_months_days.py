"""
100 days of Python course
DAY 2
"""

# the input is a numeric without decimal point
# we work with the age variable as an integer
# and then round the results so that the output is
# easily understandable to the user
age = input("What is your current age? ")

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

# note the use of f-strings which makes formatting display results easy
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
