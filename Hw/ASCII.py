print("ASCII Value Checker")
print("-" * 30)

char = input("Enter one character: ")

if len(char) == 1:
    ascii_val = ord(char)

    print("Character:", char)
    print("ASCII Value:", ascii_val)


    if ascii_val >= 65 and ascii_val <= 90:
        print("Character Type: Uppercase Letter")
    elif ascii_val >= 97 and ascii_val <= 122:
        print("Character Type: Lowercase Letter")
    elif ascii_val >= 48 and ascii_val <= 57:
        print("Character Type: Digit")
    else:
        print("Character Type: Special Character")
else:
    print("Error: Please enter exactly one character.")
