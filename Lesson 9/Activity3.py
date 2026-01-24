age = int(input("Enter your age:"))
nationality = input("Enter your nationality:")

required_age = 18
required_n = "Indian"

if nationality == required_n:
    if age >= required_age:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote because you're not 18 yet.")   
else:
    print("You're not Indian, you are not eligible to vote.")          
