
def binary_array_to_number(arr):
    
    # Reverse list to make it easier to add up from left to right
    arr.reverse()

    # Initialise sum
    int_sum = 0

    # Loop through length of arr
    for i in range(len(arr)):
        # Either 0 or 1 multiplied by 2**0, 2**1, 2**2...which are equal to 1, 2, 4...
        int_val = arr[i] * 2 ** i

        # Sum value
        int_sum += int_val

    return int_sum

print(binary_array_to_number([1, 1, 1, 1]))


# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

# Examples:

# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
# However, the arrays can have varying lengths, not just limited to 4.

# HERE IS MY FIRST CORRECT ATTEMPT THAT IS AWFUL

def binary_array_to_number_v2(arr):
    
    sum = 0
    binary = [1]

    for i in range(1, len(arr)):
        binary.append(2 ** i)

    binary.reverse()

    for i, digit in enumerate(arr):
        sum += binary[i] * digit

    return sum