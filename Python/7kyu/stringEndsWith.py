
def solution(text, ending):
    return ending == text[-len(ending):]

print(solution("abc", "bc"))
print(solution("test", "est"))
print(solution("shouldBeFalse", "true"))

# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# Inputs: "abc", "bc"
# Output: true

# Inputs: "abc", "d"
# Output: false