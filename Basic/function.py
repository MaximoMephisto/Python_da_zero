# Simple function of print values with name and surname as parameters
def print_values(name, surname):
    print(f"Hi! my name is {name} {surname}")

input_nome = input("Insert your name: ")
input_cognome = input("Insert you surname: ")

print_values(input_nome, input_cognome)

# Simple calculator functions
def sum(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

input_a = float(input("Insert first number:"))
input_b = float(input("Insert second number:"))

print(f"Sum: {sum(input_a, input_b)}")
print(f"Subtraction: {subtract(input_a, input_b)}")
print(f"Multiplication: {multiply(input_a, input_b)}")
print(f"Division: {divide(input_a, input_b)}")

# Function to return even numbers from a list
def even_number(list):
    even_numbers = []
    for i in list:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

numbers = int(input("Insert the number of elements in the list: "))
list = []
for i in range(numbers):
    list.append(i)
print(f"Even numbers in the list: {even_number(list)}")

