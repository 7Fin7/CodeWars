
def validate_pin(pin):
    return pin.isdigit() and len(pin) in (4, 6)

print(validate_pin("1234"))
print(validate_pin("12345"))

# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false