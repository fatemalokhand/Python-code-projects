# Importing the system library
import sys

# Creating a boolean variable to store if the 'A' input is a '1' or a '0'
a = (sys.argv[1] == '1')

# Creating a boolean variable to store if the 'B' input is a '1' or a '0'
b = (sys.argv[2] == '1')

# Creating a boolean variable to store if the 'C' input is a '1' or a '0'
c = (sys.argv[3] == '1')

# Creating a boolean variable to store if the 'G' input is a '1' or a '0'
g = (sys.argv[7] == '1')

# Creating a boolean variable to store if the 'H' input is a '1' or a '0'
h = (sys.argv[8] == '1')

# Creating a boolean variable to store if the 'K' input is a '1' or a '0'
k = (sys.argv[11] == '1')

# Creating the first logical expression that corresponds to the first assigned circuit
logical_expression_one = (((b or c) or (not a)) and (not b))

# Creating the second logical expression that corresponds to the second assigned circuit
logical_expression_two = ((((not k) or h) or (not g)) or h)

# Printing out an empty line
print()

# Printing out both comma-separated results inside triangle brackets
print(f"<{logical_expression_one}, {logical_expression_two}>")
