import math

# Take two numbers and return the result of 
# the first number raised to the power of the second.
number_one = int(input("Enter first number: "))
number_two = int(input("Enter the second number: "))

number_raised = math.pow(number_one, number_two)
print(number_raised)

# Returns the largest integer less than or 
# equal to the number passed as a parameter
float_one = float(input("Enter a float number: "))

integer_number_one = math.floor(float_one)
print(integer_number_one)

# Returns the largest integer equal to or 
# grater than the number passed as a parameter
float_two = float(input("Enter a second float number: "))

integer_number_two = math.ceil(float_two)
print(integer_number_two)

# Receives a parameter and return the absolut value of the number passed
number = int(input("Enter a number: "))

abs_number = abs(number)
print(abs_number)

# Finds the logarithm of a number, accepts one parameter, and returns 
# the natural logarithm of that number. With two parameters, it 
# returns the logarithm of the first number to the second number.
first_number = int(input("Insert a first number: "))
second_number = int(input("Insert a second number: "))

natural_log = math.log(first_number)
log = math.log(first_number, second_number)

print(f"Natural logarithm of the first number {natural_log}. Logarithm with the second number: {log}")

# Square root
numb = int(input("Enter a number: "))

numb_square = math.sqrt(numb)
print(f"The square root of {numb} is {numb_square}")

