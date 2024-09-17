# This example demonstrates three different methods in Python to format strings and specify the number of decimal places (precision)
# for numerical values, such as money. The three methods — f-strings, the format() method, and the % formatting operator — allow
# us to control how numbers are displayed in the output, especially for values that involve currency or need to be formatted 
# with a specific number of decimal places. Each method formats the 'amount' variable to display two decimal places (e.g., $32.00), 
# making the output consistent and precise for financial calculations or display purposes.


# Defining variables
number = 6  # This variable holds the number of burritos
amount = 32  # This variable holds the total cost in dollars

print()  # Print a blank line for spacing

# Method 1: Using f-string formatting
# The f-string allows us to easily insert variables and specify decimal precision
print(f'Using f-string: {number} burritos cost ${amount:.2f}')  # Output: 'Using f-string: 6 burritos cost $32.00'

print()  # Print another blank line for spacing

# Method 2: Using the format() method
# The format() method can also be used to insert variables and specify decimal precision
print('Using format(): {} burritos cost ${:.2f}'.format(number, amount))  # Output: 'Using format(): 6 burritos cost $32.00'

print()  # Print another blank line for spacing

# Method 3: Using the % formatting operator
# The % operator provides another way to insert variables and specify decimal precision
print('Using %% operator: %d burritos cost $%.2f' % (number, amount))  # Output: 'Using % operator: 6 burritos cost $32.00'

print()  # Print a final blank line for spacing
