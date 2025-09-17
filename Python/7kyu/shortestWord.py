
def find_shortest(s):

    word_list = s.split()
    shortest = word_list[0]

    for word in word_list[1:]:
        if len(word) < len(shortest):
            shortest = word

    return len(shortest)

print(find_shortest("turns out random test cases are easier than writing out basic ones"))
print(find_shortest("Let's travel abroad shall we"))

# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.