from collections import namedtuple  # Import the namedtuple function from the collections module

# Create a named tuple called 'Car' with fields: make, model, price, horsepower, and seats
Car = namedtuple('Car', ['make', 'model', 'price', 'horsepower', 'seats'])  

# Use the named tuple 'Car' to create an object named 'chevy_blazer' that represents a specific car
chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8)  

# Use the named tuple 'Car' to create another object named 'chevy_impala' to represent a different car
chevy_impala = Car('Chevrolet', 'Impala', 37495, 305, 5)  

# Print the details of the chevy_blazer car
print(f'Chevy Blazer Details:\nMake: {chevy_blazer.make}\nModel: {chevy_blazer.model}\nPrice: ${chevy_blazer.price}\nHorsepower: {chevy_blazer.horsepower}\nSeats: {chevy_blazer.seats}\n')

# Print the details of the chevy_impala car
print(f'Chevy Impala Details:\nMake: {chevy_impala.make}\nModel: {chevy_impala.model}\nPrice: ${chevy_impala.price}\nHorsepower: {chevy_impala.horsepower}\nSeats: {chevy_impala.seats}\n')
