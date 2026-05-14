# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y

def suma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def expo(a, b):
    return a ** b

def f_division(a, b):
    return a // b

print("1) Suma ")
print("2) Sottrazione ")
print("3) Moltiplicazione ")
print("4) Divizione ")
print("5) Modulo ")
print("6) Esponenziazione ")
print("7) F_Division ")

opt = int(input("Select an option: "))

num_1 = int(input("First number: "))
num_2 = int(input("Second number: "))

if opt == 1:
    print(suma(num_1, num_2))
elif opt == 2:
    print(sub(num_1, num_2))
elif opt == 3:
    print(mult(num_1, num_2))
elif opt == 4:
    print(div(num_1, num_2))
elif opt == 5:
    print(mod(num_1, num_2))
elif opt == 6:
    print(expo(num_1, num_2))
elif opt == 7:
    print(f_division(num_1, num_2))
else:
    print("Error, select just option with numbers (Es: 1)")
