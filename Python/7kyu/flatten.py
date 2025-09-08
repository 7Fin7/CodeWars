
def flatten(lst):

    result = []
    for element in lst:
        if isinstance(element, list):
            result.extend(element)
        else:
            result.append(element)

    return result


print(flatten([1,2,3]))
print(flatten([[1,2,3],["a","b","c"],[1,2,3]]))
print(flatten([[[1,2,3]]]))


# Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of flattening.

# flatten([1,2,3])  ==> [1,2,3]
# flatten([[1,2,3],["a","b","c"],[1,2,3]])  ==> [1,2,3,"a","b","c",1,2,3]
# flatten([[[1,2,3]]])  ==> [[1,2,3]]


# Step-by-step logic:

# Loop through each element in lst.
# Check:
    # If element is a list → add list to result
    # Else → append element directly.
# Return result.