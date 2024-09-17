# Defining two lists to demonstrate different operations
list1 = [5, 10, 15, 20]
list2 = [25, 30, 35]

# Operation 1: Find the length of the list using len()
length_of_list1 = len(list1)  # Counts the number of elements in list1
print(f'The length of list1 is {length_of_list1}')  # Output: 4, because list1 has 4 elements

print()  # Print a blank line for spacing

# Operation 2: Concatenate list2 to the end of list1 using +
combined_list = list1 + list2  # Joins list1 and list2 together into a new list
print(f'Combining list1 and list2 gives: {combined_list}')  
# Output: [5, 10, 15, 20, 25, 30, 35], because all elements of list2 are added to the end of list1

print()  # Print a blank line for spacing

# Operation 3: Find the smallest value in list1 using min()
smallest_value = min(list1)  # Finds the smallest number in list1
print(f'The smallest value in list1 is {smallest_value}')  # Output: 5, which is the smallest number in list1

print()  # Print a blank line for spacing

# Operation 4: Find the largest value in list1 using max()
largest_value = max(list1)  # Finds the largest number in list1
print(f'The largest value in list1 is {largest_value}')  # Output: 20, which is the largest number in list1

print()  # Print a blank line for spacing

# Operation 5: Find the sum of all elements in list1 using sum()
total_sum = sum(list1)  # Adds up all the numbers in list1
print(f'The sum of all elements in list1 is {total_sum}')  # Output: 50, which is the sum of 5 + 10 + 15 + 20

print()  # Print a blank line for spacing

# Operation 6: Find the index of a value in list1 using index()
index_of_15 = list1.index(15)  # Finds the position of the value 15 in list1
print(f'The index of 15 in list1 is {index_of_15}')  # Output: 2, because 15 is the third element (index starts at 0)

print()  # Print a blank line for spacing

# Operation 7: Count occurrences of a value in list1 using count()

count_of_10 = list1.count(10)

print(f'The number 10 appears {count_of_10} times in list1')  # Output: 2, because 10 appears twice in list1
# Add another 10 to list1
list1.append(10)  # Adds the number 10 to the end of list1

print()  # Print a blank line for spacing
count_of_10 = list1.count(10)  # Counts how many times the number 10 appears in list1
print(f'The number 10 appears {count_of_10} times in list1')  # Output: 2, because 10 appears twice in list1

print()  # Print a blank line for spacing