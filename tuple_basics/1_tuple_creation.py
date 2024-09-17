# This code demonstrates how tuples work in Python. An error is expected at the end of this code 
# to show that tuples are immutable, which means their values cannot be changed once they are created.

print()
# Define a tuple named 'white_house_coordinates' with two values: latitude and longitude
white_house_coordinates = (38.8977, 77.0366)

# Print the entire tuple to show the coordinates of the White House
print(f'Coordinates: {white_house_coordinates}')  # Output: (38.8977, 77.0366)

print()
# Print the length of the tuple using len(), which gives the number of elements in the tuple
print(f'Tuple length: {len(white_house_coordinates)}')  # Output: 2, because the tuple has 2 values

print()
# Access and print the first element of the tuple (latitude) using index 0
print(f'\nLatitude: {white_house_coordinates[0]} north')  # Output: 'Latitude: 38.8977 north'

print()
# Access and print the second element of the tuple (longitude) using index 1
print(f'Longitude: {white_house_coordinates[1]} west\n')  # Output: 'Longitude: 77.0366 west'

# Attempt to change the second value (longitude) of the tuple
# This line will cause an error because tuples are immutable (you cannot change their values)
white_house_coordinates[1] = 50  # Expected error: TypeError: 'tuple' object does not support item assignment
