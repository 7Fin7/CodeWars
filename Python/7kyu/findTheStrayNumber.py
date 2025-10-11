
def stray(arr):

    for num in arr:
        if arr.count(num) == 1:
            return num

print(stray([1, 1, 2]))
print(stray([5, 5, 5, 7, 5]))

# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The input array will always be valid! (odd-length >= 3)

# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3

# ALTERNATIVE METHOD USING DICTIONARY

def stray2(arr):
    
    num_count = {}

    # Count each number once
    for num in arr:
        num_count[num] = num_count.get(num, 0) + 1

    # Find the number that appears only once
    for num, count in num_count.items():
        if count == 1:
            return num