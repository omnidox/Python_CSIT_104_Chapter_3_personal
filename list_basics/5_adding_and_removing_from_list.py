print()

# Create a list named 'my_list' with two elements: the number 10 and the string 'bw'
my_list = [10, 'bw']

# Print the original list 'my_list' to show its contents
print(my_list)  # Output: [10, 'bw']

print()

# Add (append) a new element 'abc' to the end of the list
my_list.append('abc')

# Print the list after the append to show the new element added at the end
print(f'After append: {my_list}')  # Output: After append: [10, 'bw', 'abc']

print()

# Remove the element at index 1 (the second element, which is 'bw') from the list
my_list.pop(1)

# Print the list after the pop to show the element removed
print(f'After pop: {my_list}')  # Output: After pop: [10, 'abc']


print()

# Remove the element 'abc' from the list by its value
my_list.remove('abc')

# Print the list after the remove to show the element removed
print(f'After remove: {my_list}')  # Output: After remove: [10]

print()