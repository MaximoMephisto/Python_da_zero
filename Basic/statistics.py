# Mean: Average of a set of numbers. 
# The total sum of the numbers in a set 
# divided by the total number of numbers to find the mean
numbers = [10, 20, 30, 40, 50]
mean = sum(numbers) / len(numbers)
print(sum(numbers))
print(len(numbers))
print(f"Mean: {mean}")

# Median: The middle value in a sorted list of numbers.
# The sorted() function returns a sordet list
sorted_data = sorted(numbers)
number = len(sorted_data)

if number % 2 == 0:
    median_1 = sorted_data[number//2 - 1]
    median_2 = sorted_data[number//2]
    median = median_1 + median_2 / 2
else:
    median = sorted_data[number // 2]
print(f"Median: {median}")

# Mode: Is the value that appears most frequently in the dataset
# Count() for count the presence of elements
other_numbers = [12, 15, 15, 16, 17, 16, 16]

# Frequence map
frequence = {}

for n in other_numbers:
    if n in frequence: # If n is in frequence loop increment number
        frequence[n] += 1
    else:
        frequence[n] = 1

max_frequence = max(frequence.values())

mode = []
for n, conteggio in frequence.items():
    if conteggio == max_frequence:
        mode.append(n)

print(f"Mode: {mode}")