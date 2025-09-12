
def descending_order(num):

    str_num = str(num)
    list_num = [int(x) for x in str_num]
    
    return int("".join(str(x) for x in sorted(list_num, reverse=True)))
    

# print(descending_order(123))
print(sorted("6537"))

# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321