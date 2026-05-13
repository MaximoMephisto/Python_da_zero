# Every Python file is a module. 
# This means that 'basic.py' is a module, 
# as are 'list.py' and this one, 'modules.py'

# If you want to use code from another module, you can import it
import suma_module
# Now we can use the 'suma' function from 'suma_module'
result = suma_module.suma(3, 4)
# This will print 7
print(result)  

# Python have a ramdom module, that we can use to generate random numbers
import random
# This will print a random number between 1 and 10
random_number = random.randint(1, 10)
print(random_number)

# shuffle function
# This will shuffle a list of numbers
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# choice function
# This will print a random element from the list
random_element = random.choice(numbers)
print(random_element)
