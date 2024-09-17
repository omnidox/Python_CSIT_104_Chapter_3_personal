# Creating two sets named 'fruits' and 'more_fruits' for demonstration
fruits = {'apple', 'banana', 'cherry'}  # A set of some fruits
more_fruits = {'orange', 'grape'}  # Another set of different fruits

# Operation 1: Find the length of the set using len()
fruits_length = len(fruits)  # Finds the number of elements in the 'fruits' set
print(f'The number of fruits in the set is: {fruits_length}\n')  # Output: 3, because there are 3 fruits

# Operation 2: Add the elements of 'more_fruits' to 'fruits' using update()
fruits.update(more_fruits)  # Adds all the fruits from 'more_fruits' to the 'fruits' set
print(f'Fruits set after adding more fruits: {fruits}\n')  
# Output: {'apple', 'banana', 'cherry', 'orange', 'grape'}

# Operation 3: Add a new fruit to the 'fruits' set using add()
fruits.add('kiwi')  # Adds 'kiwi' to the 'fruits' set
print(f'Fruits set after adding "kiwi": {fruits}\n')  
# Output: {'apple', 'banana', 'cherry', 'orange', 'grape', 'kiwi'}

# Operation 4: Remove a fruit from the 'fruits' set using remove()
fruits.remove('banana')  # Removes 'banana' from the 'fruits' set
print(f'Fruits set after removing "banana": {fruits}\n')  
# Output: {'apple', 'cherry', 'orange', 'grape', 'kiwi'}

# Operation 5: Remove a random fruit from the 'fruits' set using pop()
removed_fruit = fruits.pop()  # Removes a random fruit from the set
print(f'Removed fruit: {removed_fruit}')  # Shows which fruit was removed
print(f'Fruits set after popping a random fruit: {fruits}\n')  
# Output: Shows the fruits set after a random fruit is removed

# Operation 6: Clear all elements from the 'fruits' set using clear()
fruits.clear()  # Removes all fruits from the set
print(f'Fruits set after clearing all elements: {fruits}\n')  
# Output: set(), which means the set is now empty
