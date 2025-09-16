
def accum(st):
    
    length = len(st)
    result = ""

    for i, letter in enumerate(st):
        result += letter.upper() + letter.lower() * i + "-"

    return result[:-1]

print(accum("abcd"))


# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.