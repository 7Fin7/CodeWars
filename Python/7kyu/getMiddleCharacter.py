def get_middle(s):

    # If length is even return middle 2 characters
    if len(s) % 2 == 0:
        end = len(s) // 2
        return s[end - 1] + s[end]
    # Else length is odd and return middle character
    else:
        middle = int(len(s) / 2)
        return s[middle]
    
    


print(get_middle("test"))
print(get_middle("floats"))
print(get_middle("guide"))
print(get_middle("testing"))
print(get_middle("s"))

# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

# If the string's length is odd, return the middle character.
# If the string's length is even, return the middle 2 characters.
# Examples:
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"