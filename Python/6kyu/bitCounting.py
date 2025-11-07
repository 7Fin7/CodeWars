
def count_bits(num):

    # Convert num to decimal
    binary_result = ""

    # Repeat process until num becomes 0
    while num > 0:

        # Find the remainder when dividing by 2 — this gives the current binary digit (0 or 1)
        rem = num % 2

        # Divide the number by 2 using integer division (//) to move to the next binary place value
        num = num // 2

        # Add the current binary digit (as a string) to the result
        # We build the binary number backwards since the least significant bit (rightmost) comes first
        binary_result += str(rem)

    # Since digits are collected in reverse order, reverse the string before returning
    binary_result = binary_result[::-1]

    return binary_result.count("1")

print(count_bits(1234))
print(count_bits(9))
print(count_bits(10))


# Write a function that takes an integer as input, and returns the number of bits 
# that are equal to one in the binary representation of that number. You can 
# guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function 
# should return 5 in this case