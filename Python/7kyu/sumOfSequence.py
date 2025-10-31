
def sequence_sum_v1(begin, end, step):
    
    sum = 0

    if begin <= end:
        for i in range(begin, end+1, step):
            sum += i

        return sum
    
    return 0

# Better solution
def sequence_sum_v2(begin, end, step):
    return sum(range(begin, end+1, step))

print(sequence_sum_v2(2, 2, 2))
print(sequence_sum_v2(2, 6, 2))
print(sequence_sum_v2(1, 5, 3))
print(sequence_sum_v2(5, 2, 1))

# Your task is to write a function which returns the sum of a sequence of integers.

# The sequence is defined by 3 non-negative values: begin, end, step.

# If begin value is greater than the end, your function should return 0. If end is not the 
# result of an integer number of steps, then don't add it to the sum. See the 4th example below.

# Examples

# 2,2,2 --> 2
# 2,6,2 --> 12 (2 + 4 + 6)
# 1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
# 1,5,3  --> 5 (1 + 4)