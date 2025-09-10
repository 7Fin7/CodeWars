
def get_count(sentence):
    
    vowels = "aeiou"
    count = 0

    for letter in sentence:
        if letter in vowels:
            count += 1

    return count

print(get_count("How many vowels are in this sentence?"))

# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata.
# The input string will only consist of lower case letters and/or spaces.
