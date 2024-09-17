# Define three sets of fruits to demonstrate different set operations

print()
fruits_set1 = {'apple', 'banana', 'cherry'}  # A set of some fruits
fruits_set2 = {'banana', 'apple', 'grape'}  # Another set of fruits with some overlap
fruits_set3 = {'grape', 'apple', 'kiwi'}  # A third set of fruits with different overlap

# Operation 1: Intersection - Find common elements in all sets using intersection()
common_fruits = fruits_set1.intersection(fruits_set2, fruits_set3)  # Finds fruits that are in all three sets
print(f'Common fruits in all sets: {common_fruits}\n')  
# Output: {'apple'} - Only 'apple' is common in all three sets

# Operation 2: Union - Combine all unique elements from all sets using union()
all_fruits = fruits_set1.union(fruits_set2, fruits_set3)  # Combines all fruits from the three sets without duplicates
print(f'All unique fruits from all sets: {all_fruits}\n')  
# Output: {'banana', 'apple', 'cherry', 'grape', 'kiwi'} - All fruits are included, no duplicates

# Operation 3: Difference - Find elements in fruits_set1 that are not in fruits_set2 or fruits_set3 using difference()
unique_to_set1 = fruits_set1.difference(fruits_set2, fruits_set3)  # Finds fruits in fruits_set1 that are not in the other sets
print(f'Fruits only in the first set: {unique_to_set1}\n')  
# Output: {'cherry'} - Only 'cherry' is unique to fruits_set1

# Operation 4: Symmetric Difference - Find elements that are in either fruits_set2 or fruits_set3, but not in both using symmetric_difference()
different_between_set2_and_set3 = fruits_set2.symmetric_difference(fruits_set3)  # Finds fruits that are in either set but not both
print(f'Fruits in set 2 or set 3, but not both: {different_between_set2_and_set3}\n')  
# Output: {'banana', 'kiwi'} - 'banana' is only in set 2, 'kiwi' is only in set 3
