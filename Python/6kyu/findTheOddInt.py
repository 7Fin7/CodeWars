
def find_it(seq):

    num_count = {}

    for num in seq:
        num_count[num] = num_count.get(num, 0) + 1

    for num, count in num_count.items():
        if count % 2 != 0:
            return num
        
print(find_it([1, 1, 2]))
print(find_it([3, 3, 3, 3, 5]))

# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

# ALTERNATE METHOD USING COUNT

def find_it(seq):

    for num in seq:
        if seq.count(num) % 2 != 0:
            return num
        
print(find_it([1, 2, 2]))
print(find_it([7]))