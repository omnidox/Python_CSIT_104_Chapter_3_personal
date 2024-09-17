# String (default presentation type - can be omitted)
name = 'Aiden'

print()  # Print a blank line for separation
print()  # Print a blank line for separation

print(f'Displaying a string: {name:s}')  # Output: 'Displaying a string: Aiden'

print()  # Print a blank line for separation

# Decimal (integer values only)
number = 4
print(f'Displaying an integer as a decimal: {number:d}')  # Output: 'Displaying an integer as a decimal: 4'

print()  # Print a blank line for separation

# Decimal (integer values only) with commas
number = 7600
print(f'Displaying an integer with commas: {number:,d}')  # Output: 'Displaying an integer with commas: 7,600'

print()  # Print a blank line for separation

# Leading 0 notation with specified width
number = 4
print(f'Displaying an integer with leading zeros (3 digits wide): {number:03d}')  # Output: 'Displaying an integer with leading zeros (3 digits wide): 004'

print()  # Print a blank line for separation

# Binary (integer values only)
number = 4
print(f'Displaying an integer in binary format: {number:b}')  # Output: 'Displaying an integer in binary format: 100'

print()  # Print a blank line for separation

# Hexadecimal in lowercase and uppercase (integer values only)
number = 31
print(f'Displaying an integer in lowercase hexadecimal: {number:x}')  # Output: 'Displaying an integer in lowercase hexadecimal: 1f'

print()  # Print a blank line for separation

print(f'Displaying an integer in uppercase hexadecimal: {number:X}')  # Output: 'Displaying an integer in uppercase hexadecimal: 1F'

print()  # Print a blank line for separation

# Exponent notation
number = 44
print(f'Displaying a number in exponent notation: {number:e}')  # Output: 'Displaying a number in exponent notation: 4.400000e+01'

print()  # Print a blank line for separation

# Fixed-point notation (six decimal places by default)
number = 4
print(f'Displaying a number in fixed-point notation (6 decimal places): {number:f}')  # Output: 'Displaying a number in fixed-point notation (6 decimal places): 4.000000'

print()  # Print a blank line for separation

# Fixed-point notation with programmer-defined precision
number = 4
print(f'Displaying a number in fixed-point notation (2 decimal places): {number:.2f}')  # Output: 'Displaying a number in fixed-point notation (2 decimal places): 4.00'

print()  # Print a blank line for separation

# Fixed-point notation with programmer-defined precision and commas
number = 7600.1
print(f'Displaying a number in fixed-point notation with commas and 2 decimal places: {number:,.2f}')  # Output: 'Displaying a number in fixed-point notation with commas and 2 decimal places: 7,600.10'
