# Return the string with initial capital letters
str = "hello world!"
capital_string = str.capitalize()
print(capital_string)

# Find the number of times the specified substring 
# is used as a parameter
specified_letters = str.count("o")
print(f"You have {specified_letters} 'o' in your text")
specified_text = str.count("he")
print(f"You have {specified_text} 'he' in your text")

# Find the first occurrence of the passed substring
find_position = str.find("h")
find_position_two = str.find("w")
print(f"The letter 'h' is in the position {find_position} and the letter 'w' in the position {find_position_two}")

# String concatenated to the past sequence
none_text = ""
iter_text = none_text.join(str)
print(iter_text)

line = "-"
a = line.join(str)
print(a)
