# Initial list named 'first_names' contains some duplicate names
first_names = ['Alba', 'Hema', 'Ron', 'Alba', 'Musa', 'Ron', 'Ron']

# Creating a set from the list 'first_names' to remove duplicate values
# A set automatically removes any repeated names, so each name will appear only once
names_set = set(first_names)

# Print the set to show the unique names
print(f'Unique names in the set: {names_set}\n')  # Output will show each name only once
