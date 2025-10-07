
def remove_smallest(numbers):

    if numbers:
        nums = numbers.copy()
        smallest = nums[0]

        for num in nums[1:]:
            if num < smallest:
                smallest = num

        nums.remove(smallest)

        return nums
    
    return []

print(remove_smallest([1, 2, 3, 4, 5]))
print(remove_smallest([5, 6, 2, 1]))

# Task
# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there 
# are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, 
# return an empty array/list.

# Don't change the order of the elements that are left.

# Examples
# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]

# ALTERNATIVE SOLUTION: use mins instead