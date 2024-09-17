# Create an empty dictionary named 'prices' to store the prices of different items
# A dictionary is like a special list where each item has a unique name (key) and a value associated with it

prices = {}  # This is an empty dictionary with no items yet

# Add a new entry to the dictionary
# The key 'banana' represents the item, and the value '1.49' is the price of the banana
prices['banana'] = 1.49  

# Print the dictionary to show the new entry that was added
print(f'Prices after adding banana: {prices}\n')  
# Output: {'banana': 1.49} - The dictionary now contains one item: 'banana' with a price of 1.49

# Modify the price of the existing entry 'banana'
# Update the value for the key 'banana' from 1.49 to 1.69
prices['banana'] = 1.69  

# Print the dictionary to show the updated price for the banana
print(f'Prices after modifying banana: {prices}\n')  
# Output: {'banana': 1.69} - The price of 'banana' has been changed to 1.69

# Remove the entry for 'banana' from the dictionary
# The del statement deletes the key-value pair for 'banana'
del prices['banana']  

# Print the dictionary to show that the entry for 'banana' has been removed
print(f'Prices after removing banana: {prices}\n')  
# Output: {} - The dictionary is now empty because the 'banana' entry was removed
