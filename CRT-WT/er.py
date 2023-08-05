def is_same_number(number):
    # Convert the number to a string and reverse it
    number_str = str(number)[::-1]
    # Convert the reversed string back to an integer
    number_x = int(number_str)
    
    # Compare the original number with the reversed number
    if number == number_x:
        return True
    else:
        return False

# Read the input number from the user
number = int(input())

# Check if the number is the same on Planet X
result = is_same_number(number)

# Print the result
print(result)