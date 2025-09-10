
def disemvowel(str):
    
    vowels = "aeiouAEIOU"
    result = ""

    for char in str:
        if char not in vowels:
            result += char
    
    return result

print(disemvowel("This website is for losers LOL!"))
print(disemvowel("Trolls are attacking!"))

# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".