
def reverse_words(text):
    
    words = text.split(" ")
    reversed = []

    for word in words:
        reversed.append(word[::-1])

    return " ".join(reversed)

print(reverse_words("This string is getting reversed!"))
print(reverse_words("This is a test"))


# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples

# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"