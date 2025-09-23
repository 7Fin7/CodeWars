
def add_binary(a, b):
    # Add the two input numbers together
    sum = a + b

    # Initialize an empty string to build the binary result
    binary_result = ""

    # Repeat the process until the sum becomes 0
    while sum > 0:
        # Find the remainder when dividing by 2 (this gives the current binary digit)
        remainder = sum % 2

        # Divide the sum by 2 using integer division to prepare for the next digit
        sum = sum // 2

        # Append the remainder to the binary_result string
        # (remainders come out in reverse order, so we'll reverse the string later)
        binary_result += str(remainder)

    # Since digits are collected in reverse order, reverse the string before returning
    return binary_result[::-1]

print(add_binary(1, 1))
print(add_binary(5, 9))

# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))

# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)