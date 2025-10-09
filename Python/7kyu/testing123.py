
def number(lines):

    result = []

    for index, content in enumerate(lines):
        result.append(f"{index + 1}: {content}")

    return result

print(number([]))
print(number(["a", "b", "c"]))
print(number(["test1", "test2", "test3"]))

# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]