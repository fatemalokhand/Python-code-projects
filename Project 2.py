# Importing the system library
import sys

# Getting the command line argument and converting it into an integer
value_one = int(sys.argv[1])

# Printing out an empty line
print()

# Getting a value from the input function call and converting it into an integer
value_two = int(input("Please enter a positive integer: "))

# Subtracting 2 from the value
final_result = value_one - 2

# Printing out an empty line
print()

# Printing out the value
print(final_result)

# Dividing the value by 6 and rounding the result down
final_result = final_result // 6

# Printing out an empty line
print()

# Printing out the value
print(final_result)

# Adding the return value from the input function call
final_result = final_result + value_two

# Printing out an empty line
print()

# Printing out the value
print(final_result)

# Adding it to the integer that is one more than itself
final_result = final_result + (final_result + 1)

# Printing out an empty line
print()

# Printing out the value
print(final_result)

# Multiplying it by 4.866667
final_result = final_result * 4.866667

# Printing out an empty line
print()

# Printing out the value
print(final_result)

# Converting it to an integer
final_result = int(final_result)

# Printing out an empty line
print()

# Printing out the value
print(final_result)

# Converting it to a character
final_result = chr(final_result)

# Printing out an empty line
print()

# Printing out the final result to the screen using triangle brackets
print(f"<{final_result}>")
