#         0  1  2  3  4 <-- Positions #
list_1 = [1, 2, 3, 4, 5]
    
list_2 = [2, "hi", 3, "my", 5]

# To access the desired value, we indicate its position
print(f"Your number is: {list_1[3]}")

# For multiple values
print(f"Three number of the list: {list_1[1:4]}")

# To update the list data
print(f"Original list {list_1[:]}")
list_1[3] = 7
print(f"New list: {list_1[:]}")

# To add a element in the end list
list_1.append(7)
print(list_1)

# With a function
list = []
a = 0
b = 5
while (a < b):
    number_for_list = input("Enter a five numbers: ")
    list.append(number_for_list)
    a += 1
print(list)

# Delete a element
delete_element = int(input("Delete with position: "))
del list[delete_element]
print(list)

delete_element_two = input("Select element do you want delete: ")
list.remove(delete_element_two)
print(list)